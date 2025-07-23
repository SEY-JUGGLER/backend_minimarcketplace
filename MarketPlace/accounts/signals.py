# signals.py (optionnel - pour personnaliser l'email)
from django.dispatch import receiver
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail
from django.conf import settings


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    """
    Signal personnalisé pour envoyer l'email de réinitialisation
    """
    email_plaintext_message = f"""
    Bonjour {reset_password_token.user.first_name},

    Quelqu'un a demandé la réinitialisation du mot de passe pour le compte associé à {reset_password_token.user.email}.

    Votre token de réinitialisation : {reset_password_token.key}

    Si vous n'avez pas fait cette demande, ignorez cet email.

    Cordialement,
    L'équipe
    """

    send_mail(
        # subject:
        "Réinitialisation de votre mot de passe",
        # message:
        email_plaintext_message,
        # from:
        settings.EMAIL_HOST_USER,
        # to:
        [reset_password_token.user.email]
    )