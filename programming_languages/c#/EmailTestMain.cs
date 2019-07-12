using System.Net;
using System.Net.Mail;


namespace EmailTestApp {

    class EmailTestMain {

        static void Main(string[] args) {
            const string fromName = "";
            const string toName = "";
            const string fromAddr = "";
            const string toAddr = "";
            const string fromPassword = "";
            const string subject = "";
            const string body = "";

            var from = new MailAddress(fromAddr, fromName);
            var to = new MailAddress(toAddr, toName);

            var smtp = new SmtpClient {
                Host = "smtp.gmail.com",
                Port = 587,
                EnableSsl = true,
                DeliveryMethod = SmtpDeliveryMethod.Network,
                UseDefaultCredentials = false,
                Credentials = new NetworkCredential(from.Address, fromPassword)
            };
            using (var message = new MailMessage(from, to) {
                Subject = subject,
                Body = body
            }) {
                smtp.Send(message);
            }
        }
    }
}
