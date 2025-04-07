![example workflow](https://github.com/Kevin051596/guanghui-food-website/actions/workflows/main.yml/badge.svg)

### 快速啟動

到 `package.json` 目錄，使用以下指令，即可快速看見在開發環境的網頁，預設 port 8090
```
npm install --legacy-peer-deps
npm run serve
```

### 注意事項
由於目前版本仍使用 vue-cli 打包，所以會有套件相依性問題，如下
```
Conflicting peer dependency: swiper@8.4.7
npm error node_modules/swiper
npm error   peer swiper@"^7.0.0  || ^8.0.0" from vue-awesome-swiper@5.0.0
npm error   node_modules/vue-awesome-swiper
npm error     vue-awesome-swiper@"^5.0.0" from the root project
```
因此目前將 swiper 套件使用 6.8.4，vue-awesome-swiper 套件使用 5.0.0 解決目前問題。但此方法較不妥善，所以之後得將整份專案改以 vite 打包，並使用 swiper/vue(適用於 vue3） 的輪播工具解決此問題，而目前整份網頁專案採用 vue3 方式，雖然運行起來沒問題，但還是得換掉打包工具實驗能否解決套件衝突

### ToDo
- [ ] 更換打包工具（vite）
- [ ] 配置 dockerfile 給網頁主體
- [ ] 測試爬蟲排程
- [ ] 測試更新 image CICD

### 相關技術介紹
<div>
<img src="https://github.com/devicons/devicon/blob/master/icons/vuejs/vuejs-original.svg" width="40" height="40"/>
<img src="https://github.com/devicons/devicon/blob/master/icons/firebase/firebase-original.svg" title="Firebase" alt="Firebase" width="40" height="40"/>
<img src="https://github.com/devicons/devicon/blob/master/icons/python/python-original.svg" title="Python" **alt="Python" width="40" height="40"/>
<img src="https://github.com/devicons/devicon/blob/master/icons/selenium/selenium-original.svg" width="40" height="40"/>
<img src="https://github.com/devicons/devicon/blob/master/icons/docker/docker-original.svg" width="40" height="40"/>
<img src="https://i2.wp.com/www.primefaces.org/wp-content/uploads/2019/12/primevue-logo.png?fit=300%2C300&ssl=1" width="40" height="40"/>
</div>
本網站使用 vue3 語法，並結合 firebase store、storage，並使用 firbase host 部屬，另外設計爬蟲程式定時抓取 FB 上的最新資訊更新到網頁上，而這部分有使用 Docker 管理，所以可以隨地部屬，不與網站主體相依。樣式部分使用 PrimeVue 元件和 flaticon。
