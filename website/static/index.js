function deleteMoney(money_id) {
  fetch("/delete", {
    method: "POST",
    body: JSON.stringify({ money_id: money_id }),
  }).then(location.reload(true));
}
