import firebase from "firebase/compat/app"
import { getFirestore, doc } from "firebase/firestore"

const firebaseConfig = {
  apiKey: "AIzaSyBu-_rk8pJRRR6PvyfGyU95fOxhbgwOXKs",
  authDomain: "guanghui-food-website.firebaseapp.com",
  databaseURL: "https://guanghui-food-website-default-rtdb.firebaseio.com",
  projectId: "guanghui-food-website",
  storageBucket: "guanghui-food-website.appspot.com",
  messagingSenderId: "294046337994",
  appId: "1:294046337994:web:1fce3db5d8121d36aa5d33",
  measurementId: "G-3MM6ZN72KF"
}

const firebaseApp = firebase.initializeApp(firebaseConfig)
const db = getFirestore(firebaseApp)
const storeNames = doc(db, "blocks", "storeName")
const timeTable = doc(db, "blocks", "timeTable")
const news = doc(db, "blocks", "news")
const about = doc(db, "blocks", "about")
const merchandise = doc(db, "blocks", "merchandise")
const gallery = doc(db, "blocks", "pictures")
const comment = doc(db, "blocks", "comments")

export { storeNames, timeTable, news, about, merchandise, gallery, comment }
