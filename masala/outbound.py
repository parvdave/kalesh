from .models import Kaleshi
from openai import OpenAI
from django.conf import settings
from django.core.mail import send_mail

client = OpenAI(api_key=settings.OPENAI_API_KEY)

def send_resolution_email(resolution,kaleshi_email_1,kaleshi_email_2):
    subject = f"Your Kalesh Resolution Is Here!"
    message = resolution
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [kaleshi_email_1,kaleshi_email_2]

    send_mail(subject, message, from_email, recipient_list)

def send_email_for_kalesh(kaleshi_slug, kaleshi_email):

        # Prepare email details
    subject = f'You\'ve been drafted to a Kalesh'
    message = f'Welcome to Kalesh\n You can enter your response at: http://127.0.0.1:8000/kaleshi/{kaleshi_slug}/'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [kaleshi_email]  # or any other recipients

    send_mail(subject, message, from_email, recipient_list)

def resolve_kalesh(kalesh_object):
    kaleshi_slug_1 = kalesh_object.kaleshi_slug_1
    kaleshi_slug_2 = kalesh_object.kaleshi_slug_2
    kaleshi_responses = Kaleshi.objects.filter(kaleshi_slug__in=[kaleshi_slug_1, kaleshi_slug_2]).values_list('kaleshi_response', flat=True)

    prompt = construct_prompt(kaleshi_responses)

    print(prompt)
    resolution = send_request_to_openai_and_receive_response(prompt)

    return resolution

def construct_prompt(kaleshi_responses):
    print("constructing prompt")
    header = """You are a couple's therapist of sorts that will now listen to the problem of your client couple from two perspectives. 
            I want you to gauge their tone, intentions, subtext in their words, and whatever else to help them reach a resolution to their conflict by bringing them clarity.
            Your response should also help foster healthy relationship habits, such as communication, teamwork, loyalty, etc. Use Gentle Language.
            Your response will be sent as an email to the two in the couple.
            Make sure you make it personalized, with anecdotes and stay impartial. 
            Make assumptions if you'd like, that's okay too. And don't make it sound like a corporate email please.
            Here are the two perspectives:


        """
    perspectives = ""
    for kaleshi_response in kaleshi_responses:
        perspectives+= f"""
            "{kaleshi_response}"

        """

    return header + perspectives

def send_request_to_openai_and_receive_response(prompt):
    response = client.chat.completions.create(model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful and empathetic couples therapist."},
        {"role": "user", "content": prompt}
    ],
    max_tokens=1000,  # Adjust based on desired response length
    temperature=0.7  # Adjust for creativity
    )

    return response.choices[0].message.content