function hitungStatistik(data) {
  let jumlah = 0;
  let minimum = null;
  let maksimum = null;
  let genap = 0;
  let ganjil = 0;
  let positif = 0;
  let negatif = 0;
  let nol = 0;
  let totalKuadrat = 0;
  let totalKubik = 0;
  let rataRata = 0;
  let selisih = 0;
  let banyak = 0;
  let pertama = null;
  let terakhir = null;
  const urutan = [];
  const unik = new Set();
  let duplikat = 0;
  for (const nilai of data) {
    jumlah += 1;
    if (minimum === null || nilai < minimum) {
      minimum = nilai;
    }
    if (maksimum === null || nilai > maksimum) {
      maksimum = nilai;
    }
    if (nilai % 2 === 0) {
      genap += 1;
    } else {
      ganjil += 1;
    }
    if (nilai > 0) {
      positif += 1;
    } else if (nilai < 0) {
      negatif += 1;
    } else {
      nol += 1;
    }
    totalKuadrat += nilai * nilai;
    totalKubik += nilai * nilai * nilai;
    if (!unik.has(nilai)) {
      unik.add(nilai);
      urutan.push(nilai);
    } else {
      duplikat += 1;
    }
    if (pertama === null) {
      pertama = nilai;
    }
    terakhir = nilai;
  }
  banyak = data.length;
  if (banyak > 0) {
    rataRata = jumlah / banyak;
    selisih = maksimum - minimum;
  }
  return {
    jumlah,
    minimum,
    maksimum,
    genap,
    ganjil,
    positif,
    negatif,
    nol,
    totalKuadrat,
    totalKubik,
    rataRata,
    selisih,
    banyak,
    pertama,
    terakhir,
    urutan,
    duplikat,
  };
}

function pendek(a, b) {
  return a + b;
}
