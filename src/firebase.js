import firebase from "firebase/compat/app"
import { getFirestore, doc } from "firebase/firestore"

const firebaseConfig = {
  apiKey: process.env.FIREBASE_API_KEY,
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
const timeTableBlock = doc(db, "blocks", "timeTable")
const newsBlock = doc(db, "blocks", "news")
const aboutBlock = doc(db, "blocks", "about")
const merchandiseBlock = doc(db, "blocks", "merchandise")
const galleryBlock = doc(db, "blocks", "pictures")
const commentBlock = doc(db, "blocks", "comments")

export { storeNames, timeTableBlock, newsBlock, aboutBlock, merchandiseBlock, galleryBlock, commentBlock }
