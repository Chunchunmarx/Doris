/* ----- polyfills start ----- */
/**
 * Match String in start
 */
if (!String.prototype.startsWith)
{
    String.prototype.startsWith = function (searchString, position) {
        position = position || 0;
        return (this.indexOf(searchString, position) === position);
    };
}

/**
 * Match String in end
 */
if (!String.prototype.endsWith)
{
    String.prototype.endsWith = function (searchString, position) {
        var subjectString = this.toString();
        if (position === undefined || position > subjectString.length) {
            position = subjectString.length;
        }
        position -= searchString.length;
        var lastIndex = subjectString.indexOf(searchString, position);
        return (lastIndex !== -1 && lastIndex === position);
    };
}

/**
 * Match String in all
 */
if (!String.prototype.includes)
{
    String.prototype.includes = function () {
        'use strict';
        return String.prototype.indexOf.apply(this, arguments) !== -1;
    };
}
/* ----- polyfills end ----- */

/* ----- app objects ----- */
var flaskcode = window.flaskcode || {};

/* app level config */
flaskcode.config = (function () {
    /* private members */
    var _Data = function () {};
    var data = new _Data();
    /* public members */
    return {
        has: function (key) {
            return data.hasOwnProperty(key);
        },
        set: function (key, value) {
            data[key] = value;
        },
        get: function (key, default_value) {
            return (!this.has(key)) ? default_value : data[key];
        },
        remove: function (key) {
            return (this.has(key)) ? delete data[key] : false;
        },
        clear: function (keyPrefix) {
            if (keyPrefix) {
                var key;
                for (key in data) {
                    if (key.startsWith(keyPrefix)) {
                        delete data[key];
                    }
                }
            } else {
                data = {};
            }
        },
        backup: function () {
            return data;
        },
        restore: function (dataset) {
            if (!(dataset instanceof _Data)) {
                throw new TypeError('Invalid argument type.');
            }
            data = dataset;
        }
    };
})();

/* local storage */
flaskcode.storage = {
    set: function (key, value) {
        if (window.localStorage) {
            window.localStorage.setItem(key, value);
        } else {
            flaskcode.config.set('__storage_'+key, value);
        }
    },
    get: function (key) {
        if (window.localStorage) {
            return window.localStorage.getItem(key);
        } else {
            return flaskcode.config.get('__storage_'+key, null);
        }
    },
    remove: function (key) {
        if (window.localStorage) {
            window.localStorage.removeItem(key);
        } else {
            flaskcode.config.remove('__storage_'+key);
        }
    },
    clear: function () {
        if (window.localStorage) {
            window.localStorage.clear();
        } else {
            flaskcode.config.clear('__storage_');
        }
    },
};

/* truncate string from left */
flaskcode.strTruncateLeft = function (string, max_length, replacement) {
    string = '' + string;
    max_length = max_length || 30;
    if (typeof replacement == 'undefined') {
        replacement = '...';
    }
    return (string.length <= max_length + replacement.length) 
        ? string : (replacement + string.substring(string.length - max_length));
};

/* get parent directory path of given path */
flaskcode.dirname = function (path) {
    return path.replace(/\\/g, '/').replace(/\/[^/]*\/?$/, '');
};

/* autoremove plugin */
(function ($) {
    $.fn.autoremove = function (seconds, effect) {
        if (typeof seconds === 'string') {
            effect = seconds
            seconds = 5
        } else {
            seconds = parseInt(seconds) || 5;
        }
        var $this = this;
        var effectFunc = ['fadeOut', 'slideUp'].indexOf(effect) > -1 ? effect : 'fadeOut';
        setTimeout(function () {
            $this[effectFunc](400, function () {
                $(this).remove();
            });
        }, seconds * 1000);
        return $this;
    };
})(jQuery);


/* draggables */
/*
var dragging = false;
var dragging_horizontal = false;
   $('#dragbar-vertical').mousedown(function(e){
       e.preventDefault();

       dragging = true;
       var main = $('#secondary-list');
       var wrapper = $('#dir-wrapper');
       var ghostbar = $('<div>',
                        {id:'ghostbar',
                         css: {
                                width: main.outerWidth(),
                           			top: e.pageY,
                                left: main.offset().left
                               }
                        }).appendTo('#dir-wrapper');

        $(document).mousemove(function(e){
          ghostbar.css("top", (e.pageY + 2));
       });

    });

   $('#dragbar-horizontal').mousedown(function(e){
       e.preventDefault();
       dragging_horizontal = true;
       var main = $('#flaskcode-content');
       var wrapper = $('#page-row');
       var ghostbar = $('<div>',
                        {id:'ghostbar',
                         css: {
                                width: main.outerWidth(),
                                    top: e.pageX,
                                left: main.offset().left
                               }
                        }).appendTo('#page-row');

        $(document).mousemove(function(e){
          ghostbar.css("left", (e.pageX + 2));
       });

    });
   $(document).mouseup(function(e){
       if (dragging)
       {
           var percentage = ((e.pageY - $('#dir-wrapper').offset().top) / $('#dir-wrapper').height()) * 100;
           var mainPercentage = 100-percentage;

           $('#flaskcode-list').css("height",percentage + "%");
           $('#secondary-list').css("height",mainPercentage + "%");
           $('#ghostbar').remove();
           $(document).unbind('mousemove');
           dragging = false;
       }
    });


   $(document).mouseup(function(e){
       if (dragging_horizontal)
       {
           var percentage = ((e.pageX - $('#page-row').offset().left) / $('#page-row').weight()) * 100;
           var mainPercentage = 100-percentage;

           $('#left-view').css("weight",percentage + "%");
           $('#flaskcode-content').css("weight",mainPercentage + "%");
           $('#ghostbar').remove();
           $(document).unbind('mousemove');
           dragging_horizontal = false;
       }
    });
*/
 $("#panel-left").resizable({
   handleSelector: ".splitter",
   resizeHeight: false
 });

 $(".panel-top ").resizable({
   handleSelector: ".splitter-horizontal",
   resizeWidth: false
 });