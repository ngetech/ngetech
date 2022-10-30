const createThreadCard = (data) => {
    return `<a id="thread-${data.pk}" class="p-4 bg-charcoal-800 hover:bg-charcoal-700 rounded-lg" href="/discussion/${data.pk}/">
      <div class="flex flex-col break-words gap-2">
        <p class="font-bold text-2xl">${data.title}</p>
        <p class="text-gray-500">Started by <span class="text-blue-600 font-medium">@${data.user}</span></p>
      </div>
    </a>`;
}

const getThreads = () => {
    $.get("/discussion/get/", (data) => {
        console.log(data);
        for(var i = 0; i < data.length; i++){
            console.log(data[i]);
            $("#forum").append(createThreadCard({
                pk: data[i].pk,
                title: data[i].fields.title,
                content: data[i].fields.content,
                user: data[i].fields.user[0]
            }));
        }
    });
}

$(document).ready(() => {
    getThreads();
});