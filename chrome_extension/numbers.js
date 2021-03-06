//функция парсинга и тегирования
$.fn.highlight = function (pattern, settings_arg="highlight") {
      var settings_obj = {
        className: "highlight",
      };
      settings_obj = $.extend(settings_obj, settings_arg);
    function addClassNameToFindReuslt(element) {
        element = element.childNodes;
        for (var e = element.length, a; a = element[--e];)
            if (3 == a.nodeType) { // TEXT_NODE
                if (!/^\s+$/.test(a.data)) { //only letters
                    var d = a.data,
                        d = d.replace(pattern, '<span class="' + settings_obj.className + ' "data-content="$1">$1</span>');
                    $(a).replaceWith(d)
                }
            } else 
            {
            1 == a.nodeType && a.childNodes && (!/(script|style)/i.test(a.tagName) && a.className != settings_obj.className) && addClassNameToFindReuslt(a);
            }
    }
    
    return this.each(function () {
        addClassNameToFindReuslt(this);
    })
};

// выполнение функции парсинга и тегирования при загрузке страницы
start = function() {
    $("body").highlight(RegExp(/(\d[\d|.| |,]+)/, "gi"));
   
    Tipped.create('.highlight', function(element) {
     var target = $(element).data('content').toString( );
     var text="12";
     var xhr = new XMLHttpRequest();
     xhr.open('GET', 'https://space-obr-api-dev.herokuapp.com/number/?format=json&value='+target.replace(/ /gi,"").replace(',','.'), false);
     xhr.send();
     // (3)
       if (xhr.status != 200) {
       console.log("error");
     } else {
       var response = JSON.parse(xhr.responseText);
       console.log(response.results[0].value + response.results[0].unit + " - "+ response.results[0].link);
       text = "<a href='"+response.results[0].link+"'>"+ response.results[0].description_text+"</a>";
       title = parseFloat(response.results[0].value).toLocaleString() + " "+ response.results[0].unit;
       return{
        title: title ,
        content: text,
       }
       
      }
   }, {
    maxWidth: 200
   });
}; 

start()
