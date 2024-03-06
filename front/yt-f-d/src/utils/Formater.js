
/**Função responsável por colocar a url do vídeo no formato que o preview box precisa para incoorporar o vídeo na aplicação
 */
export default function formatTextUrl(url_share){
    let prefix = "https://www.youtube.com/embed/";
    let attr = url_share.split('/');

    return prefix + attr[3];

}