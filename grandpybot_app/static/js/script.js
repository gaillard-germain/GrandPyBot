
$(function() {
  $('form').on('submit', function (event) {
    $.ajax({
      url: '/answer',
      data: {userentry : $('#userentry').val()},
      type: 'POST',
      })
    .done(function(data) {
      var dialog = $('#userentry').val();
      addBubble(dialog, 'you');
      if (data == "nothing") {
        dialog = "Répète moi ça poussin... Je n'ai pas tout compris...";
        addBubble(dialog, 'papy');
      }else if (data == "noplace") {
        dialog = "Je n'en ai pas la moindre idée ma grenouille...désolé.";
        addBubble(dialog, 'papy');
      }else {
        dialog = data.name + '<br>' + data.address;
        addBubble(dialog, 'papy');
        dialog = data.info
        addBubble(dialog, 'papy')
        $('#map').attr("src", data.source);
      }
    });
    event.preventDefault();
    event.stopPropagation();
    });
});

function addBubble(dialog, cssClass) {
  var paragraph = document.createElement('p');
  paragraph.classList.add('bubble', cssClass);
  paragraph.innerHTML = dialog;
  messagebox.appendChild(paragraph);
}
