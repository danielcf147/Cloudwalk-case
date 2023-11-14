from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()


def email_alert(subject, body, to, image_paths=None):
    # Create a multipart message
    msg = MIMEMultipart()
    msg.attach(MIMEText(body, "plain"))
    msg["Subject"] = subject
    msg["To"] = to
    msg["From"] = "danielcf147@gmail.com"

    # Attach images as attachments
    if image_paths:
        for image_path in image_paths:
            with open(image_path, "rb") as image_file:
                image = MIMEImage(image_file.read())
                image.add_header(
                    "Content-Disposition", f"attachment; filename={image_path}"
                )
                msg.attach(image)

    # Send the email
    user = os.getenv("USER")
    password = os.getenv("PASSWORD")  # Replace with your email password

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(user, password)
        server.sendmail(user, to, msg.as_string())


if __name__ == "__main__":
    # Example usage with an image attachment
    email_alert(
        "Test with Image",
        "Here is an image attachment.",
        "recipient@example.com",
        image_paths=["imagePath.png"],
    )
