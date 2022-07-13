網站位址: https://kevin051596.github.io/guanghui-food-website/  

<img src="https://github.com/Kevin051596/guanghui-food-website/blob/main/%E5%85%89%E6%85%A7%E6%B0%B4%E7%85%8E%E5%8C%85(%E6%A2%A7%E6%A3%B2%E5%BA%97).png?raw=true" width="50%" height="50%"/>

問題：
    1. contact, commit 刷新跑位
    2. hash 的 URL 問題 -> 使用 id 參數替代 hash 值
    3. 刷新頁面導致 name 抓取問題 -> name 會被 id 參數覆蓋，而 path 則會忽略 id 參數，導致使用 path 時傳遞 to.params.id 參數為空 
    4. mobile version 的 icon 顯示問題