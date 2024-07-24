function parseAlpha(c) {
	return (c.charCodeAt(0) - 65) * 26 + c.charCodeAt(1) - 65;
}

function formatAlpha(c) {
	return String.fromCharCode(c / 26 + 65 | 0) + String.fromCharCode(c % 26 + 65);
}

function parseNum(n) {
	return n - 1;
}

function formatNum(n) {

	n = String(n + 1);
	for (var i = n.length; i < 3; i++) {
		n = '0' + n;
	}
	return n;
}

function solve(p, n) {

	var ndx = [0, 2, 1];
	var parse = [parseAlpha, parseAlpha, parseNum];
	var format = [formatAlpha, formatAlpha, formatNum];
	var bases = [26 * 26, 26 * 26, 999];

	p = p.split("-");
	p = p.map((v, i) => parse[i](p[ndx[i]]));

	n += p[0] * bases[2] * bases[1] + p[1] * bases[2] + p[2];

	var ret = [];
	for (var i = p.length - 1; i >= 0; i--) {
		ret[ndx[i]] = format[i](n % bases[i]);
		n = n / bases[i] | 0;
	}
	return ret.join("-");
}

var x = console.readline()
var n = console.readline()

console.log(solve(x, n));