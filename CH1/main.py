from datetime import date
from flask import Flask, views


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():

    return "This is an online … counseling system (OPCS)"


@app.route('/home')
def home():

    return ''' 

       <html><head><title>Online Personal … System</title> 

          </head><body> 

           <h1>Online … Counseling System (OPCS)</h1> 

           <p>This is a template of a web-based counseling  

              application where counselors can … … …</em> 

           </body></html> 

       '''


@app.route('/home')
@app.route('/information')
@app.route('/introduction')
def home():

    return '''<html><head> 

             <title>Online Personal … System</title> 

        </head><body> 

           <h1>Online … Counseling System (OPCS)</h1> 

            … … … … … 

        </body></html> 

       '''


def show_honor_dissmisal(counselor: str, effective_date: date, patient: str):

    letter = """ 
       … … … … … 
       </head><body> 
           <h1> Termination of Consultation </h1> 
           <p>From: {} 
           <p>Head, Counselor 
           <p>Date: {} 
           <p>To: {} 
           <p>Subject: Termination of consultation	 
                    <p>Dear {}, 
                    … … … … … … 
                    <p>Yours Sincerely, 
                    <p>{} 
                </body> 
            </html> 
    """.format(counselor, effective_date, patient, patient, counselor)
    return letter, 200


app.add_url_rule('/certificate/terminate/<string:counselor>/<date:effective_date>/<string:patient>',
                 'show_honor_dissmisal', views.certificates.show_honor_dissmisal)


if __name__ == '__main__':
    app.run(debug=True)
    