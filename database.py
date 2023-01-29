import pyrebase
firebaseConfig={"apiKey": "AIzaSyBXwMTRXTGgnwcysfG5zlIhMLoWVV3bdWk",
  "authDomain": "quizit-589ff.firebaseapp.com",
  "databaseURL": "https://quizit-589ff-default-rtdb.asia-southeast1.firebasedatabase.app",
  "projectId": "quizit-589ff",
  "storageBucket": "quizit-589ff.appspot.com",
  "messagingSenderId": "298100903178",
  "appId": "1:298100903178:web:4f7fec8915b58e40587ef3",
  "measurementId": "G-PHP79SGCZG"
}

firebase=pyrebase.initialize_app(firebaseConfig)
db=firebase.database()
# try1=db.child("users").get()
# print(try1.key())
# for i in try1.each():
  # print(i.key())