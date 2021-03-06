// set csrf token
(function () {
    let csrftoken = Cookies.get('csrftoken');
    // console.log(csrftoken);
    $.ajaxSetup({
        headers: {"X-CSRFToken": csrftoken}
    });
})();

//Показать форму комментария
let openForm = function (id) {
    $(`#${id}`).show()
};
// Скрыть форму комментария
let closeForm = function (id) {
    $(`#${id}`).hide()
};
// Become a follower
let follow = function (id) {
    $.ajax({
        // url:{% url 'add-follower'%},
        url: "http://127.0.0.1:8000/profile/add-follower/",
        type: "POST",
        data: {
            pk: id,
        },
        success: (response) => {
        window.location = response;
        },
        error:(response) =>{
            console.log('can not add follower')
        }

    })
};
// User can remove himself from people he follows
let undofollow = function (id) {
    $.ajax({
        // url:{% url 'add-follower'%},
        url: "http://127.0.0.1:8000/profile/undo-follower/",
        type: "POST",
        data: {
            pk: id,
        },
        success: (response) => {
        window.location = response;
        },
        error:(response) =>{
            console.log('can not add follower')
        }

    })
};

// Поставить лайк
let like = function (id) {
    $.ajax({
        url: "http://127.0.0.1:8000/like/",
        type: "POST",
        data: {
            pk: id,
        },
        success: (response) => {
        //console.log('ajax ++++')
        window.location = response;
        }
    })
};

$(".need_auth").submit(function(e){
         e.preventDefault();
         var url = $(this).attr('action');
         var data = $(this).serialize();
         $.post(
            url,
            data,
            function(response){
                //almost impossible to see (because of reload)
                //console.log('respones coming');
                //console.log(response);
                window.location = response.location;
            }

        );
     });
