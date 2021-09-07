$(function() {
  /* NOTE: hard-refresh the browser once you've updated this */
  $(".typed").typed({
    strings: [
      "<br/>" +
      "' skills: data science, finance, information systems<br/> ^100" +
      "' education: copenhagenbs, kedgebs, yale, openclassroom<br/> ^100" +
      "' references: ibm, chanel, acom audit, chimitec<br/> ^100" +
      "' languages: french, english, spanish, portuguese <br/>" +
      "' software: microsoft package, sap, jupyter, sublime text, postgres <br/>" +
      "' hobbies: tennis, mountains, running, juggling, reading<br/> ^300" +
      "' status: academic exchange abroad<br/> ^100"/*
      "><span class='caret'>$</span> <a href='/timeline'>timeline</a> <a href='http://www.github.com/crearo/'>github</a> <a href='http://in.linkedin.com/in/bhardwajrish/'>linkedin</a> <a href='http://bhardwajrish.blogspot.com/'>blog</a><br/>"*/
    ],
    showCursor: true,
    cursorChar: '_',
    autoInsertCss: true,
    typeSpeed: 0.001,
    startDelay: 50,
    loop: false,
    showCursor: false,
    onStart: $('.message form').hide(),
    onStop: $('.message form').show(),
    onTypingResumed: $('.message form').hide(),
    onTypingPaused: $('.message form').show(),
    onComplete: $('.message form').show(),
    onStringTyped: function(pos, self) {$('.message form').show();},
  });
  $('.message form').hide()
});

