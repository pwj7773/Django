// 1. 글쓰기와 수정에서 쓸 수 있는 함수
/// 제목이 비어있거나 또는 5글자 이하라면 경고창 표시하고
/// 진행 멈춤
/// 글 내용이 비어있거나 10글자 이하라면 경고창 표시하고
/// 진행 멈춤
/// 제목이나 글 내용에 바보, 멍청이, 한조 들어 있으면 경고창 표시하고
/// 진행 멈춤
function formValidate(){
    let filters = ["바보","멍청이","한조"];
    let title = $("#title").val();
    let content = $("#content").val();

    if (title.trim() == "" || title.length < 6 ) {
        alert("제목이 비어있거나 또는 5글자 이하 입니다.");
        console.log(title.length);
        return false;
    }
    if (content.trim() == "" || content.length < 11 ) {
        alert("내용이 비어있거나 또는 11글자 이하 입니다.");
        return false;
    }

    for (i of filters) {
        if (title.includes(i) || content.includes(i)){
            alert(i + "가 포함되었습니다.");
            return false;
        }
    }
    return true;
}
