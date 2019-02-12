//функция парсинга и тегирования
$.fn.highlight = function (b, k) {
    function l() {
        $("." + c.className).each(function (c, e) {
            var a = e.previousSibling,
                d = e.nextSibling,
                b = $(e),
                f = "";
            a && 3 == a.nodeType && (f += a.data, a.parentNode.removeChild(a));
            e.firstChild && (f += e.firstChild.data);
            d && 3 == d.nodeType && (f += d.data, d.parentNode.removeChild(d));
            b.replaceWith(f);
        })
    }
    function h(b) {
        b = b.childNodes;
        for (var e = b.length, a; a = b[--e];)
            if (3 == a.nodeType) {
                if (!/^\s+$/.test(a.data)) {
                    var d = a.data,
                        d = d.replace(m, '<span class="' + c.className + '"data-content="$1 Стоимость чегото">$1</span>');
                    $(a).replaceWith(d)
                }
            } else 
            {
            1 == a.nodeType && a.childNodes && (!/(script|style)/i.test(a.tagName) && a.className != c.className) && h(a);
            
            console.log("2");
            }
    }
    var c = {
        split: "\\s+",
        className: "highlight",
        caseSensitive: !1,
        strictly: !1,
        remove: !0
    }, c = $.extend(c, k);
    c.remove && l();
    b = $.trim(b);
   
    var g = c.strictly ? "" : "\\S*",
      //  m = RegExp("(" + g + b.replace(RegExp(c.split, "g"), g + "|" + g) + g + ")", (c.caseSensitive ? "" : "i") + "g");
      //регулярное выражение, которое отвечает за поиск денежных выражений
        m = RegExp("(" + "\\d+[\\$,р]"  + ")", (c.caseSensitive ? "" : "i") + "g");
       // m = RegExp("Вот");
    return this.each(function () {
        b && h(this);
    })
};

$(function () {
$('#scan').click(function () {
console.log($(this)[0].offsetTop);
       var settings = {};
       var pattern = $('#pattern').val();
       $("#right").prop("checked") && (settings.strictly = true);
       $("#case").prop("checked") && (settings.caseSensitive = true);
       $("#remove").prop("checked") && (settings.remove = false);
       pattern && $("div").highlight(pattern, settings)
   })
})
 $(function () {
  $('#fuck').click(function () {
  
console.log($(this)[0].innerHTML);
  })
 })
// выполнение функции парсинга и тегирования при загрузке страницы
$(window).load(function() {
   var settings = {};
       var pattern = $('#pattern').val();
       $("#right").prop("checked") && (settings.strictly = true);
       $("#case").prop("checked") && (settings.caseSensitive = true);
       $("#remove").prop("checked") && (settings.remove = false);
       pattern && $("div").highlight(pattern, settings)
    Tipped.create('.highlight', function(element) {
     var target = $(element).data('content');
     var text="12";
     var xhr = new XMLHttpRequest();
     xhr.open('GET', 'http://api.obr.space/number/?format=json&value='+target.replace(/\D+/gi,""), false);
     xhr.send();
     // (3)
       if (xhr.status != 200) {
       console.log("error");
     } else {
       var response = JSON.parse(xhr.responseText);
       console.log(response.results[0].value + response.results[0].unit + " - "+ response.results[0].description_text);
       text = response.results[0].value + response.results[0].unit + " - "+ response.results[0].description_text;
     }
   
     return {
       title: $(element).data('title'),
       content:text
     };
   }, {
     skin: 'light'
   });
}); 
