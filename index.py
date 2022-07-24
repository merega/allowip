from flask import Flask, request, render_template
import subprocess, settings, os


app = Flask(__name__)

allow_file = settings.allow_file

@app.route('/')
def showip():
    file = open(allow_file, 'r')
    data = file.read()
    file.close()
    hstnm = subprocess.check_output("/usr/bin/hostname")
    #return(data.split(";"))
    return render_template('showip.html', data=data.split(";"), hstnm = hstnm.decode("utf-8"))


@app.route('/addip')
def addip_form():
    return render_template('addip.html')


@app.route('/data', methods=['POST'])
def addip():
    if request.method == 'POST':
        ipadr = request.form['address']
        with open(allow_file, 'r') as f:
            old_data = f.read()
        new_data = old_data.replace('deny all;', 'allow {ipadr};\ndeny all;'.format(ipadr = ipadr))
        with open(allow_file, 'w') as f:
            f.write(new_data)
        ngnx = os.system('/usr/sbin/nginx -t')
        if ngnx != 0:
            with open(allow_file, 'w') as f:
                f.write(old_data)
        os.system('/usr/bin/systemctl restart nginx')
        
        return render_template('added.html', ipadr=ipadr)


if __name__ == '__main__':
    app.run(debug=True)
