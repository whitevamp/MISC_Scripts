"use strict";(self.webpackChunkkitsune=self.webpackChunkkitsune||[]).push([[467],{6848:(e,t,r)=>{r.d(t,{Ay:()=>z});var n=r(2284),i=r(3662),a=r(9417),o=r(5501),s=r(9640),u=r(467),c=r(4765),h=r(296),l=r(3029),f=r(2901),v=r(4467),p=r(4756),d=r.n(p),A=r(2628);function w(){w=function(e,t){return new r(e,void 0,t)};var e=RegExp.prototype,t=new WeakMap;function r(e,n,a){var o=new RegExp(e,n);return t.set(o,a||t.get(e)),(0,i.A)(o,r.prototype)}function a(e,r){var n=t.get(r);return Object.keys(n).reduce((function(t,r){var i=n[r];if("number"==typeof i)t[r]=e[i];else{for(var a=0;void 0===e[i[a]]&&a+1<i.length;)a++;t[r]=e[i[a]]}return t}),Object.create(null))}return(0,o.A)(r,RegExp),r.prototype.exec=function(t){var r=e.exec.call(this,t);if(r){r.groups=a(r,this);var n=r.indices;n&&(n.groups=a(n,this))}return r},r.prototype[Symbol.replace]=function(r,i){if("string"==typeof i){var o=t.get(this);return e[Symbol.replace].call(this,r,i.replace(/\$<([^>]+)>/g,(function(e,t){var r=o[t];return"$"+(Array.isArray(r)?r.join("$"):r)})))}if("function"==typeof i){var s=this;return e[Symbol.replace].call(this,r,(function(){var e=arguments;return"object"!=(0,n.A)(e[e.length-1])&&(e=[].slice.call(e)).push(a(e,s)),i.apply(this,e)}))}return e[Symbol.replace].call(this,r,i)},w.apply(this,arguments)}var m=function(){function e(){var t=arguments.length>0&&void 0!==arguments[0]?arguments[0]:"";(0,l.A)(this,e),(0,v.A)(this,"major",void 0),(0,v.A)(this,"minor",void 0),(0,v.A)(this,"patch",void 0),(0,v.A)(this,"label",void 0);var r=t.match(/([\d\.]*)([ab]\d*)?/i),n=(0,h.A)(r,3);t=n[1],this.label=n[2];var i=t.split(".").map((function(e){return parseInt(e,10)})),a=(0,h.A)(i,3);this.major=a[0],this.minor=a[1],this.patch=a[2]}return(0,f.A)(e,[{key:"toString",value:function(t){var r,n="",i=(0,c.A)(e.order);try{for(i.s();!(r=i.n()).done;){var a=r.value,o=this[a];if("label"===a)o&&(n+=o);else if(t&&isNaN(o))n+=".0";else{if(isNaN(o))break;n+="."+o.toString()}if(t===a)break}}catch(e){i.e(e)}finally{i.f()}return n.slice(1)}}]),e}();(0,v.A)(m,"order",["major","minor","patch","label"]);var b=(0,f.A)((function e(){(0,l.A)(this,e),(0,v.A)(this,"mozilla",!1),(0,v.A)(this,"brands",void 0),(0,v.A)(this,"version",void 0)})),g=function(){function e(){(0,l.A)(this,e),(0,v.A)(this,"name",void 0),(0,v.A)(this,"version",void 0)}return(0,f.A)(e,[{key:"mobile",get:function(){return["Android","iOS"].includes(this.name)}},{key:"toString",value:function(){var e=this.name;return this.version&&(e+=" "+this.version),e}}]),e}();(0,v.A)(g,"versionNormalization",{Windows:{"nt 5.1":"XP","nt 5.2":"XP","nt 6.0":"Vista","nt 6.1":"7","nt 6.2":"8","nt 6.3":"8.1","nt 6.4":"10","nt 10.0":"10"}});var x=function(){function e(){(0,l.A)(this,e)}var t,r;return(0,f.A)(e,[{key:"browser",value:(r=(0,u.A)(d().mark((function e(){var t,r=arguments;return d().wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return t=r.length>0&&void 0!==r[0]?r[0]:new b,e.abrupt("return",t);case 2:case"end":return e.stop()}}),e)}))),function(){return r.apply(this,arguments)})},{key:"os",value:(t=(0,u.A)(d().mark((function e(){var t,r=arguments;return d().wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return t=r.length>0&&void 0!==r[0]?r[0]:new g,e.abrupt("return",t);case 2:case"end":return e.stop()}}),e)}))),function(){return t.apply(this,arguments)})}]),e}(),k=function(e){(0,o.A)(i,e);var t,r,n=(0,s.A)(i);function i(){var e,t=arguments.length>0&&void 0!==arguments[0]?arguments[0]:navigator.userAgent;return(0,l.A)(this,i),e=n.call(this),(0,v.A)((0,a.A)(e),"uaString",void 0),e.uaString=t,e}return(0,f.A)(i,[{key:"browser",value:(r=(0,u.A)(d().mark((function e(){var t,r,n,a,o,s,u,c=arguments;return d().wrap((function(e){for(;;)switch(e.prev=e.next){case 0:if(t=c.length>0&&void 0!==c[0]?c[0]:new b,!(r=this.uaString.match(i.mozillaRegex))){e.next=13;break}return t.mozilla=!0,a=r.groups,o=a.name,s=a.version,o=o.toLowerCase(),u=null!==(n=i.brandNormalization[o])&&void 0!==n?n:[],e.next=9,this.os();case 9:e.sent.mobile||(u=u.filter((function(e){return"Firefox Focus"!==e}))),t.brands=u,t.version=new m(s);case 13:return e.abrupt("return",t);case 14:case"end":return e.stop()}}),e,this)}))),function(){return r.apply(this,arguments)})},{key:"os",value:(t=(0,u.A)(d().mark((function e(){var t,r,n,a,o,s,u,l,f,v,p,A,w=arguments;return d().wrap((function(e){for(;;)switch(e.prev=e.next){case 0:t=w.length>0&&void 0!==w[0]?w[0]:new g,r=(0,c.A)(i.osRegexps),e.prev=2,r.s();case 4:if((n=r.n()).done){e.next=15;break}if(a=(0,h.A)(n.value,2),o=a[0],s=a[1],!(u=this.uaString.match(s))){e.next=13;break}return A=null==u||null===(l=u.groups)||void 0===l?void 0:l.version.toLowerCase(),A=null!==(f=null===(v=g.versionNormalization)||void 0===v||null===(p=v[o])||void 0===p?void 0:p[A])&&void 0!==f?f:A,t.name=o,t.version=A,e.abrupt("return",t);case 13:e.next=4;break;case 15:e.next=20;break;case 17:e.prev=17,e.t0=e.catch(2),r.e(e.t0);case 20:return e.prev=20,r.f(),e.finish(20);case 23:case"end":return e.stop()}}),e,this,[[2,17,20,23]])}))),function(){return t.apply(this,arguments)})}]),i}(x);(0,v.A)(k,"mozillaRegex",w(/(Firefox|FxiOS|Fennec|Focus|Klar|Thunderbird)\/([0-9\._]+)?/i,{name:1,version:2})),(0,v.A)(k,"brandNormalization",{firefox:["Firefox","Firefox Focus"],fxios:["Firefox","Firefox Focus"],fennec:["Firefox"],focus:["Firefox Focus"],klar:["Firefox Focus"],thunderbird:["Thunderbird"]}),(0,v.A)(k,"osRegexps",[["Windows",w(/Windows ?((?:NT )?[0-9a-z\._]+)?/i,{version:1})],["iOS",/(iPhone)|(iPad)|(iPod)/i],["Mac OS",w(/Mac OS ?(X [0-9\._]+)?/i,{version:1})],["Android",/Android/i],["Linux",/Linux|X11|BSD|GNU/i]]);var y=function(){function e(t){for(var r in(0,l.A)(this,e),t)this[r]=t[r]}var t;return(0,f.A)(e,[{key:"getHighEntropyValues",value:(t=(0,u.A)(d().mark((function e(t){return d().wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.abrupt("return",this);case 1:case"end":return e.stop()}}),e,this)}))),function(e){return t.apply(this,arguments)})}]),e}(),D=function(e){(0,o.A)(n,e);var t,r=(0,s.A)(n);function n(e){var t;return(0,l.A)(this,n),t=r.call(this),(0,v.A)((0,a.A)(t),"uaData",navigator.userAgentData),e&&(t.uaData=new y(e)),t}return(0,f.A)(n,[{key:"os",value:(t=(0,u.A)(d().mark((function e(){var t,r,n,i,a,o=arguments;return d().wrap((function(e){for(;;)switch(e.prev=e.next){case 0:if(r=o.length>0&&void 0!==o[0]?o[0]:new g,null!==(t=this.uaData)&&void 0!==t&&t.platform){e.next=3;break}return e.abrupt("return",r);case 3:return r.name=this.uaData.platform,e.prev=4,e.next=7,this.uaData.getHighEntropyValues(["platformVersion"]);case 7:i=e.sent,n=i.platformVersion,e.next=14;break;case 11:return e.prev=11,e.t0=e.catch(4),e.abrupt("return",r);case 14:return"Windows"===this.uaData.platform&&((a=new m(n).major)>=13?r.version="11":a>=1&&(r.version="10")),e.abrupt("return",r);case 16:case"end":return e.stop()}}),e,this,[[4,11]])}))),function(){return t.apply(this,arguments)})}]),n}(x),S=function(){function e(t){(0,l.A)(this,e),this.data=t}var t;return(0,f.A)(e,[{key:"getData",value:(t=(0,u.A)(d().mark((function e(){return d().wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.abrupt("return",this.data);case 1:case"end":return e.stop()}}),e,this)}))),function(){return t.apply(this,arguments)})}]),e}(),F=function(e){(0,o.A)(i,e);var t,r,n=(0,s.A)(i);function i(e){var t;return(0,l.A)(this,i),t=n.call(this),(0,v.A)((0,a.A)(t),"remote",new A.A),e&&(t.remote=new S(e)),t}return(0,f.A)(i,[{key:"browser",value:(r=(0,u.A)(d().mark((function e(){var t,r,n,i,a,o,s=arguments;return d().wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return t=s.length>0&&void 0!==s[0]?s[0]:new b,e.next=3,this.remote.getData();case 3:return r=e.sent,n=r.application,a=(i=void 0===n?{}:n).name,o=i.version,a&&o&&(t.mozilla=!0,t.brands=[a],t.version=new m(o)),e.abrupt("return",t);case 10:case"end":return e.stop()}}),e,this)}))),function(){return r.apply(this,arguments)})},{key:"os",value:(t=(0,u.A)(d().mark((function e(){var t,r,n,a,o=arguments;return d().wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return t=o.length>0&&void 0!==o[0]?o[0]:new g,e.next=3,this.remote.getData();case 3:return r=e.sent,n=r.application,a=(void 0===n?{}:n).osVersion,i.windows11Regex.test(a)&&(t.name="Windows",t.version="11"),e.abrupt("return",t);case 10:case"end":return e.stop()}}),e,this)}))),function(){return t.apply(this,arguments)})}]),i}(x);(0,v.A)(F,"windows11Regex",/^Windows_NT 10\.0 2[0-9]{4}$/i);var z=function(){function e(t,r,n){(0,l.A)(this,e),this.uaDetector=new k(t),this.uaDataDetector=new D(r),this.troubleshootingDetector=new F(n)}var t,r;return(0,f.A)(e,[{key:"getBrowser",value:(r=(0,u.A)(d().mark((function e(){var t,r;return d().wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,this.uaDetector.browser();case 2:return t=e.sent,e.next=5,this.uaDetector.os();case 5:if(r=e.sent,!t.mozilla||r.mobile){e.next=10;break}return e.next=9,this.troubleshootingDetector.browser(t);case 9:t=e.sent;case 10:return e.abrupt("return",t);case 11:case"end":return e.stop()}}),e,this)}))),function(){return r.apply(this,arguments)})},{key:"getOS",value:(t=(0,u.A)(d().mark((function e(){var t;return d().wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,this.uaDetector.os();case 2:if("Windows"!==(t=e.sent).name||"10"!==t.version){e.next=16;break}return e.next=6,this.uaDetector.browser();case 6:if(!e.sent.mozilla||t.mobile){e.next=13;break}return e.next=10,this.troubleshootingDetector.os(t);case 10:t=e.sent,e.next=16;break;case 13:return e.next=15,this.uaDataDetector.os(t);case 15:t=e.sent;case 16:return e.abrupt("return",t);case 17:case"end":return e.stop()}}),e,this)}))),function(){return t.apply(this,arguments)})}]),e}()},2628:(e,t,r)=>{r.d(t,{A:()=>u});var n=r(467),i=r(3029),a=r(2901),o=r(4756),s=r.n(o),u=function(){function e(){(0,i.A)(this,e)}var t;return(0,a.A)(e,[{key:"getData",value:(t=(0,n.A)(s().mark((function e(){var t,r,n,i,a=arguments;return s().wrap((function(e){for(;;)switch(e.prev=e.next){case 0:if(t=a.length>0&&void 0!==a[0]?a[0]:1e3,!this.data){e.next=3;break}return e.abrupt("return",this.data);case 3:return r=new Promise((function(e,t){window.addEventListener("WebChannelMessageToContent",(function(r){if("remote-troubleshooting"===r.detail.id){var n=r.detail.message;if(n)return e(n)}t()}))})),n=new Promise((function(e,r){window.setTimeout((function(){return r()}),t)})),i=new window.CustomEvent("WebChannelMessageToChrome",{detail:JSON.stringify({id:"remote-troubleshooting",message:{command:"request"}})}),window.dispatchEvent(i),e.prev=7,e.next=10,Promise.race([r,n]);case 10:this.data=e.sent,e.next=16;break;case 13:e.prev=13,e.t0=e.catch(7),this.data={};case 16:return e.abrupt("return",this.data);case 17:case"end":return e.stop()}}),e,this,[[7,13]])}))),function(){return t.apply(this,arguments)})}]),e}()}}]);