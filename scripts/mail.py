FROM = "kmages@hrimembers.cash"
SENDGRID_API_KEY = (
    "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"
)

import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import ssl

if not os.environ.get("PYTHONHTTPSVERIFY", "") and getattr(
    ssl, "_create_unverified_context", None
):
    ssl._create_default_https_context = ssl._create_unverified_context

# import pdb

# pdb.set_trace()
message = Mail(
    from_email=FROM,
    to_emails="prakhar.jain@crowdbotics.com",
    subject="Sending TEST EMAIL",
    html_content="<strong>TEST EMAIL </strong>",
)
try:
    # import pdb

    # pdb.set_trace()
    # sg = SendGridAPIClient(os.environ.get("SENDGRID_API_KEY"))
    sg = SendGridAPIClient(
        # "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",
        "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"
        # verify=False,
    )
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e)
