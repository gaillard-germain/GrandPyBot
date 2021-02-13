
$(function() {
  $('form').on('submit', function (event) {
    $.ajax({
      url: '/answer',
      data: {userentry : $('#userentry').val()},
      type: 'POST',
      })
    .done(function(data) {
      var question = document.createElement('p');
      question.classList.add('bubble', 'you');
      question.innerHTML = data.question;
      messagebox.appendChild(question);
      var answer = document.createElement('p');
      answer.classList.add('bubble', 'papy');
      answer.innerHTML = data.name + '<br>' + data.address;
      messagebox.appendChild(answer);
      $('#map').attr("src", data.source)
    });
    event.preventDefault();
    event.stopPropagation();
    });
});
