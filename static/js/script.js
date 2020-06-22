window.parseISOString = function parseISOString(s) {
  var b = s.split(/\D+/);
  return new Date(Date.UTC(b[0], --b[1], b[2], b[3], b[4], b[5], b[6]));
};

const delete_venue_btn = document.getElementById('delete_venue');
if (delete_venue_btn) {
  delete_venue_btn.onclick = function (e) {
    const venueId = e.target.dataset['id'];
    fetch('/venues/' + venueId, {
        method: 'DELETE'
    }).then(function(){
      window.location.href = '/venues';
    });
  }
}