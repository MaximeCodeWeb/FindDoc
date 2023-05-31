#######################################################
#################  Find Documentation  ################             D:\Code WEB\Python\FindDoc\test.txt
#######################################################

#Color Console
class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR


#imports
import os.path
import os


# effacement de l'ecran
os.system('cls')
print("\n")


#Code
print(bcolors.OK + "[FD] " + bcolors.RESET + "Coller le path de votre fichier HTML :")
pathFile = str(input(bcolors.OK + "[FD] " + bcolors.RESET + ">> "))



balises = {
    "h1" : "<h1> : https://developer.mozilla.org/en-US/docs/Web/HTML/Element/Heading_Elements \n",
    "doctype": "<DOCTYPE> : https://developer.mozilla.org/en-US/docs/Glossary/Doctype \n",
    "a" : "<a> : https://developer.mozilla.org/fr/docs/Web/HTML/Element/a \n",
    "abbr" : "<abbr> : https://developer.mozilla.org/fr/docs/Web/HTML/Element/abbr \n",
    "acronym" : "<acronym> : https://developer.mozilla.org/fr/docs/Web/HTML/Element/acronym \n",
    "address" : "<address> :  https://developer.mozilla.org/fr/docs/Web/HTML/Element/address \n",
    "area" : "<area> : https://developer.mozilla.org/fr/docs/Web/HTML/Element/area \n",
    "article" : "<article> : https://developer.mozilla.org/fr/docs/Web/HTML/Element/article \n",
    "aside" : "<aside> : https://developer.mozilla.org/fr/docs/Web/HTML/Element/aside \n",
    "audio" : "<audio> : https://developer.mozilla.org/fr/docs/Web/HTML/Element/audio \n",
    "b" : "<b> : https://developer.mozilla.org/fr/docs/Web/HTML/Element/b \n",
    "base" : "<base> : https://developer.mozilla.org/fr/docs/Web/HTML/Element/base \n",
    "bdi" :  "https://developer.mozilla.org/fr/docs/Web/HTML/Element/bdi \n",
    "bdo" : "<bdo> : https://developer.mozilla.org/fr/docs/Web/HTML/Element/bdo \n",
    "blockquote" : "<blockquote> : https://developer.mozilla.org/fr/docs/Web/HTML/Element/blockquote \n",
    "body" : "<body> : https://developer.mozilla.org/fr/docs/Web/HTML/Element/body \n",
    "br" : "<br> : https://developer.mozilla.org/fr/docs/Web/HTML/Element/br \n",
    "button" : "<button> : https://developer.mozilla.org/fr/docs/Web/HTML/Element/button \n",
    "canvas" : "<canvas> : https://developer.mozilla.org/fr/docs/Web/HTML/Element/canvas \n",
    "caption" : "<caption>: https://developer.mozilla.org/fr/docs/Web/HTML/Element/caption \n",
    "cite" : "<cite> : https://developer.mozilla.org/fr/docs/Web/HTML/Element/cite \n",
    "code" : "<code> : https://developer.mozilla.org/fr/docs/Web/HTML/Element/code \n",
    "col" : "<col> : https://developer.mozilla.org/fr/docs/Web/HTML/Element/col \n",
    "colgroup" : "<colgroup> : https://developer.mozilla.org/fr/docs/Web/HTML/Element/colgroup \n",
    "data" : "<data> : https://developer.mozilla.org/fr/docs/Web/HTML/Element/data \n",
    "datalist" : "<datalist> : https://developer.mozilla.org/fr/docs/Web/HTML/Element/datalist \n",
    "dd" : "<dd> : https://developer.mozilla.org/fr/docs/Web/HTML/Element/dd \n",
    "el1" : "<del> : https://developer.mozilla.org/fr/docs/Web/HTML/Element/del \n",
    "details" : "<details> https://developer.mozilla.org/fr/docs/Web/HTML/Element/details \n",
    "dfn" : "<dfn> : https://developer.mozilla.org/fr/docs/Web/HTML/Element/dfn \n",
    "dialog" : "<dialog> : https://developer.mozilla.org/fr/docs/Web/HTML/Element/dialog \n",
    "div" : "<div> : https://developer.mozilla.org/fr/docs/Web/HTML/Element/div \n",
    "dl" : "<dl> : https://developer.mozilla.org/fr/docs/Web/HTML/Element/dl \n",
    "dt" : "<dt> : https://developer.mozilla.org/fr/docs/Web/HTML/Element/dt \n",
    "em" : "<em> : https://developer.mozilla.org/fr/docs/Web/HTML/Element/em \n",
    "embed": "<embed> : https://developer.mozilla.org/fr/docs/Web/HTML/Element/embed \n",
    "fieldset" : "<fieldset> : https://developer.mozilla.org/fr/docs/Web/HTML/Element/fieldset \n",
    "figcaption" : "<figcaption> : https://developer.mozilla.org/fr/docs/Web/HTML/Element/figcaption \n",
    "figure":"<figure> : https://developer.mozilla.org/fr/docs/Web/HTML/Element/figure \n",
    "footer":"<footer> : https://developer.mozilla.org/fr/docs/Web/HTML/Element/footer \n",
    "form" : "<form> : https://developer.mozilla.org/fr/docs/Web/HTML/Element/form \n",
    "head":"<head> : https://developer.mozilla.org/fr/docs/Web/HTML/Element/head \n",
    "header":"<header> : https://developer.mozilla.org/fr/docs/Web/HTML/Element/header \n",
    "hgroup" :"<hgroup> : https://developer.mozilla.org/fr/docs/Web/HTML/Element/hgroup \n",
    "hr" :"<hr> : https://developer.mozilla.org/fr/docs/Web/HTML/Element/hr \n",
    "html" : "<html> : https://developer.mozilla.org/fr/docs/Web/HTML/Element/html \n",
    "i":"<i> : https://developer.mozilla.org/fr/docs/Web/HTML/Element/i \n",
    "iframe":"<iframe> : https://developer.mozilla.org/fr/docs/Web/HTML/Element/iframe \n",
    "img":"<img>  : https://developer.mozilla.org/fr/docs/Web/HTML/Element/img \n",
    "input" : "<input> : https://developer.mozilla.org/fr/docs/Web/HTML/Element/input \n",
    "ins" : "<ins> : https://developer.mozilla.org/fr/docs/Web/HTML/Element/ins \n",
    "kbd":"<kbd> : https://developer.mozilla.org/fr/docs/Web/HTML/Element/kbd \n",
    "label":"<label> : https://developer.mozilla.org/fr/docs/Web/HTML/Element/label \n",
    "legend":"<legend> : https://developer.mozilla.org/fr/docs/Web/HTML/Element/legend \n",
    "li":"<li> : https://developer.mozilla.org/fr/docs/Web/HTML/Element/li \n",
    "link":"<link> : https://developer.mozilla.org/fr/docs/Web/HTML/Element/link \n",
    "main":"<main> : https://developer.mozilla.org/fr/docs/Web/HTML/Element/main \n",
    "map":"<map> : https://developer.mozilla.org/fr/docs/Web/HTML/Element/map \n",
    "mark":"<mark> : https://developer.mozilla.org/fr/docs/Web/HTML/Element/mark \n",
    "menu":"<menu> : https://developer.mozilla.org/fr/docs/Web/HTML/Element/menu \n",
    "meta":"<meta> : https://developer.mozilla.org/fr/docs/Web/HTML/Element/meta \n",
    "meter":"<meter> : https://developer.mozilla.org/fr/docs/Web/HTML/Element/meter \n",
    "nav":"<nav> : https://developer.mozilla.org/fr/docs/Web/HTML/Element/nav \n",
    "noscript":"<noscript : https://developer.mozilla.org/fr/docs/Web/HTML/Element/noscript \n",
    "object1":"<object> : https://developer.mozilla.org/fr/docs/Web/HTML/Element/object \n",
    "ol":"<ol> : https://developer.mozilla.org/fr/docs/Web/HTML/Element/ol \n",
    "optgroup":"<optgroup : https://developer.mozilla.org/fr/docs/Web/HTML/Element/optgroup \n",
    "option":"<option> : https://developer.mozilla.org/fr/docs/Web/HTML/Element/option \n",
    "output":"<output> : https://developer.mozilla.org/fr/docs/Web/HTML/Element/output \n",
    "p":"<p> : https://developer.mozilla.org/fr/docs/Web/HTML/Element/p \n",
    "picture":"<picture> : https://developer.mozilla.org/fr/docs/Web/HTML/Element/picture \n",
    "portal":"<portal> : https://developer.mozilla.org/fr/docs/Web/HTML/Element/portal \n",
    "pre":"<pre> : https://developer.mozilla.org/fr/docs/Web/HTML/Element/pre \n",
    "progress":"<progress : https://developer.mozilla.org/fr/docs/Web/HTML/Element/progress \n",
    "q":"<q> : https://developer.mozilla.org/fr/docs/Web/HTML/Element/q \n",
    "rp":"<rp> : https://developer.mozilla.org/fr/docs/Web/HTML/Element/rp \n",
    "rt":"<rt> : https://developer.mozilla.org/fr/docs/Web/HTML/Element/rt \n",
    "ruby":"<ruby> : https://developer.mozilla.org/fr/docs/Web/HTML/Element/ruby \n",
    "s":"<s> : https://developer.mozilla.org/fr/docs/Web/HTML/Element/s \n",
    "samp":"<samp> : https://developer.mozilla.org/fr/docs/Web/HTML/Element/samp \n",
    "script":"<script> : https://developer.mozilla.org/fr/docs/Web/HTML/Element/script \n",
    "section":"<section> : https://developer.mozilla.org/fr/docs/Web/HTML/Element/section \n",
    "select":"<select> : https://developer.mozilla.org/fr/docs/Web/HTML/Element/select \n",
    "slot":"<slot> : https://developer.mozilla.org/fr/docs/Web/HTML/Element/slot \n",
    "small":"<small> : https://developer.mozilla.org/fr/docs/Web/HTML/Element/small \n",
    "source":"<source> : https://developer.mozilla.org/fr/docs/Web/HTML/Element/source \n",
    "span":"<span> : https://developer.mozilla.org/fr/docs/Web/HTML/Element/span \n",
    "strong":"<strong> : https://developer.mozilla.org/fr/docs/Web/HTML/Element/strong \n",
    "style":"<style> : https://developer.mozilla.org/fr/docs/Web/HTML/Element/style \n",
    "sub":"<sub> : https://developer.mozilla.org/fr/docs/Web/HTML/Element/sub \n",
    "summary":"<summary> : https://developer.mozilla.org/fr/docs/Web/HTML/Element/summary \n",
    "sup":"<sup> : https://developer.mozilla.org/fr/docs/Web/HTML/Element/sup \n",
    "table":"<table> : https://developer.mozilla.org/fr/docs/Web/HTML/Element/table \n",
    "tbody":"<tbody> : https://developer.mozilla.org/fr/docs/Web/HTML/Element/tbody \n",
    "td":"<td> : https://developer.mozilla.org/fr/docs/Web/HTML/Element/td \n",
    "template":"<template : https://developer.mozilla.org/fr/docs/Web/HTML/Element/template \n",
    "textarea":"<textarea : https://developer.mozilla.org/fr/docs/Web/HTML/Element/textarea \n",
    "tfoot":"<tfoot> : https://developer.mozilla.org/fr/docs/Web/HTML/Element/tfoot \n",
    "th":"<th> : https://developer.mozilla.org/fr/docs/Web/HTML/Element/th \n",
    "thead":"<thead> : https://developer.mozilla.org/fr/docs/Web/HTML/Element/thead \n",
    "time":"<time> : https://developer.mozilla.org/fr/docs/Web/HTML/Element/time \n",
    "title":"<title> : https://developer.mozilla.org/fr/docs/Web/HTML/Element/title \n",
    "tr":"<tr> : https://developer.mozilla.org/fr/docs/Web/HTML/Element/tr \n",
    "track":"<track> : https://developer.mozilla.org/fr/docs/Web/HTML/Element/track \n",
    "u":"<u> : https://developer.mozilla.org/fr/docs/Web/HTML/Element/u \n",
    "ul":"<ul> : https://developer.mozilla.org/fr/docs/Web/HTML/Element/ul \n",
    "var":"<var> : https://developer.mozilla.org/fr/docs/Web/HTML/Element/var \n",
    "video":"<video> : https://developer.mozilla.org/fr/docs/Web/HTML/Element/video \n",
    "wbr":"<wbr> : https://developer.mozilla.org/fr/docs/Web/HTML/Element/wbr \n",

}

test = os.path.isfile(pathFile)
if test :
    print(bcolors.OK + "[FD] " + bcolors.RESET + "Création du fichiers en cours...")

    with open(pathFile, 'r') as fichier:
        contenu = str(fichier.read())

        
        


        with open("documentation.txt", "w") as file:
            file.write("-----------------------------------------------\n")
            file.write("---------------Documentation-------------------\n")
            file.write("-----------------------------------------------\n\n\n")
            #print(contenu)
            #Variables
            h1 = "</h1>" in contenu
            a = "</a>" in contenu
            abbr = "</abbr>" in contenu
            acronym = "</acronym>" in contenu
            address = "</address>" in contenu
            area = "<area " in contenu
            article = "</article>" in contenu
            aside = "</aside>" in contenu
            audio = "</audio>" in contenu
            b = "</b>" in contenu
            base = "<base " in contenu
            bdi = "</bdi>" in contenu
            bdo = "</bdo>" in contenu
            blockquote = "</blockquote>" in contenu
            body = "</body>" in contenu
            br = "<br>" in contenu
            button = "</button>" in contenu
            canvas = "</canvas>" in contenu
            caption = "</caption>" in contenu
            cite = "</cite>" in contenu
            code = "</code>" in contenu
            col = "<col " in contenu
            colgroup = "</colgroup>" in contenu
            data = "</data>" in contenu
            datalist = "</datalist>" in contenu
            dd = "</dd>" in contenu
            del1 = "</del>" in contenu
            details = "</details>" in contenu
            dfn = "</dfn>" in contenu
            dialog = "</dialog>" in contenu
            div = "</div>" in contenu
            dl = "</dl>" in contenu
            dt = "</dt>" in contenu
            em = "</em>" in contenu
            embed = "<embed " in contenu
            fieldset = "</fieldset>" in contenu
            figcaption = "</figcaption>" in contenu
            figure = "</figure>" in contenu
            footer = "</footer>" in contenu
            form = "</form>" in contenu
            head = "</head>" in contenu
            header = "</header>" in contenu
            hgroup = "</hgroup>" in contenu
            hr ="<hr " in contenu
            html = "</html>" in contenu
            i = "</i>" in contenu
            iframe = "</iframe>" in contenu
            img = "<img " in contenu
            input = "<input " in contenu
            ins = "<ins " in contenu
            kbd = "</kbd>" in contenu
            label = "</label>" in contenu
            legend = "</legend>" in contenu
            li = "</li>" in contenu
            link = "<link " in contenu
            main = "</main>" in contenu
            map = "<map " in contenu
            mark = "</mark>" in contenu
            menu = "</menu>" in contenu
            meta = "<meta " in contenu
            meter = "</meter>" in contenu
            nav = "</nav>" in contenu
            noscript = "</noscript>" in contenu
            object1 = "</object>" in contenu
            ol = "</ol>" in contenu
            optgroup = "</optgroup>" in contenu
            option = "</option>" in contenu
            output = "</output>" in contenu
            p = "</p>" in contenu
            picture = "</picture>" in contenu
            portal = "<portal>" in contenu
            pre = "</pre>" in contenu
            progress = "</progress>" in contenu
            q = "<q>" in contenu
            rp = "</rp>" in contenu
            rt = "</rt>" in contenu
            ruby = "</ruby>" in contenu
            s = "</s>" in contenu
            samp = "</samp>" in contenu
            script = "</script>" in contenu
            section = "</section>" in contenu
            select = "</select>" in contenu
            slot = "</slot>" in contenu
            small = "</small>" in contenu
            source = "<source " in contenu
            span = "</span>" in contenu
            strong = "</strong>" in contenu
            style = "</style>" in contenu
            sub = "</sub>" in contenu
            summary = "</summary>" in contenu
            sup = "</sup>" in contenu
            table = "</table>" in contenu
            tbody = "</tbody>" in contenu
            td = "</td>" in contenu
            template = "</template>" in contenu
            textarea = "</textarea>" in contenu
            tfoot = "</tfoot>" in contenu
            th = "</th>" in contenu
            thead = "</thead>" in contenu
            time = "</time>" in contenu
            title = "</title>" in contenu
            tr = "</tr>" in contenu
            track = "<track " in contenu
            u = "</u>" in contenu
            ul = "</ul>" in contenu
            var = "</var>" in contenu
            video = "</video>" in contenu
            wbr = "<wbr>" in contenu
            #print(div)

            if h1:
                file.write(balises.get("h1"))

            if a:
                file.write(balises.get("a"))
                
            if abbr:
                file.write(balises.get("abbr"))
            
            if acronym:
                file.write(balises.get("acronym"))

            if address:
                file.write(balises.get("address"))

            if area:
                file.write(balises.get("area"))
                
            if article:
                file.write(balises.get("article"))
            
            if aside:
                file.write(balises.get("aside"))

            if audio:
                file.write(balises.get("audio"))
            if b:
                file.write(balises.get("b"))
                
            if base:
                file.write(balises.get("base"))
            
            if bdi:
                file.write(balises.get("bdi"))

            if bdo:
                file.write(balises.get("bdo"))


            if blockquote:
                file.write(balises.get("blockquote"))
                
            if body:
                file.write(balises.get("body"))
            
            if br:
                file.write(balises.get("br"))

            if button:
                file.write(balises.get("button"))

            if canvas:
                file.write(balises.get("canvas"))
                
            if caption:
                file.write(balises.get("caption"))
            
            if cite:
                file.write(balises.get("cite"))

            if code:
                file.write(balises.get("code"))
            if col:
                file.write(balises.get("col"))
                
            if colgroup:
                file.write(balises.get("colgroup"))
            
            if data:
                file.write(balises.get("data"))

            if datalist:
                file.write(balises.get("datalist"))


            if dd:
                file.write(balises.get("dd"))
                
            if del1:
                file.write(balises.get("del"))
            
            if details:
                file.write(balises.get("details"))

            if dfn:
                file.write(balises.get("dfn"))

            if dialog:
                file.write(balises.get("dialog"))
                
            if div:
                file.write(balises.get("div"))
            
            if dl:
                file.write(balises.get("dl"))

            if dt:
                file.write(balises.get("dt"))
            if em:
                file.write(balises.get("em"))
                
            if embed:
                file.write(balises.get("embed"))
            
            if fieldset:
                file.write(balises.get("fieldset"))

            if figcaption:
                file.write(balises.get("figcaption"))


            if figure:
                file.write(balises.get("figure"))
                
            if footer:
                file.write(balises.get("footer"))
            
            if form:
                file.write(balises.get("form"))

            if head:
                file.write(balises.get("head"))

            if header:
                file.write(balises.get("header"))
                
            if hgroup:
                file.write(balises.get("hgroup"))
            
            if hr:
                file.write(balises.get("hr"))

            if html:
                file.write(balises.get("html"))
            if i:
                file.write(balises.get("i"))
                
            if iframe:
                file.write(balises.get("iframe"))
            
            if img:
                file.write(balises.get("img"))

            if input:
                file.write(balises.get("input"))

            if ins:
                file.write(balises.get("ins"))
            if kbd:
                file.write(balises.get("kbd"))
                
            if label:
                file.write(balises.get("label"))
            
            if legend:
                file.write(balises.get("legend"))

            if li:
                file.write(balises.get("li"))


            if link:
                file.write(balises.get("link"))
                
            if main:
                file.write(balises.get("main"))
            
            if map:
                file.write(balises.get("map"))

            if mark:
                file.write(balises.get("mark"))

            if menu:
                file.write(balises.get("menu"))
                
            if meta:
                file.write(balises.get("meta"))
            
            if meter:
                file.write(balises.get("meter"))

            if nav:
                file.write(balises.get("nav"))
            if noscript:
                file.write(balises.get("noscript"))
                
            if object1:
                file.write(balises.get("object"))
            
            if ol:
                file.write(balises.get("ol"))

            if optgroup:
                file.write(balises.get("optgroup"))


            if option:
                file.write(balises.get("option"))
                
            if output:
                file.write(balises.get("output"))
            
            if p:
                file.write(balises.get("p"))

            if picture:
                file.write(balises.get("picture"))

            if portal:
                file.write(balises.get("portal"))
                
            if pre:
                file.write(balises.get("pre"))
            
            if progress:
                file.write(balises.get("progress"))

            if q:
                file.write(balises.get("q"))
            if rp:
                file.write(balises.get("rp"))
                
            if rt:
                file.write(balises.get("rt"))
            
            if ruby:
                file.write(balises.get("ruby"))

            if s:
                file.write(balises.get("s"))


            if samp:
                file.write(balises.get("samp"))
                
            if script:
                file.write(balises.get("script"))
            
            if section:
                file.write(balises.get("section"))

            if select:
                file.write(balises.get("select"))

            if slot:
                file.write(balises.get("slot"))
                
            if small:
                file.write(balises.get("small"))
            
            if source:
                file.write(balises.get("source"))

            if span:
                file.write(balises.get("span"))
            if strong:
                file.write(balises.get("strong"))
                
            if style:
                file.write(balises.get("style"))
            
            if sub:
                file.write(balises.get("sub"))

            if summary:
                file.write(balises.get("summary"))

            if sup:
                file.write(balises.get("sup"))
            
            if table:
                file.write(balises.get("table"))

            if tbody:
                file.write(balises.get("tbody"))
            if td:
                file.write(balises.get("td"))
                
            if template:
                file.write(balises.get("template"))
            
            if textarea:
                file.write(balises.get("textarea"))

            if tfoot:
                file.write(balises.get("tfoot"))
            if th:
                file.write(balises.get("th"))
            
            if thead:
                file.write(balises.get("thead"))

            if time:
                file.write(balises.get("time"))
            if title:
                file.write(balises.get("title"))
                
            if tr:
                file.write(balises.get("tr"))
            
            if track:
                file.write(balises.get("track"))

            if u:
                file.write(balises.get("u"))

            if ul:
                file.write(balises.get("ul"))

            if var:
                file.write(balises.get("var"))

            if video:
                file.write(balises.get("video"))

            if wbr:
                file.write(balises.get("wbr"))



    print(bcolors.OK + "[FD] " + bcolors.RESET + "Fichier crée")


else :
    print(bcolors.OK + "[FD] " + bcolors.RESET + "Relancer le programme et veuillez rentrer le bon path")


