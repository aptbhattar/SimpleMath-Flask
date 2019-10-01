from flask import Blueprint

router = Blueprint("router", __name__)

@router.route("/check")
def check():
    return "Congratulations! Your app works. :)"

@router.route("/add", methods=["POST"])
def add():
    # Add logic here
    return

@app.route('/', methods=['GET', 'POST'])
def home():
    calc = power()

    if request.method == 'POST': 
        for i in range(b):
            a=a*a
            i=i+1
            print(a)

    elif request.method == 'GET':
        return render_template('home.html', form=form)
