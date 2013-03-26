Title: Implementing jQuery tablesorter natural sort plugin as text sort
Date: 2011-11-04 22:55
Author: Admin
Category: Programming

I have been doing quite a bit of web programming lately and was recently
trying to figure out how to get the jquery plugin '[tablesorter][]' to
perform a natural sort.

For those not aware of what natural sort is, it is the way in which
human beings tend to sort things intuitively (hence the prefix
'natural'). In fact, [coding horror as a pretty good article about
natural sort and how tough it can be][]. To cut the story short, it
ensures that word19 comes after word2 in a sorted list (a typical sort
would place word2 after, since the ascii characters in the 5th position
define the sort order).

Now, normally implementing a natural sort is not so difficult depending
on the language, you basically split up the areas of the string that
represent digits, and then sort each substring piece in order (string
order if two strings, numeric order if two digits). Unfortunately, the
javascript tablesorter plugin allows you to sort by providing a function
that takes an element to be sorted and transforms it into a different
string or number that must be sorted EITHER numerical OR textually, but
not both.

Looking around online didn't yield any good solutions aside from,
"implement a jquery plugin". So I got to wondering what how it could be
done. These plugins could take the either table or cell as an argument
but then you'd have to remain stateless and re-perform the entire
natural sort over again. It may be possible to also use the jquery data
api to store data about a table to be sorted and then fetch it on each
call (performing the natural sort once and assigning ids to each cell or
something).

It got me wondering about formulating a natural sorting algorithm as a
numeric or textual sort. So I tried to prove if it could be done. I tend
to get carried away and engrossed by certain little challenges like
this:

1.) Natural Sort As Numeric Sort

This should become clear shortly that natural sort cannot be easily
implemented as a stateless numerical sort. Since you are ultimately
converting the string to a number, you can simply make the string longer
to produce a bigger number and mess up the sort order.

2.) Natural Sort As Textual Sort

This seemed like it could work. A textual sort is just a sequential
comparison of ascii coded bytes, each with a numeric value. Natural sort
is also a set of sequential comparison operations that ultimately break
down to numeric comparisons. One simply needs to convert the numeric
pieces into a string of characters preserving the same order as the
numeric sort, then create a new string with these numeric characters
replaced.

I decided to follow the original idea of ascii code comparisons, and I
decided to convert each number to a fixed length string in which each
digit is a base 127 or 256 number. Why 127 or 256? They represent
standard and extended ascii code length and ensure that the values
always fall without the proper range. String needs to be fixed length so
that all numerals are compared equally (longer numbers won't be
incorrectly compared against smaller numbers). The length of your string
determines the maximum size of any numeric segment. That means that
using a N digit base 127 string gives you 127\^(N-1) numbers. At 10
digits, thats 3x10\^18 numbers. If you use base 256 you get 21 decimal
places. Technically you can go even higher with UTF8.

Anyway, here is my solution (excuse my probably ugly javascript,
truthfully its one of the first javascript functions I've written from
scratch).

    :::javascript
      ts.addParser({
      id: "natural",
      is: function(s) {
      return false;
      },
      format: function(s) {
      var ret = "";
      var num_str = "";
      var base_num = 256;
      var fixed_len = 10;
      var num_to_ascii_len_str = function (base, max_len, num)
      {
        var tmp = num;
        var ret = "";
        for (var i = 0; i < max_len; i++)
        {
          if (tmp > base)
          {
            var div = tmp / base;
            tmp = tmp - div * base;
            ret = String.fromCharCode(div) + ret;
          }
          else
          {
            ret = String.fromCharCode(tmp) + ret;
            tmp = 0;
          }
        }
        return ret;
      };
      for(var i = 0; i < s.length; i++)
      {
        code = s.charCodeAt(i);
        if (code > 47 && code < 58) {
          num_str = num_str + s.charAt(i);
        }
        else{
          if (num_str.length > 0)
          {
            ret = ret + num_to_ascii_len_str(base_num, fixed_len,
                parseInt(num_str));
            num_str = "";
          }
          else
          {
            ret = ret + s.charAt(i);
          }
        }
      }
      if (num_str.length > 0)
      {
        ret = ret + num_to_ascii_len_str(base_num, fixed_len,
            parseInt(num_str));
      }
      return ret;
      },
      type: "text"
      });

Hope this helps someone out there, as this kind of thing is useful but
not easily found. Oh and if anyone can figure out if its possible for
formulate this as a numeric sort or knows a better way to do this in the
context of the tablesorter plugin, please share!

  [tablesorter]: http://tablesorter.com/docs/
  [coding horror as a pretty good article about natural sort and how
  tough it can be]: http://www.codinghorror.com/blog/2007/12/sorting-for-humans-natural-sort-order.html
