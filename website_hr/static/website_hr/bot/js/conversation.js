
const chat = {
    1: {
        text: 'HI THERE!.',
        options: [
            {
                text: '👋',
                next: 2
            }
        ]
    },
    2: {
        text: 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s!!',
        next: 3
    },
    3: {
        text: 'But you probably knew that anyway.',
        options: [
            {
                text: "<strong>OH!</strong>, nice!",
                next: 4
            },
            {
                text: "<strong>OK</strong>, I knew that",
                next: 5
            },
            {
                text: "<strong>okay</strong>, I Don't Care",
                next: 7
            }
        ]
    },
    4: {
        text: 'Awesome. This chat is still in development',
    },
    5: {
        text: 'Aah, you\'re Smart!',
        next: 6
    },
    6: {
        text: 'You should check this Out',
        options: [
            {
                text: "okay",
                url: "https://youtube.com/shorts/Obgnr9pc820?feature=share"
            }
        ]
    },

    7: {
        text: 'oh oh check this',
        options: [
            {
                text: "Please click this!",
                url: "https://youtu.be/dQw4w9WgXcQ"
            }
        ]
    }
};
