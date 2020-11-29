from flask import Flask, request
from processing import do_calculation
app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/", methods=["GET", "POST"])
def adder_page():
        errors = ""
        if request.method == "POST":
            number1 = None
            number2 = None
            try:
                number1 = float(request.form["number1"])
            except:
                errors += "<p>Το {!r} δεν είναι αριθμός.</p>\n".format(request.form["number1"])
            try:
                number2 = float(request.form["number2"])
            except:
                errors += "<p>Το {!r} ξέρεις ότι δεν είναι αριθμός!</p>\n".format(request.form["number2"])
            if number1 is not None and number2 is not None:
                result = do_calculation(number1, number2)
                return '''
                    <html>
                        <body>
                            <p>Το άθροισμα είναι: {result}</p>
                            <p><a href="/">Νέος υπολογισμός</a>
                        </body>
                    </html>
                '''.format(result=result)
        return '''
            <html>
                <body>
                    {errors}
                    <p>Καλωσήρθατε στον προσωπικό μου υπολογιστή!</p>
                    <p> </p>
                    <p>&nbsp;</p>
                    <br /><p></p>
                    <p></p><div class="separator" style="clear: both; text-align: left;"><a href=" http://nicktremoulis.pythonanywhere.com/" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" data-original-height="268" data-original-width="545" src="https://1.bp.blogspot.com/-JyhHW3B0o8c/X1zjsGv5cBI/AAAAAAAAL24/OiTNGC5RSLYv2DEp1ZByTM0OSp4lKHEqgCLcBGAsYHQ/s320/syn1.jpg" width="320" /></a></div><br />&nbsp;
                    <p></p>
                    <p>&nbsp;
                    <p>Καταχωρήστε δύο προσθετέους:</p>
                    <form method="post" action=".">
                        <p><input name="number1" /></p>
                        <p><input name="number2" /></p>
                        <p><input type="submit" value="Πρόσθεση" /></p>
                    </form>
                </body>
            </html>
        '''.format(errors=errors)
