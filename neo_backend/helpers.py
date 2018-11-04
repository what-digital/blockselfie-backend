from datetime import date

from django.contrib.auth import get_user_model
from django.db.models import QuerySet, Sum
from .models import Question, Schedule, Purchase, QuestionLog


def get_todays_question_as_queryset() -> QuerySet:
    """
    Returning a QuerySet with one instance inside is more practical than returning an instance
    :return:
    """
    if not Schedule.objects.filter(date_published=date.today()).exists():
        todays_schedule = Schedule.objects.exclude(
            has_been_published=True,
        ).exclude(
            date_published__isnull=False,
        ).order_by('sorting').first()

        if todays_schedule:
            todays_schedule.date_published = date.today()
            todays_schedule.has_been_published = True
            todays_schedule.save()
        else:
            return Question.objects.none()

    question_ids = Schedule.objects.filter(
        date_published=date.today()
    ).values_list('question_id', flat=True)

    return Question.objects.filter(pk__in=question_ids)


def get_credit_for_user(user: get_user_model()) -> dict:
    aggregation = Purchase.objects.filter(user=user).aggregate(price=Sum('products__price'))
    total_cost = aggregation.get('price', 0)

    if not total_cost:
        total_cost = 0

    user_question_log = QuestionLog.objects.filter(user=user)

    total_rewards = sum(
        [question_log.get_effective_reward() for question_log in user_question_log if question_log.is_correct()]
    )

    if not total_rewards:
        total_rewards = 0

    try:
        credit = total_rewards - total_cost
    except Exception:
        credit = "n/a"

    return {
        "total_cost": total_cost,
        "total_rewards": total_rewards,
        "credit": credit,
    }
