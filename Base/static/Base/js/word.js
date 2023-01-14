
   $(document).ready(function(){
        $('.sec_div10 >  p').each(function() {
                var $this = $(this);
                words = $this.text()

                const re = ' ';
                const wordlist = words.split(re);
                var text = "";
                $this.innerHTML = "<p>" + text + "</p>";

                wordlist.forEach(myFunction);

                document.getElementById("words").innerHTML = output;

                function myFunction(item) {
                    text += "<sp> " + item + "</sp>";
                        }
              // $this.html($this.text().replace(/\b(\w+)\b/g, "<sp>$1</sp>"));
            });

        // bind to each span
        $('.sec_div10>  p > sp').hover(

            function() {

               let $word = $(this).text();
               let $id_gazal = $('#id_gazal').text() ;
               document.getElementById('id').value = $id_gazal;
               document.getElementById('word').value = $word;


               var $form = $('#wordform');
               var $serializedData = $form.serialize();
                console.log($serializedData);
                $('#word').text($(this).css('background-color','rgb(136, 197, 243)').text());

                $(this).addClass( "izoh" );

                var $hover = $('#hoverr');


                   var $izoh = $('.izoh')
                var position = $izoh.position();

                var width = $izoh.outerWidth();
                var height = $izoh.outerHeight();

                  $hover.css({
                     position: "absolute",
                     top: position.top + height + "px",
                     left: position.left + "px",
                   })
                   .show();

                   console.log(position.left);

                $.ajax({
                   url: '/gazalin_gazal/'+$id_gazal+'/',
                   type: "POST",
                   data: $serializedData,
                   dataType: 'json',
                   success: function (data) {

                            $hover.css('opacity', '1');
                            $hover.css('z-index', '1');
                           console.log('ok');
                           document.getElementById('id').value = data.soz;
                           document.getElementById('word').value = data.mano;

                   },
                   error:function(e){
                       console.log('topilmadi ');
                       $hover.css('opacity', '0');
                       $hover.css('z-index', '1');
                   }
                 });
               },

            function() { $('#word').text(''); $(this).css('background-color','');
            $(this).removeClass("izoh");
            $hover = $('#hoverr')
             $hover.css('opacity', '0');
            $hover.css('z-index', '-1');
            }
        );

       })




$(document).ready(function(){
    if (window.location.href.indexOf('search_result')>-1){

        if(!$('.result1 > p').text().trim()){
            console.log("Topilmadi");
        }
        else{

            $('.result1  >  p').each(function() {
                var $this = $(this);

                $this.html($this.text().replace(/\b(\w+)\b/g, "<sp>$1</sp>"));
            });
            $('.result1  >  p > sp').each(function() {
                var $this = $(this);
                $searchedWord = $('#searchedWord').text();
                console.log($searchedWord);
                $searchedWord2 = $searchedWord.replace($searchedWord[0], $searchedWord[0].toUpperCase());
                $searchedWord3 = $searchedWord.replace($searchedWord[0], $searchedWord[0].toLowerCase());

                if ($(this).text().includes($searchedWord) === true || $(this).text().includes($searchedWord2) === true || $(this).text().includes($searchedWord3) === true){
                     $this.css({"background-color": "rgb(136, 197, 243)", "font-size": "110%"});
                }
            });
        }
    };
})

$(document).ready(function (){
     if (window.location.href.indexOf('gazalin_gazal')>-1){
        if(!$('.sec_div10 > p').text().trim()){
            console.log("Topilmadi");
        }
        else{
            $('.sec_div10  >  p').each(function() {
                var $this = $(this);
                $searchedWord = $('#searchWord_new').text();
                console.log('So`z');
                console.log($searchedWord);
                $searchedWord2 = $searchedWord.replace($searchedWord[0], $searchedWord[0].toUpperCase());
                $searchedWord3 = $searchedWord.replace($searchedWord[0], $searchedWord[0].toLowerCase());

                if ($this.text().includes($searchedWord) === true || $this.text().includes($searchedWord2) === true || $this.text().includes($searchedWord3) === true){
                     $this.css({"background-color": "rgb(136, 197, 243)"});
                }
            });
        }
    };
})

   var $word_length= $('#word');
    var word_width = $word_length.outerWidth();

if  (word_width > '200px'){
    alert('salom')
    $word_length.addClass('marquee')
   }



$(document).ready(function(){
        $('.sec_div10 >  p').each(function() {
                var $this = $(this);
                janr_words = $this.text()

                const re = ' ';
                const janr_wordlist = janr_words.split(re);
                var janr_text = "";
                $this.innerHTML = "<p>" + janr_text + "</p>";

                janr_wordlist.forEach(myFunction);

                document.getElementById("janr_word").innerHTML = output;

                function myFunction(item) {
                    janr_text += "<sp> " + item + "</sp>";
                        }
              // $this.html($this.text().replace(/\b(\w+)\b/g, "<sp>$1</sp>"));
            });

        // bind to each span
        $('.sec_div10>  p > sp').hover(

            function() {

               let $janr_word = $(this).text();
               let $janr_id = $('#id_janr').text() ;
               document.getElementById('janr_id').value = $id_gazal;
               document.getElementById('janr_word').value = $word;


               var $form = $('#janr_wordform');
               var $janr_serializedData = $form.serialize();
                console.log($janr_serializedData);
                $('#janr_word').text($(this).css('background-color','rgb(136, 197, 243)').text());

                $(this).addClass( "izoh" );

                var $hover = $('#janr_hoverr');


                   var $izoh = $('.izoh')
                var position = $izoh.position();

                var width = $izoh.outerWidth();
                var height = $izoh.outerHeight();

                  $hover.css({
                     position: "absolute",
                     top: position.top + height + "px",
                     left: position.left + "px",
                   })
                   .show();

                   console.log(position.left);

                $.ajax({
                   url: '/devon/janr_misra/'+$id_janr+'/',
                   type: "POST",
                   data: $serializedData,
                   dataType: 'json',
                   success: function (data) {

                            $hover.css('opacity', '1');
                            $hover.css('z-index', '1');
                           console.log('ok');
                           document.getElementById('janr_id').value = data.janr_soz;
                           document.getElementById('janr_word').value = data.janr_mano;

                   },
                   error:function(e){
                       console.log('topilmadi ');
                       $hover.css('opacity', '0');
                       $hover.css('z-index', '1');
                   }
                 });
               },

            function() { $('#janr_word').text(''); $(this).css('background-color','');
            $(this).removeClass("izoh");
            $hover = $('#janr_hoverr')
             $hover.css('opacity', '0');
            $hover.css('z-index', '-1');
            }
        );

       })
