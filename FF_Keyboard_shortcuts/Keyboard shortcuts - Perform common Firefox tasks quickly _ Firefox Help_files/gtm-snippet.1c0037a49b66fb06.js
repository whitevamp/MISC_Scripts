"use strict";(self.webpackChunkkitsune=self.webpackChunkkitsune||[]).push([[299],{6863:()=>{void 0===window.Mozilla&&(window.Mozilla={}),Mozilla.dntEnabled=function(t,a){var e=t||navigator.doNotTrack||window.doNotTrack||navigator.msDoNotTrack,o=a||navigator.userAgent,n=o.match(/Firefox\/(\d+)/),g=/MSIE|Trident/i.test(o),i=o.match(/Windows.+?(?=;)/g);return(!g||"function"==typeof Array.prototype.indexOf)&&"Enabled"===(n&&parseInt(n[1],10)<32||g&&i&&-1!==["Windows NT 6.1","Windows NT 6.2","Windows NT 6.3"].indexOf(i.toString())?"Unspecified":{0:"Disabled",1:"Enabled"}[e]||"Unspecified")};const t=Mozilla.dntEnabled;!function(a){var e=document.getElementsByTagName("html")[0],o=e.getAttribute("data-gtm-container-id");if(a.gaConsoleLogging=!1,a.dataLayer=a.dataLayer||[],a.gtag=function(){a.dataLayer.push(arguments)},"function"==typeof t&&!t()&&o){!function(t,a,e,o,n,g,i,s,d){for(t[o]=t[o]||[],t[o].push({"gtm.start":(new Date).getTime(),event:"gtm.js"}),i=a.getElementsByTagName(e)[0],d=n.length,"//www.googletagmanager.com/gtag/js?id=@&l=dataLayer";d--;)(g=a.createElement(e)).async=!0,g.src="//www.googletagmanager.com/gtag/js?id=@&l=dataLayer".replace("@",n[d]),i.parentNode.insertBefore(g,i)}(window,document,"script","dataLayer",[o]),a.gtag("js",new Date);var n={};e.getAttribute("lang")&&(n.locale=e.getAttribute("lang")),e.dataset.gaTopics&&(n.topics=e.dataset.gaTopics),e.dataset.gaProducts&&(n.products=e.dataset.gaProducts),e.dataset.gaContentGroup&&(n.content_group=e.dataset.gaContentGroup),e.dataset.gaDefaultSlug&&(n.default_slug=e.dataset.gaDefaultSlug),e.dataset.gaArticleLocale&&(n.article_locale=e.dataset.gaArticleLocale),e.dataset.gaDebugMode&&(n.debug_mode=!0),e.dataset.gaConsoleLogging&&(a.gaConsoleLogging=!0,console.log("------------------------------"),console.log("config for ".concat(o,":")),console.log("parameters: ".concat(JSON.stringify(n,null,2))),console.log("------------------------------")),a.gtag("config",o,n)}}(window)}},t=>{t.O(0,[620],(()=>t(t.s=6863))),t.O()}]);