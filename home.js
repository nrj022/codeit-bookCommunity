const bookList = document.querySelector(".best-seller");
const comprehensiveList = document.querySelector(".comprehensive");
const alladinList = document.querySelector(".alladdin");
const yes24List = document.querySelector(".yes24");

const bookListBtn = document.querySelector(".best-seller__type--button");
const comprehensiveBtn = document.querySelector(".comprehensive-btn");
const alladinBtn = document.querySelector(".alladdin-btn");
const yes24Btn = document.querySelector(".yes24-btn");

function showComprehensive() {
  alladinBtn.style.fontWeight = "unset";
  yes24Btn.style.fontWeight = "unset";
  alladinList.style.visibility = "hidden";
  yes24List.style.visibility = "hidden";
  comprehensiveBtn.style.fontWeight = "700";
  comprehensiveList.style.visibility = "visible";
}

function showAlladin() {
  comprehensiveBtn.style.fontWeight = "unset";
  yes24Btn.style.fontWeight = "unset";
  comprehensiveList.style.visibility = "hidden";
  yes24List.style.visibility = "hidden";
  alladinBtn.style.fontWeight = "700";
  alladinList.style.visibility = "visible";
}

function showYes24() {
  comprehensiveBtn.style.fontWeight = "unset";
  alladinBtn.style.fontWeight = "unset";
  comprehensiveList.style.visibility = "hidden";
  alladinList.style.visibility = "hidden";
  yes24Btn.style.fontWeight = "700";
  yes24List.style.visibility = "visible";
}

function init() {
  comprehensiveBtn.addEventListener("click", function () {
    showComprehensive();
  });
  alladinBtn.addEventListener("click", function () {
    showAlladin();
  });
  yes24Btn.addEventListener("click", function () {
    showYes24();
  });
}

init();
