$(function() {
  $('form').on('submit', function (event) {
    var dialog = $('#userentry').val();
    addBubble(dialog, 'you');
    thinking().scrollIntoView({behavior: "smooth", block: "end"});
    $.ajax({
      url: '/answer',
      data: {userentry : $('#userentry').val()},
      type: 'POST'
      })
    .done(function(data) {
      $('#thinkbubble').hide();
      if (data == "nothing") {
        console.log('Invalid entry');
        dialog = "Répète moi ça poussin... Je n'ai pas tout compris...";
        addBubble(dialog, 'papy');
      }else if (data == "noplace") {
        console.log('No place found');
        dialog = "Je n'en ai pas la moindre idée ma grenouille...désolé.";
        addBubble(dialog, 'papy');
      }else {
        dialog = data.name + '<br>' + data.address;
        addBubble(dialog, 'papy');
        dialog = data.info;
        addBubble(dialog, 'papy');
        $('#map').attr("src", data.source);
      }
    });
    event.preventDefault();
    event.stopPropagation();
  });
});

function addBubble(dialog, cssClass) {
  var messagebox = document.getElementById('messagebox')
  var paragraph = document.createElement('p');
  paragraph.classList.add('bubble', cssClass);
  paragraph.innerHTML = dialog;
  paragraph.scrollIntoView({behavior: "smooth", block: "end"})
  messagebox.appendChild(paragraph);
  return paragraph
}

function thinking() {
  var messagebox = document.getElementById('messagebox');
  var thinkBubble = document.getElementById('thinkbubble');
  thinkBubble.style.display = "flex";
  messagebox.appendChild(thinkBubble);
  return thinkBubble
}
