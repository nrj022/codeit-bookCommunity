const bookList = document.querySelector(".best-seller");
const kyoboList = document.querySelector(".kyobo");
const alladinList = document.querySelector(".alladdin");
const yes24List = document.querySelector(".yes24");

const bookListBtn = document.querySelector(".best-seller__type--button");
const kyoboBtn = document.querySelector(".kyobo-btn");
const alladinBtn = document.querySelector(".alladdin-btn");
const yes24Btn = document.querySelector(".yes24-btn");

function showKyobo() {
  alladinBtn.style.fontWeight = "unset";
  yes24Btn.style.fontWeight = "unset";
  alladinList.style.visibility = "hidden";
  yes24List.style.visibility = "hidden";
  kyoboBtn.style.fontWeight = "700";
  kyoboList.style.visibility = "visible";
}

function showAlladin() {
  kyoboBtn.style.fontWeight = "unset";
  yes24Btn.style.fontWeight = "unset";
  kyoboList.style.visibility = "hidden";
  yes24List.style.visibility = "hidden";
  alladinBtn.style.fontWeight = "700";
  alladinList.style.visibility = "visible";
}

function showYes24() {
  kyoboBtn.style.fontWeight = "unset";
  alladinBtn.style.fontWeight = "unset";
  kyoboList.style.visibility = "hidden";
  alladinList.style.visibility = "hidden";
  yes24Btn.style.fontWeight = "700";
  yes24List.style.visibility = "visible";
}

function init() {
  kyoboBtn.addEventListener("click", function () {
    showKyobo();
  });
  alladinBtn.addEventListener("click", function () {
    showAlladin();
  });
  yes24Btn.addEventListener("click", function () {
    showYes24();
  });
}

init();
