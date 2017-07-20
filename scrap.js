var request = require('request-promise-native');
var cheerio = require('cheerio');
var URL = require('url-parse');
var jsonfile = require('jsonfile');

const url = "http://www.thedevelopersconference.com.br";
var pageToVisit = "http://www.thedevelopersconference.com.br/tdc/2017/saopaulo/trilhas";
(async function functionName() {
		console.log("Visiting page " + pageToVisit);
		const $ = cheerio.load(await request(pageToVisit));
		console.log("Loaded ...");
		const json = (await Promise.all($("#trilhas-saopaulo .btn").map(function t(index, el) {
			const track_title = $(this).text().trim();
			const href = $(this).attr("href");
			// console.log(href);
			if(href.indexOf("javascript:") > -1){
				return;
			}
			// console.log(`loading ${ track_title }...`);
			return request(/www.thedevelopersconference.com.br/.test(href) ? href : `${ url }${ href }`).then(track => {
				console.log(`${ track_title } loaded.`);
				const c = cheerio.load(track);
				//
				// const title = c(".titulo-trilha").text().trim();
				const description = c(".lead").text().trim();
				const date = replace(c('.fa-calendar').parent().text()).match(/([0-9]{2}) de Julho de 2017/);

				return c("#accordion tr").map(function a() {
					const el = $(this);
					const time = replace(el.find(".horario").text()).split(' às ');
					const title = replace(el.find(".conteudo .palestra, .todos .breaks").text());
					const desc = replace(el.find(".conteudo .descricao").text());
					const palestrante = replace(el.find(".palestrante").text());
					return  { track_title ,time, title, palestrante, desc, date: date[1]};
				}).get().filter(({time, title}) => time && title);

			}, (err) => {
				console.log(err, ":/");
			});
		}).get())).reduce((ret, arr) => [...ret,...arr] ).filter(e => e);
		console.log("JSON ->", json);
		jsonfile.writeFile("scripts/programacao.json", json,{spaces: 2}, function (err) {
		  console.error(err)
		})

})();

const replace = text => text.trim().replace(/[ \n]+/igm, " ")
