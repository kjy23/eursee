import re

# 假设我们已经有了这三个字典：
STATIC_LOGOS = {
    "CNEWS": "https://i.ibb.co/qY6w8ds/cnews.png",
    "LCI": "https://i.ibb.co/Zfcrrr1/lci.png",
    "FRANCE INFO:": "https://i.ibb.co/XkLHrbC/frinfo2bl.png",
    "LE MÉDIA TV": "https://i.ibb.co/ZBqk6mK/lemedia.jpg",
    "LE MÉDIA TV -1H": "https://i.ibb.co/ZBqk6mK/lemedia.jpg",
    "EURONEWS FR": "https://i.ibb.co/VxLFYSj/euronews.png",
    "TV5MONDE INFO": "https://i.ibb.co/drk4BWw/tv5inf.png",
    "FRANCE 24 FR": "https://i.ibb.co/hKP8X8B/f24.png",
    "LCP-AN": "https://i.ibb.co/rkv3Nvq/lcpan.png",
    "PUBLIC-SÉNAT": "https://i.ibb.co/2jG942b/publicsn.png",
    "BFM 2": "https://i.ibb.co/2MhqYgg/bfm2.png",
    "BFM GRAND REPORTAGES": "https://i.ibb.co/ChVvjpF/bfmgr.jpg",
    "RMC TALK INFO": "https://i.ibb.co/k4Bs0Cj/rmcti.jpg",
    "20 MINUTES TV IDF": "https://i.ibb.co/5j6DZrt/20mn.png",
    "LE FIGARO IDF": "https://i.ibb.co/hcPj99k/fgro.png",
    "LE FIGARO LIVE": "https://i.ibb.co/hcPj99k/fgro.png",
    "i24 NEWS FR": "https://i.ibb.co/j68q1Bp/i24.png",
    "CGTN FRANÇAIS": "https://i.ibb.co/ZgqnqnJ/cgtnfr.png",
    "LN24 BE": "https://i.ibb.co/nR2HsVr/ln24.png",
    "MONACO INFO": "https://i.ibb.co/MZLCTmN/monacoinfo.png",
    "RDI CANADA": "https://i.ibb.co/sd7qf1w7/icirdiqb.png",
    "AFRICA 24 FR": "https://i.ibb.co/pdnMrZn/a24.png",
    "AFRICANEWS FR": "https://i.ibb.co/XSYtYHZ/africanews.png",
    "BFM BUSINESS": "https://i.ibb.co/HDB0sdh/bfmbusiness.png",
    "B SMART": "https://i.ibb.co/Tm8bZHc/bsmart.png",
    "BLOOMBERG FR": "https://i.ibb.co/Nn5x9Hq/bloom.jpg",
    "TV FINANCE": "https://i.ibb.co/cCXgWWw/tvfinance.jpg",
    "PRESS IR FRENCH [temp barker]": "https://i.ibb.co/rwbrckj/pressir.png",
    "RT FRANÇAIS [censure-blocked]": "https://i.ibb.co/D7w9h7Q/rt.png",
    "BFM TV (backup)": "https://i.ibb.co/kckRLh5/bfm.png",
    "BFM 2 (backup)": "https://i.ibb.co/2MhqYgg/bfm2.png",
    "BFM BUSINESS (backup)": "https://i.ibb.co/HDB0sdh/bfmbusiness.png",
    "LE MÉDIA TV (backup ko)": "https://i.ibb.co/ZBqk6mK/lemedia.jpg",
    "TV5MONDE INFO (backup)": "https://i.ibb.co/drk4BWw/tv5inf.png",
    "EURONEWS FR (backup)": "https://i.ibb.co/VxLFYSj/euronews.png",
    "FRANCE INFO: (backup)": "https://i.ibb.co/XkLHrbC/frinfo2bl.png",
    "FRANCE INFO: (backup-off)": "https://i.ibb.co/XkLHrbC/frinfo2bl.png",
    "FRANCE INFO: [find-host]": "https://i.ibb.co/XkLHrbC/frinfo2bl.png",
    "FRANCE 24 FR (backup)": "https://i.ibb.co/hKP8X8B/f24.png",
    "FRANCE 24 FR (backup-off)": "https://i.ibb.co/hKP8X8B/f24.png",
    "LCI (backup)": "https://i.ibb.co/Zfcrrr1/lci.png",
    "CNEWS (backup)": "https://i.ibb.co/qY6w8ds/cnews.png",
    "LE MÉDIA TV (backup)": "https://i.ibb.co/ZBqk6mK/lemedia.jpg",
    "LCP-AN (backup)": "https://i.ibb.co/rkv3Nvq/lcpan.png",
    "LE FIGARO IDF (backup)": "https://i.ibb.co/hcPj99k/fgro.png",
    "CGTN FRANÇAIS (backup)": "https://i.ibb.co/ZgqnqnJ/cgtnfr.png",
    "RDI CANADA (backup)": "https://i.ibb.co/sq11nQ1/rdicanada.png",
    "AFRICANEWS FR (backup)": "https://i.ibb.co/XSYtYHZ/africanews.png",
    "LCI [tkn-blocked]": "https://i.ibb.co/Zfcrrr1/lci.png",
    "TF1": "https://i.ibb.co/BBpR1Wx/tf1.png",
    "FRANCE 2": "https://i.ibb.co/GxWtcTm/fr2bl.png",
    "FRANCE 3": "https://i.ibb.co/y8PjbJ4/fr3bl.png",
    "FRANCE 4": "https://i.ibb.co/VgcrtZ5/fr4blok.png",
    "FRANCE 5": "https://i.ibb.co/N9d4yXt/fr5bl.png",
    "FRANCE TV SÉRIES": "https://i.ibb.co/9rmSGqP/frsr.png",
    "FRANCE TV DOCUMENTAIRES": "https://i.ibb.co/kJjHW61/frdocs.png",
    "ARTE": "https://i.ibb.co/BPpZPBn/arte.png",
    "ARTE -0,5H": "https://i.ibb.co/BPpZPBn/arte.png",
    "CHÉRIE 25": "https://i.ibb.co/R3KG4L9/cherie25.png",
    "CANAL+ EN CLAIR": "https://i.ibb.co/ftYS2bk/CANAL-logo.png",
    "RMC STORY": "https://i.ibb.co/fdYg3Lz/rmcstory.png",
    "RMC DÉCOUVERTE": "https://i.ibb.co/VS4xR2g/rmcdecou.png",
    "CSTAR": "https://i.ibb.co/Sm9PtLR/cstar.png",
    "TMC": "https://i.ibb.co/hKVyKj4/tmc.png",
    "TV5MONDE EUROPE [geo-area]": "https://i.ibb.co/420Bjqt/tv5europe.png",
    "TV5MONDE MOYEN-ORIENT [geo-area]": "https://i.ibb.co/x8YnkQ2/tv5.png",
    "TV5MONDE ASIE SUD-EST [geo-area]": "https://i.ibb.co/x8YnkQ2/tv5.png",
    "TV5MONDE PACIFIQUE [geo-area]": "https://i.ibb.co/x8YnkQ2/tv5.png",
    "CANAL+ EN CLAIR (backup)": "https://i.ibb.co/ftYS2bk/CANAL-logo.png",
    "M6 [drm-keycrypted]": "https://i.ibb.co/wgJTdGY/m6.png",
    "W9 [drm-keycrypted]": "https://i.ibb.co/LNRd253/w9.png",
    "6TER [drm-keycrypted]": "https://i.ibb.co/nzh88j8/6ter.png",
    "NRJ 12 [OUT]": "https://i.ibb.co/6spXX2y/nrj12.png",
    "C8 [OUT]": "https://i.ibb.co/cQbcrGZ/c8.png",
    "CSTAR (backup)": "https://i.ibb.co/Sm9PtLR/cstar.png",
    "TF1 (backup)": "https://i.ibb.co/BBpR1Wx/tf1.png",
    "FRANCE 2 (backup)": "https://i.ibb.co/GxWtcTm/fr2bl.png",
    "FRANCE 3 (backup)": "https://i.ibb.co/y8PjbJ4/fr3bl.png",
    "FRANCE 4 (backup)": "https://i.ibb.co/VgcrtZ5/fr4blok.png",
    "FRANCE 5 (backup)": "https://i.ibb.co/N9d4yXt/fr5bl.png",
    "ARTE (backup)": "https://i.ibb.co/BPpZPBn/arte.png",
    "M6 (backup)": "https://i.ibb.co/wgJTdGY/m6.png",
    "M6 (test)": "https://i.ibb.co/wgJTdGY/m6.png",
    "W9 (check)": "https://i.ibb.co/LNRd253/w9.png",
    "FUN RADIO TV FR": "https://i.ibb.co/ByN83p3/funradtv.png",
    "GÉNÉRATIONS TV": "https://i.ibb.co/g3YTn6c/geneok.png",
    "MÉLODY": "https://i.ibb.co/BPzb19X/melody.png",
    "INA 70s": "https://i.ibb.co/svWdczbW/ina.png",
    "QWEST JAZZ": "https://i.ibb.co/B2Z50vtt/qwest.png",
    "CLUBBING TV": "https://i.ibb.co/M5P1TMG/clubbing.png",
    "TRACE URBAN": "https://i.ibb.co/2hgmDs6/traceurb.png",
    "TRACE SPORTS": "https://i.ibb.co/sWxH6cv/tracesports.png",
    "SPORT EN FRANCE": "https://i.ibb.co/p1stMyz/sportenfr.webp",
    "L'ÉQUIPE LIVE 1": "https://i.ibb.co/cXRbJz4/eqps.png",
    "L'ÉQUIPE LIVE 2": "https://i.ibb.co/cXRbJz4/eqps.png",
    "L'ÉQUIPE TV": "https://i.ibb.co/KXhYwm0/lequipe.png",
    "L'ÉQUIPE LIVE 3 EVENTS": "https://i.ibb.co/cXRbJz4/eqps.png",
    "L'ÉQUIPE LIVE 4 EVENTS": "https://i.ibb.co/cXRbJz4/eqps.png",
    "L'ÉQUIPE LIVE FOOT": "https://i.ibb.co/cXRbJz4/eqps.png",
    "RMC TALK SPORT": "https://i.ibb.co/gTxbf2C/rmcts.jpg",
    "JOURNAL DU GOLF": "https://i.ibb.co/Xt5YPJY/jdgolf.png",
    "L'ÉSPRIT SORCIER TV": "https://i.ibb.co/yPsXSFf/esprsorc.png",
    "SQOOL TV": "https://i.ibb.co/HnSphLp/sqool.jpg",
    "GULLI": "https://i.ibb.co/LQXjFc3/gulli.png",
    "GONG": "https://i.ibb.co/MMpFXQL/gong.jpg",
    "SUPERTOONS FR": "https://i.ibb.co/m4qxfcH/supertoons.jpg",
    "PLUTO KIDS": "https://i.ibb.co/92Q9cRS/plutokids.jpg",
    "VEVO POP": "https://i.ibb.co/brFBnw8/vevopop.png",
    "VEVO HP RB": "https://i.ibb.co/WFQ0NCF/vevohprb.png",
    "VEVO 90 00": "https://i.ibb.co/3CtD77v/vevo90.png",
    "MGG E-SPORT": "https://i.ibb.co/kDmhscZ/mgg.png",
    "FIFA+ FR": "https://i.ibb.co/hFf6hc4T/fifaplus.jpg",
    "DRIVE AUTO": "https://i.ibb.co/Xs1PxZs/driveauto.png",
    "MOTORSPORT FR": "https://i.ibb.co/0YKFn02/motorvisionfrs.png",
    "MOTORVISION FR": "https://i.ibb.co/0YKFn02/motorvisionfrs.png",
    "MOTORVISION TV": "https://i.ibb.co/0sdMx5Z/mtrvsn.png",
    "MOTORVISION TV-2": "https://i.ibb.co/0sdMx5Z/mtrvsn.png",
    "TECH&CO": "https://i.ibb.co/443jKxq/techco.png",
    "MEN'S UP TV": "https://i.ibb.co/tcYgz6h/mensup.png",
    "TOP SANTÉ": "https://i.ibb.co/TLPBT2L/topsante.png",
    "MAISON & TRAVAUX": "https://i.ibb.co/d66k2fw/maisontrvx.png",
    "NATURE TIME": "https://i.ibb.co/HzXTSvk/naturetime.jpg",
    "TRAVEL XP": "https://i.ibb.co/tYqGGQp/travelxp.jpg",
    "TV5MONDE VOYAGE": "https://i.ibb.co/vxqS6F0/tv5voyage.png",
    "VOYAGES ET SAVEURS": "https://i.ibb.co/2F8Cqdn/voyagessaveurs.png",
    "VOYAGES+": "https://i.ibb.co/JRX9cpG/voyagesplus.jpg",
    "PLUTO CUISINE": "https://i.ibb.co/vH6Q8Qx/plutocuisine.jpg",
    "RMC WOW": "https://i.ibb.co/d6JJHZR/rmcwow.jpg",
    "RMC MYSTÈRE": "https://i.ibb.co/VpvbTn4/rmcmyst.jpg",
    "RMC MECANIC": "https://i.ibb.co/c3ZRH8G/rmcmeca.jpg",
    "RMC ALERTE SECOURS": "https://i.ibb.co/tpy1mKV/rmcalertes.jpg",
    "ALLO CINÉ": "https://i.ibb.co/2SHJGsj/allocine.png",
    "RAKUTEN TOP FILMS TV": "https://i.ibb.co/3v8W06Q/rakutenfilms.png",
    "BREF CINÉ": "https://i.ibb.co/yhRGCbH/Brefcin.png",
    "CINÉ PRIME": "https://i.ibb.co/Hpqbt3q/cineprime.png",
    "FAMILY CLUB": "https://i.ibb.co/xqMPP7j/famclub.png",
    "FILMS FRANÇAIS": "https://i.ibb.co/M9XhS35/filmsfr.jpg",
    "WILD SIDE TV": "https://i.ibb.co/VvMKr5V/wildside.jpg",
    "TELE NOVELA TV": "https://i.ibb.co/grBSqt4/novela.png",
    "BBLACK! AFRICA": "https://i.ibb.co/JB18vMW/bblack.png",
    "BBLACK! CARIBBEAN": "https://i.ibb.co/JB18vMW/bblack.png",
    "BBLACK! CLASSIK": "https://i.ibb.co/JB18vMW/bblack.png",
    "UNIVERS CINÉ": "https://i.ibb.co/f1FyTkt/universcine.jpg",
    "PLUTO CINÉ": "https://i.ibb.co/px6TJjx/plutocine.jpg",
    "PLUTO POLAR": "https://i.ibb.co/h1M7Xrt/plutopolar.jpg",
    "CINÉ NANAR": "https://i.ibb.co/02pwsTj/cinenanar.png",
    "CINÉ WESTERN": "https://i.ibb.co/QbDCvVf/cinewestern.png",
    "KTO": "https://i.ibb.co/883phd1/ktook.png",
    "DIEU TV": "https://i.ibb.co/xJyNqdg/dieutv.png",
    "EMCI TV": "https://i.ibb.co/0FM2MbV/emci.png",
    "MUSEUM": "https://i.ibb.co/LgSzMCy/museum.webp",
    "MY ZEN": "https://i.ibb.co/VvRpRty/myzen.png",
    "MY ZEN WELLBEING": "https://i.ibb.co/VvRpRty/myzen.png",
    "FASHION TV": "https://i.ibb.co/LYbF1Wt/fashionok.png",
    "TRACE URBAN (backup)": "https://i.ibb.co/2hgmDs6/traceurb.png",
    "TV5MONDE STYLE [geo-area]": "https://i.ibb.co/WPbxmgn/tv5style.png",
    "TV5MONDE TiVi [geo-area]": "https://i.ibb.co/Jpk0d48/tv5tivi.png",
    "GULLI (backup)": "https://i.ibb.co/LQXjFc3/gulli.png",
    "FUN RADIO TV BE [died-link]": "https://i.ibb.co/ByN83p3/funradtv.png",
    "FUN RADIO TV BE (backup)": "https://i.ibb.co/ByN83p3/funradtv.png",
    "BFM ALPES": "https://i.ibb.co/mzhSFNV/bfmregions.png",
    "BFM ALSACE": "https://i.ibb.co/mzhSFNV/bfmregions.png",
    "BFM H.PROVENCE": "https://i.ibb.co/mzhSFNV/bfmregions.png",
    "BFM LILLE": "https://i.ibb.co/mzhSFNV/bfmregions.png",
    "BFM LITTORAL": "https://i.ibb.co/mzhSFNV/bfmregions.png",
    "BFM LYON": "https://i.ibb.co/mzhSFNV/bfmregions.png",
    "BFM MARSEILLE": "https://i.ibb.co/mzhSFNV/bfmregions.png",
    "BFM NICE": "https://i.ibb.co/mzhSFNV/bfmregions.png",
    "BFM NORMANDIE": "https://i.ibb.co/mzhSFNV/bfmregions.png",
    "BFM PARIS": "https://i.ibb.co/mzhSFNV/bfmregions.png",
    "BFM TOULON": "https://i.ibb.co/mzhSFNV/bfmregions.png",
    "F3/ICI PARIS IDF": "https://i.ibb.co/z8SYHqs/f3ici.png",
    "F3/ICI PROVENCE ALPES": "https://i.ibb.co/z8SYHqs/f3ici.png",
    "F3/ICI CÔTE D'AZUR": "https://i.ibb.co/z8SYHqs/f3ici.png",
    "F3/ICI RHÔNE ALPES": "https://i.ibb.co/z8SYHqs/f3ici.png",
    "F3/ICI ALPES": "https://i.ibb.co/z8SYHqs/f3ici.png",
    "F3/ICI AUVERGNE": "https://i.ibb.co/z8SYHqs/f3ici.png",
    "F3/ICI BOURGOGNE": "https://i.ibb.co/z8SYHqs/f3ici.png",
    "F3/ICI FRANCHE COMPTÉ": "https://i.ibb.co/z8SYHqs/f3ici.png",
    "F3/ICI CENTRE": "https://i.ibb.co/z8SYHqs/f3ici.png",
    "F3/ICI CORSE VÍA STELLA": "https://i.ibb.co/z8SYHqs/f3ici.png",
    "F3/ICI ALSACE": "https://i.ibb.co/z8SYHqs/f3ici.png",
    "F3/ICI CHAMPAGNE": "https://i.ibb.co/z8SYHqs/f3ici.png",
    "F3/ICI LORRAINE": "https://i.ibb.co/z8SYHqs/f3ici.png",
    "F3/ICI NORD PDC": "https://i.ibb.co/z8SYHqs/f3ici.png",
    "F3/ICI PICARDIE": "https://i.ibb.co/z8SYHqs/f3ici.png",
    "F3/ICI B.NORMANDIE": "https://i.ibb.co/z8SYHqs/f3ici.png",
    "F3/ICI H.NORMANDIE": "https://i.ibb.co/z8SYHqs/f3ici.png",
    "F3/ICI AQUITAINE": "https://i.ibb.co/z8SYHqs/f3ici.png",
    "F3/ICI NOA": "https://i.ibb.co/z8SYHqs/f3ici.png",
    "F3/ICI LIMOUSIN": "https://i.ibb.co/z8SYHqs/f3ici.png",
    "F3/ICI POITOU CHARENTES": "https://i.ibb.co/z8SYHqs/f3ici.png",
    "F3/ICI MIDI PYRÉNÉES": "https://i.ibb.co/z8SYHqs/f3ici.png",
    "F3/ICI LANGUEDOC": "https://i.ibb.co/z8SYHqs/f3ici.png",
    "F3/ICI PAYS LOIRE": "https://i.ibb.co/z8SYHqs/f3ici.png",
    "F3/ICI BRETAGNE": "https://i.ibb.co/z8SYHqs/f3ici.png",
    "TÉBÉO TV": "https://i.ibb.co/xmhMMDN/tebeo.png",
    "TVR RENNES": "https://i.ibb.co/3k4Lv34/tvrennes.png",
    "BORDO TV": "https://i.ibb.co/C5mwn8j2/bordotv.png",
    "BORDO SPORT": "https://i.ibb.co/vCB3X1Hm/bordosport.png",
    "C11 MÉDIA": "https://i.ibb.co/PGX8qp8n/c11media.png",
    "TÉLÉ NANTES": "https://i.ibb.co/3y88kpg/telenantes.jpg",
    "TV VENDÉE": "https://i.ibb.co/xS8B1qS/tvvendee.png",
    "TV 78": "https://i.ibb.co/fdcDJWF/tv78.png",
    "7A LIMOGES": "https://i.ibb.co/WpSPwkN/7alim.png",
    "ALPE D'HUEZ TV": "https://i.ibb.co/zRLKgFS/alpehuez.png",
    "BIP TV": "https://i.ibb.co/61mqv2h/biptv.png",
    "CANAL 32": "https://i.ibb.co/Dpsn6ZV/c32.png",
    "IL TV": "https://i.ibb.co/YLL42C6/iltv.png",
    "MOSELLE TV": "https://i.ibb.co/vmqkmDB/moselle.jpg",
    "TV7 BORDEAUX": "https://i.ibb.co/9VrjLFT/tv7b.png",
    "TV7 COLMAR": "https://i.ibb.co/d6x3fxq/tv7colm.png",
    "TV 3V": "https://i.ibb.co/2nG96GF/tv3v.png",
    "VIA MATÉLÉ": "https://i.ibb.co/4ZfHZhf/viamatele.png",
    "VIA OCCITANIE": "https://i.ibb.co/3My0NGd/viaocc.png",
    "VIA TELEPAESE": "https://i.ibb.co/nQP8st8/telepaese.png",
    "VOSGES TV": "https://i.ibb.co/qkkHNPR/vosges.png",
    "WÉO NORD PICARDIE": "https://i.ibb.co/nMkybxK/weo1.png",
    "NANCY WEB TV": "https://i.ibb.co/KGNTppx/nancyweb.jpg",
    "MAURIENNE TV": "https://i.ibb.co/MMDSDQ9/maurienne.png",
    "LA CHAÎNE 32": "https://i.ibb.co/dDbcFbF/lch32.png",
    "TÉLÉ GOHELLE": "https://i.ibb.co/VNDPTDY/tgohelle.png",
    "TVPI BAYONNE": "https://i.ibb.co/6W98gzZ/tvpi.png",
    "PUISSANCE TÉLÉVISION": "https://i.ibb.co/1rDLsMp/puisstv.png",
    "NA TV": "https://i.ibb.co/Tr2b0gV/natv.png",
    "KANAL DUDE": "https://i.ibb.co/2Zb8Gmb/kdude.png",
    "CANNES LÉRINS TV": "https://i.ibb.co/0q3DHhF/cannesler.png",
    "LITTORAL TV": "https://i.ibb.co/tLPxcFn/littoral.png",
    "TV TARN": "https://i.ibb.co/QYJL1N7/tarn.png",
    "MOSAIK CRISTAL TV": "https://i.ibb.co/Jk1ND0P/mosaik.png",
    "TV8 MONTBLANC": "https://i.ibb.co/74fJt5v/8mblanc.png",
    "TVT TOURS": "https://i.ibb.co/vDRB1fK/tvtloire.png",
    "ANGERS TÉLÉ": "https://i.ibb.co/QM2Y7TV/angtl.jpg",
    "LYON CAPITALE TV": "https://i.ibb.co/3NX9rPp/lyoncap.png",
    "TL CHOLETAIS": "https://i.ibb.co/h2VX7Wj/tlcholt.png",
    "BRIONNAIS TV": "https://i.ibb.co/S0X9VM8/brion.jpg",
    "VALLOIRE TV": "https://i.ibb.co/c2MfMVN/valloire.jpg",
    "N31": "https://i.ibb.co/gj4ZGdY/n31.jpg",
    "TÉLÉ GRENOBLE": "https://i.ibb.co/c2CBDqt/grenoble.png",
    "LM TV SARTHE": "https://i.ibb.co/nccDkr5/lmtv.png",
    "ASTV": "https://i.ibb.co/2qs2HxR/astv.png",
    "TL7 LOIRE": "https://i.ibb.co/yRLR4Ny/tl7l.png",
    "MARITIMA TV": "https://i.ibb.co/C99d8Z7/maritima.jpg",
    "TÉLÉ BOCAL": "https://i.ibb.co/1RVPRkx/bocal.png",
    "UBIZNEWS OM5TV": "https://i.ibb.co/3pbTbdG/ubizom.jpg",
    "MADRAS FM TV": "https://i.ibb.co/BwD72ps/madras.png",
    "ANTENNE RÉUNION": "https://i.ibb.co/PxqLyjh/antreu.png",
    "LA BRISE HAÏTI": "https://i.ibb.co/CPZ00LY/labrise.jpg",
    "TNTV": "https://i.ibb.co/kcPbyTD/tntv.png",
    "ETV GUADELOUPE": "https://i.ibb.co/CB78JpG/etvgp.png",
    "FUSION TV": "https://i.ibb.co/Psz0Q4Zm/fusiontv.jpg",
    "LA 1ÈRE MARTINIQUE [geo-area]": "https://i.ibb.co/GkjLyFv/la1ereom.png",
    "LA 1ÈRE GUADELOUPE [geo-area]": "https://i.ibb.co/GkjLyFv/la1ereom.png",
    "LA 1ÈRE GUYANE [geo-area]": "https://i.ibb.co/GkjLyFv/la1ereom.png",
    "LA 1ÈRE MAYOTTE [geo-area]": "https://i.ibb.co/GkjLyFv/la1ereom.png",
    "LA 1ÈRE RÉUNION [geo-area]": "https://i.ibb.co/GkjLyFv/la1ereom.png",
    "LA 1ÈRE N.CALÉDONIE [geo-area]": "https://i.ibb.co/GkjLyFv/la1ereom.png",
    "LA 1ÈRE POLYNÉSIE [geo-area]": "https://i.ibb.co/GkjLyFv/la1ereom.png",
    "LA 1ÈRE WALLIS FUTUNA [geo-area]": "https://i.ibb.co/GkjLyFv/la1ereom.png",
    "LA 1ÈRE SAINT-PIERRE MIQUELON [geo-area]": "https://i.ibb.co/GkjLyFv/la1ereom.png",
    "LA 1ÈRE MARTINIQUE (news only)": "https://i.ibb.co/GkjLyFv/la1ereom.png",
    "LA 1ÈRE GUADELOUPE (news only)": "https://i.ibb.co/GkjLyFv/la1ereom.png",
    "LA 1ÈRE GUYANE (news only)": "https://i.ibb.co/GkjLyFv/la1ereom.png",
    "LA 1ÈRE MAYOTTE (news only)": "https://i.ibb.co/GkjLyFv/la1ereom.png",
    "LA 1ÈRE RÉUNION (news only)": "https://i.ibb.co/GkjLyFv/la1ereom.png",
    "LA 1ÈRE N.CALÉDONIE (news only)": "https://i.ibb.co/GkjLyFv/la1ereom.png",
    "LA 1ÈRE POLYNÉSIE (news only)": "https://i.ibb.co/GkjLyFv/la1ereom.png",
    "LA 1ÈRE WALLIS FUTUNA (news only)": "https://i.ibb.co/GkjLyFv/la1ereom.png",
    "LA 1ÈRE SAINT-PIERRE MIQUELON (news only)": "https://i.ibb.co/GkjLyFv/la1ereom.png",
    "TV MONACO": "https://i.ibb.co/XjzvmqL/tvmonaco.jpg",
    "BEL RTL": "https://i.ibb.co/NyHqX5R/belrtl.png",
    "LA TÉLÉ": "https://i.ibb.co/WGHbhfh/latelebe.png",
    "NO TÉLÉ": "https://i.ibb.co/RCY8bJZ/notele.png",
    "TÉLÉ BRUXELLES": "https://i.ibb.co/4dTPMzK/tlbrux.png",
    "VEDIA": "https://i.ibb.co/cbbQ0hK/vedia.png",
    "RTC TÉLÉ LIÈGE": "https://i.ibb.co/4YZfGGL/rtcliege.png",
    "QUATRE LIÈGE": "https://i.ibb.co/ZphSkW0n/qu4trebe.jpg",
    "TÉLÉ MB": "https://i.ibb.co/5TyhqWc/telemb.jpg",
    "BOUKÈ": "https://i.ibb.co/y0jz90j/bouke.jpg",
    "ANTENNE CENTRE": "https://i.ibb.co/2F48hsL/actv.png",
    "CANAL ZOOM": "https://i.ibb.co/0VSd8bM/zoombe.png",
    "SAMBRE CHARLEROI": "https://i.ibb.co/8gczbQk/sambre.png",
    "BRABANT WALLON": "https://i.ibb.co/NSZgQQG/Brabant.png",
    "TV LUX": "https://i.ibb.co/MCtzw8h/tvlux.png",
    "NOOVO": "https://i.ibb.co/fqq90Z2/noovo.png",
    "LÉMAN BLEU": "https://i.ibb.co/CQb8zFT/lemanbleu.jpg",
    "CARAC 1": "https://i.ibb.co/Y8QFgbN/carac.png",
    "CARAC 2": "https://i.ibb.co/Y8QFgbN/carac.png",
    "CARAC 3": "https://i.ibb.co/Y8QFgbN/carac.png",
    "CARAC 4": "https://i.ibb.co/Y8QFgbN/carac.png",
    "TVM 3": "https://i.ibb.co/gz2wbkL/tvm3.png",
    "CANAL 9": "https://i.ibb.co/1XYdy6j/canal9.png",
    "CANAL ALPHA": "https://i.ibb.co/st6cDg1/calpha.png",
    "M LE MÉDIA": "https://i.ibb.co/FzJtxkx/mmediach.png",
    "SAVOIR.MÉDIA": "https://i.ibb.co/LzWqD0s/savoirmedia.png",
    "TÉLÉ QUÉBEC": "https://i.ibb.co/hFr5pYb/telequebec.png",
    "CPAC TV": "https://i.ibb.co/HqLCHkz/cpac.png",
    "ICI QUÉBEC": "https://i.ibb.co/whkNzKNr/iciteleqb.png",
    "ICI MONTRÉAL": "https://i.ibb.co/tHBB7zv/icimontreal.png",
    "SÖZCÜ TV": "https://i.ibb.co/B40rjP3/szc1.png",
    "HABER TÜRK": "https://i.ibb.co/wdwm0fn/haberturk.png",
    "HABER GLOBAL": "https://i.ibb.co/k58p7P2/hglobal.png",
    "HALK TV": "https://i.ibb.co/BtYMK4q/halk21a.png",
    "TV 100": "https://i.ibb.co/bLpTdYZ/tv100.png",
    "TELE 1": "https://i.ibb.co/4Mhmggc/tele1.png",
    "MK TV": "https://i.ibb.co/wrMn5rgQ/mktv.png",
    "EKOL TV": "https://i.ibb.co/Ln92Dj2/Ekoltv.png",
    "ULUSAL KANAL": "https://i.ibb.co/tXdf2YF/ulusal22.png",
    "NTV": "https://i.ibb.co/9c7MvWX/ntv.png",
    "TV 5": "https://i.ibb.co/6m9Pb3t/tv5tr1.png",
    "BLOOMBERG HT": "https://i.ibb.co/HXKrJRC/blght22.png",
    "EKO TÜRK": "https://i.ibb.co/xS3zLQr/ekoturk.png",
    "CNN TÜRK": "https://i.ibb.co/JqWCczW/cnnturk1.png",
    "KRT": "https://i.ibb.co/jZShqBM/Krt24v2.png",
    "GZT": "https://i.ibb.co/9s9YKYT/gzt.png",
    "BENGÜ TÜRK": "https://i.ibb.co/0MHPk8y/benguturk.png",
    "TGRT HABER": "https://i.ibb.co/vJJzR8G/tgrthab22.png",
    "TV NET": "https://i.ibb.co/1RWhvy4/tvnet.png",
    "24": "https://i.ibb.co/PhwYjQ7/24tv.png",
    "FLASH HABER": "https://i.ibb.co/F5FcvbZ/flash4ok.png",
    "ÜLKE": "https://i.ibb.co/ZXts607/ulketv.png",
    "AKIT TV": "https://i.ibb.co/B4XX5Vx/akittv.png",
    "A HABER": "https://i.ibb.co/1X8nWHc/ahaber.png",
    "LİDER HABER TV": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "TÜRK HABER": "https://i.ibb.co/j9Pmc2qN/thhaber.jpg",
    "BUSINESS CHANNEL TÜRK": "https://i.ibb.co/b2b6Zn0/businesschtr.jpg",
    "FİNANS TÜRK": "https://i.ibb.co/GQdBjZfW/finansturk.png",
    "A PARA": "https://i.ibb.co/KwXzY6B/apara.png",
    "CNBC-E": "https://i.ibb.co/kcpSwmK/cnbce.png",
    "TBMM TV": "https://i.ibb.co/BN9tk1q/tbmm22.png",
    "DHA (feed 1)": "https://i.ibb.co/K6BKFqY/dha.png",
    "DHA (feed 2)": "https://i.ibb.co/K6BKFqY/dha.png",
    "AA (feed)": "https://i.ibb.co/jLd8Fcb/aa.png",
    "TRT HABER": "https://i.ibb.co/Bt6frts/trthaber.png",
    "TRT HABER (backup)": "https://i.ibb.co/Bt6frts/trthaber.png",
    "SÖZCÜ TV (backup)": "https://i.ibb.co/B40rjP3/szc1.png",
    "HABER TÜRK (backup)": "https://i.ibb.co/wdwm0fn/haberturk.png",
    "HABER GLOBAL (backup)": "https://i.ibb.co/k58p7P2/hglobal.png",
    "TV 100 (backup)": "https://i.ibb.co/bLpTdYZ/tv100.png",
    "CNN TÜRK (backup)": "https://i.ibb.co/JqWCczW/cnnturk1.png",
    "ULUSAL KANAL (backup)": "https://i.ibb.co/tXdf2YF/ulusal22.png",
    "NTV (backup)": "https://i.ibb.co/9c7MvWX/ntv.png",
    "FLASH HABER (backup)": "https://i.ibb.co/F5FcvbZ/flash4ok.png",
    "EKOL TV (backup)": "https://i.ibb.co/Ln92Dj2/Ekoltv.png",
    "TELE 1 (backup)": "https://i.ibb.co/4Mhmggc/tele1.png",
    "BENGÜ TÜRK (backup)": "https://i.ibb.co/0MHPk8y/benguturk.png",
    "ÜLKE (backup)": "https://i.ibb.co/ZXts607/ulketv.png",
    "A HABER (backup)": "https://i.ibb.co/1X8nWHc/ahaber.png",
    "KRT (backup)": "https://i.ibb.co/jZShqBM/Krt24v2.png",
    "HALK TV (backup)": "https://i.ibb.co/BtYMK4q/halk21a.png",
    "24 (backup)": "https://i.ibb.co/PhwYjQ7/24tv.png",
    "BLOOMBERG HT (backup)": "https://i.ibb.co/HXKrJRC/blght22.png",
    "CNBC-E (backup)": "https://i.ibb.co/kcpSwmK/cnbce.png",
    "TGRT HABER (backup)": "https://i.ibb.co/vJJzR8G/tgrthab22.png",
    "TRT 1": "https://i.ibb.co/d6c87Km/trt122.png",
    "KANAL D": "https://i.ibb.co/s9mVqWH/kanald.png",
    "STAR": "https://i.ibb.co/PmDyTX6/star.jpg",
    "SHOW": "https://i.ibb.co/BrGNZJ4/showtv.png",
    "TV8": "https://i.ibb.co/tXKXNDz/tv8.png",
    "ATV": "https://i.ibb.co/n1SCYqN/atv.png",
    "KANAL 7": "https://i.ibb.co/1s3fHfm/k7tr1.png",
    "BEYAZ TV": "https://i.ibb.co/0tc3PYz/beyaz22b.png",
    "TRT 1 (backup)": "https://i.ibb.co/d6c87Km/trt122.png",
    "KANAL D (backup)": "https://i.ibb.co/s9mVqWH/kanald.png",
    "STAR (backup)": "https://i.ibb.co/DYyDzGV/star22tv.png",
    "SHOW (backup)": "https://i.ibb.co/BrGNZJ4/showtv.png",
    "NOW (backup)": "https://i.ibb.co/0DpKtzT/nowtvturk.png",
    "ATV (backup)": "https://i.ibb.co/n1SCYqN/atv.png",
    "ATV [youtube-src]": "https://i.ibb.co/n1SCYqN/atv.png",
    "ATV [tkn-blocked]": "https://i.ibb.co/n1SCYqN/atv.png",
    "TV8 (backup)": "https://i.ibb.co/tXKXNDz/tv8.png",
    "KANAL 7 (backup)": "https://i.ibb.co/1s3fHfm/k7tr1.png",
    "BEYAZ TV [diedlink]": "https://i.ibb.co/0tc3PYz/beyaz22b.png",
    "TRT 2": "https://i.ibb.co/TB5N8cN/trt2.png",
    "MELTEM TV": "https://i.ibb.co/Fq0ZvYG/meltemtvt.png",
    "TİVİ 6": "https://i.ibb.co/sRNHKjS/tivi622.png",
    "CİNE 1": "https://i.ibb.co/SnPFhXS/cnee12.png",
    "AKILLI TV": "https://i.ibb.co/8dQdNrv/akilli22.png",
    "DMAX": "https://i.ibb.co/QQQR6VK/dmax.png",
    "TLC TR": "https://i.ibb.co/Z1vHy41/tlc.png",
    "360": "https://i.ibb.co/FVnG3Zr/360tv.png",
    "TV 4": "https://i.ibb.co/pXncfpb/tv422.png",
    "TYT TÜRK": "https://i.ibb.co/N2n2tqMz/tyt.png",
    "TÜRKİYE KLİNİKLERİ TV": "https://i.ibb.co/VWRBg1M/trklinik.png",
    "CGTN BELGESEL": "https://i.ibb.co/s9gLmqv/cgtnch.png",
    "SAĞLIK CHANNEL": "https://i.ibb.co/TTwc1rR/saglikch.png",
    "WOMAN KADIN TV": "https://i.ibb.co/DKHDfbr/wmtv.png",
    "WOMAN LIFE TV": "https://i.ibb.co/YQtd480/wlife.jpg",
    "MOR TV": "https://i.ibb.co/qRsfyb2/tvmor.png",
    "CINE5 TV": "https://i.ibb.co/SBhSXwk/Cine5tv.jpg",
    "ONS TV": "https://i.ibb.co/PZW37ch0/onstv.jpg",
    "TEVE 2": "https://i.ibb.co/1Z22dCY/teve2.png",
    "TV8 BUÇUK": "https://i.ibb.co/dgj3MTh/tv85.png",
    "BİZİM EV TV": "https://i.ibb.co/1Ty8Z3X/bizimev.png",
    "SHOW MAX": "https://i.ibb.co/kxjKk89/showmax.png",
    "A2": "https://i.ibb.co/2qrg9QF/a2022.png",
    "FİL TV": "https://i.ibb.co/Zd6fMvZ/filtr.png",
    "YABAN TV": "https://i.ibb.co/rynNr53/yabantv.png",
    "SHOW MAX (backup)": "https://i.ibb.co/kxjKk89/showmax.png",
    "SHOW MAX [tkn-blocked]": "https://i.ibb.co/kxjKk89/showmax.png",
    "A2 (backup)": "https://i.ibb.co/2qrg9QF/a2022.png",
    "A2 [tkn-blocked]": "https://i.ibb.co/2qrg9QF/a2022.png",
    "TEVE 2 (backup)": "https://i.ibb.co/1Z22dCY/teve2.png",
    "TV8 BUÇUK (backup)": "https://i.ibb.co/dgj3MTh/tv85.png",
    "TV8 BUÇUK [tkn-blocked]": "https://i.ibb.co/dgj3MTh/tv85.png",
    "TRT BELGESEL (backup)": "https://i.ibb.co/N1h8m96/trtbelgesel.png",
    "DMAX (backup)": "https://i.ibb.co/QQQR6VK/dmax.png",
    "DMAX [downline]": "https://i.ibb.co/QQQR6VK/dmax.png",
    "TLC TR [downline]": "https://i.ibb.co/Z1vHy41/tlc.png",
    "TLC TR (backup)": "https://i.ibb.co/Z1vHy41/tlc.png",
    "360 [tkn-blocked]": "https://i.ibb.co/FVnG3Zr/360tv.png",
    "360 (backup)": "https://i.ibb.co/FVnG3Zr/360tv.png",
    "WOMAN KADIN TV (backup)": "https://i.ibb.co/DKHDfbr/wmtv.png",
    "TRT DİYANET ÇOCUK": "https://i.ibb.co/qDF8pHQ/tdcc.png",
    "MİNİKA GO (sometimes)": "https://i.ibb.co/R2Zgy7F/minikago.png",
    "MİNİKA ÇOCUK (sometimes)": "https://i.ibb.co/L8ftBdN/minikacocuk.png",
    "CARTOON NETWORK TR": "https://i.ibb.co/Zxd0j45/cartoonnetwork.png",
    "GALATASARAY TV": "https://i.ibb.co/SwwjnF5/gstv.png",
    "FENERBAHÇE TV": "https://i.ibb.co/867fC4z/fbtv22a.png",
    "HT SPOR": "https://i.ibb.co/F0Tsz1v/htsportr.png",
    "A SPOR": "https://i.ibb.co/xSjB51j/aspor.png",
    "BIS HABER": "https://i.ibb.co/BfM21nC/beinhaber.png",
    "SPORTS TV": "https://i.ibb.co/4Rm7Z6Z/sports22.png",
    "TRT SPOR [geo-blocked]": "https://i.ibb.co/3WmLjwG/trtspor22c.png",
    "TRT SPOR2 YILDIZ [geo-blocked]": "https://i.ibb.co/ky3qVPc/trtspory2.png",
    "TABİİ SPOR 1 [geoblocked]": "https://i.ibb.co/YBDCT7q/tabii.png",
    "TABİİ SPOR 2 [geoblocked]": "https://i.ibb.co/YBDCT7q/tabii.png",
    "TABİİ SPOR 3 [geoblocked]": "https://i.ibb.co/YBDCT7q/tabii.png",
    "TABİİ SPOR 4 [geoblocked]": "https://i.ibb.co/YBDCT7q/tabii.png",
    "TABİİ SPOR 5 [geoblocked]": "https://i.ibb.co/YBDCT7q/tabii.png",
    "TABİİ SPOR 6 [geoblocked]": "https://i.ibb.co/YBDCT7q/tabii.png",
    "TJK TV [geo-blocked]": "https://i.ibb.co/0Yt6jbg/tjk.png",
    "TJK TV": "https://i.ibb.co/0Yt6jbg/tjk.png",
    "BY HORSES TV": "https://i.ibb.co/dgpChqK/horses.png",
    "TAY TV": "https://i.ibb.co/J5QjKLt/tay22.png",
    "TRT EBA TV": "https://i.ibb.co/8g20RBH/ebatek.png",
    "MİNİKA ÇOCUK (offline)": "https://i.ibb.co/L8ftBdN/minikacocuk.png",
    "MİNİKA GO (offline)": "https://i.ibb.co/R2Zgy7F/minikago.png",
    "MİNİKA GO (backup)": "https://i.ibb.co/R2Zgy7F/minikago.png",
    "CARTOON NETWORK TR (offline)": "https://i.ibb.co/Zxd0j45/cartoonnetwork.png",
    "MİNİKA GO (backoff)": "https://i.ibb.co/R2Zgy7F/minikago.png",
    "MİNİKA ÇOCUK (backoff)": "https://i.ibb.co/L8ftBdN/minikacocuk.png",
    "HT SPOR (backup)": "https://i.ibb.co/F0Tsz1v/htsportr.png",
    "BIS HABER (backup)": "https://i.ibb.co/BfM21nC/beinhaber.png",
    "TRT SPOR (backup)": "https://i.ibb.co/3WmLjwG/trtspor22c.png",
    "TRT SPOR2 YILDIZ (backup)": "https://i.ibb.co/ky3qVPc/trtspory2.png",
    "TRT3 SPOR [offline]": "https://i.ibb.co/M9kWXzt/trt3spor22c.png",
    "TRT ÇOCUK (backup)": "https://i.ibb.co/YjkMYbF/trtcocuk21a.png",
    "SPORTS TV (backup)": "https://i.ibb.co/4Rm7Z6Z/sports22.png",
    "A SPOR (backup)": "https://i.ibb.co/xSjB51j/aspor.png",
    "A SPOR [tkn-blocked]": "https://i.ibb.co/xSjB51j/aspor.png",
    "SPOTIFY TURKEY • 2025 🎶🎵🎼🎹🪗": "https://i.ibb.co/gdbyhx2/spotify.png",
    "SPOTIFY TURKEY • 2024 🎸🎷🎺🎻🪕": "https://i.ibb.co/gdbyhx2/spotify.png",
    "TRT MÜZİK": "https://i.ibb.co/d6Zfm2P/trtmuzik21c.png",
    "KRAL - KRAL POP": "https://i.ibb.co/6401NQw/kraltv.png",
    "DREAM TÜRK": "https://i.ibb.co/4SsJS4R/dreamturk.png",
    "POWER TÜRK": "https://i.ibb.co/B6N9KsN/powerturk22.png",
    "POWER TÜRK TAPTAZE": "https://i.ibb.co/wy1H8jM/pturkttaze.png",
    "POWER TÜRK SLOW": "https://i.ibb.co/rZxNWKv/pslow.png",
    "POWER TÜRK AKUSTİK": "https://i.ibb.co/FgCW885/pturkakustik.png",
    "TATLISES": "https://i.ibb.co/cQfPfgR/tatlises.png",
    "MİLYON TV": "https://i.ibb.co/Jqzzby7/milyontv.png",
    "NUMBER ONE TÜRK": "https://i.ibb.co/wSPFds2/nr1turk.png",
    "NUMBER ONE TÜRK ASK": "https://i.ibb.co/jJWLsCQ/nr1ask.jpg",
    "NUMBER ONE TÜRK DAMAR": "https://i.ibb.co/824MwJ6/nr1damar.jpg",
    "NUMBER ONE TÜRK DANCE": "https://i.ibb.co/LR5v10B/nr1dance.jpg",
    "NUMBER ONE": "https://i.ibb.co/bQHyST5/nr1tv.png",
    "FASHION ONE": "https://i.ibb.co/9grLJCS/fone22.png",
    "POWER TV": "https://i.ibb.co/xhfcTC7/powertv.png",
    "POWER DANCE": "https://i.ibb.co/FVNL477/pdance.png",
    "POWER LOVE": "https://i.ibb.co/VLQ6cmV/plove.png",
    "NUMBER ONE (backup)": "https://i.ibb.co/bQHyST5/nr1tv.png",
    "KRAL - KRAL POP (backup)": "https://i.ibb.co/6401NQw/kraltv.png",
    "TRT TÜRK": "https://i.ibb.co/swtn1kV/trtturk.png",
    "KANAL 7 AVRUPA": "https://i.ibb.co/cDxKJy1/k7avr1.png",
    "SHOW TÜRK": "https://i.ibb.co/WvhGGP0/showturk1.png",
    "EURO D": "https://i.ibb.co/THj0Jrg/eurod22.png",
    "EURO D (geçici geçerli)": "https://i.ibb.co/THj0Jrg/eurod22.png",
    "EURO STAR": "https://i.ibb.co/Lg90xsB/eurostar22.png",
    "EURO STAR (geçici geçerli)": "https://i.ibb.co/Lg90xsB/eurostar22.png",
    "ATV AVRUPA (geçici geçerli)": "https://i.ibb.co/PtH4wGr/atvavr.png",
    "TV8 INT (geçici geçerli)": "https://i.ibb.co/n7Jy3h5/tv8int22.png",
    "TGRT EU": "https://i.ibb.co/MCXCRcn/tgrteu1.png",
    "AGRO TV": "https://i.ibb.co/1RnLJpf/agro.png",
    "ÇİFTÇİ TV": "https://i.ibb.co/vHwMgx0/ciftci.png",
    "TARIM TV": "https://i.ibb.co/tDB51ww/tarim.png",
    "YOL TV": "https://i.ibb.co/hB9yNXV/yol22.png",
    "KANAL B": "https://i.ibb.co/X7zxL8v/knlb.png",
    "EM TV": "https://i.ibb.co/Sc4DY66/emtv.webp",
    "DİYANET TV": "https://i.ibb.co/k9phm3v/diyanettv.png",
    "SEMERKAND": "https://i.ibb.co/k8L3Mq1/semerkandtv.png",
    "SEMERKAND WAY": "https://i.ibb.co/k8L3Mq1/semerkandtv.png",
    "DOST TV": "https://i.ibb.co/jwgqtSB/dosttv.png",
    "REHBER TV": "https://i.ibb.co/tHfxLTn/rehbertv.png",
    "LALEGÜL TV": "https://i.ibb.co/wrL2khn/lalegul.png",
    "BERAT TV": "https://i.ibb.co/yN9HKJ6/berrat.png",
    "VAV TV": "https://i.ibb.co/bj1H8LCm/vavtv.png",
    "CAN TV": "https://i.ibb.co/FX1SqtR/cantv.jpg",
    "ON4 TV": "https://i.ibb.co/6B8M20v/on422.png",
    "AFRO TURK TV": "https://i.ibb.co/DMRJYJM/afroturk.png",
    "LUYS TV": "https://i.ibb.co/KjLpH6t/luys.png",
    "SAT 7 TÜRK": "https://i.ibb.co/Cm1kp8f/sat7turk.png",
    "KANAL HAYAT": "https://i.ibb.co/1qFR0jX/Kanalhayat.png",
    "ABN TURKEY": "https://i.ibb.co/ChhQT8b/Abn.png",
    "TGRT BELGESEL": "https://i.ibb.co/JHH0xcX/tgrtbel22.png",
    "TGRT EU (backup)": "https://i.ibb.co/MCXCRcn/tgrteu1.png",
    "TGRT BELGESEL (backup)": "https://i.ibb.co/JHH0xcX/tgrtbel22.png",
    "TGRT BELGESEL (checkalt)": "https://i.ibb.co/JHH0xcX/tgrtbel22.png",
    "KANAL 7 AVRUPA [off-link]": "https://i.ibb.co/cDxKJy1/k7avr1.png",
    "KANAL 7 AVRUPA (backup)": "https://i.ibb.co/cDxKJy1/k7avr1.png",
    "ATV AVRUPA (backoff)": "https://i.ibb.co/PtH4wGr/atvavr.png",
    "SHOW TÜRK (geçici geçerli)": "https://i.ibb.co/WvhGGP0/showturk1.png",
    "AKSU TV KAHRAMANMARAŞ": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "ALANYA POSTA TV": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "ALANYA TV": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "ALTAS TV ORDU": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "ART AMASYA": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "AS TV BURSA": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "BARTIN TV": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "BEYKENT TV": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "BİR TV İZMİR": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "BRTV KARABÜK": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "BURSA LINE TV": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "BURSA ON6 TV": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "BÜLTEN TV ANKARA": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "ÇAY TV RİZE": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "ÇEKMEKÖY BELEDİYE TV": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "ÇORUM BLD TV": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "DEHA TV DENİZLİ": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "DENİZ POSTASI TV": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "DİM TV ALANYA": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "DİYAR TV": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "DRT DENİZLİ": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "DÜĞÜN TV ÇİNE": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "EDESSA TV ŞANLIURFA": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "EGE MAX İZMİR": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "EGE LIVE TV": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "ELMAS TV ZONGULDAK": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "ER TV MALATYA": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "ERCİS TV": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "ERCİYES TV": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "ERT ŞAH TV ERZİNCAN": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "ERZURUM WEB TV": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "ES TV ESKİŞEHİR": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "EDİRNE TV": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "EFES DOST TV": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "ESENLER ŞEHİR TV": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "ETV KAYSERİ": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "FRT FETHİYE": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "GRT GAZİANTEP TV": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "GÜNEY TV TARSUS": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "GÜNEYDOĞU TV": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "GURBET 24 TV": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "HEDEF TV KOCAELİ": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "HABER61 TRABZON": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "HRT HATAY AKDENİZ": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "HUNAT TV KAYSERİ": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "İÇEL TV MERSİN": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "İZMİR TIME 35 TV": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "İZMİR TÜRK TV": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "KANAL 15 BURDUR": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "KANAL 19 ÇORUM": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "KANAL 23 ELAZIĞ": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "KANAL 26 ESKİŞEHİR": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "KANAL 3 AFYONKARAHİSAR": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "KANAL 32 ISPARTA": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "KANAL 33 MERSİN": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "KANAL 34 İSTANBUL": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "KANAL 53 RİZE": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "KANAL 56 SİİRT": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "KANAL 58 SİVAS": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "KANAL 68 AKSARAY": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "KANAL EGE": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "KANAL FIRAT": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "KANAL S SAMSUN": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "KANAL URFA": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "KANAL V ANTALYA": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "KANAL Z ZONGULDAK": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "KASTAMONU TV": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "KARABÜK DERİN TV": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "KARDELEN TV": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "KAY TV KAYSERİ": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "K+ KAYSERİ": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "KEÇİÖREN TV ANKARA": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "KENT 38 TV KAYSERİ": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "KENT TV BODRUM": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "KOCAELİ TV": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "KONYA KTV": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "KONYA OLAY TV": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "KOZA TV ADANA": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "LIFE TV KAYSERİ": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "MALATYA VUSLAT TV": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "MANISA ETV": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "MARMARİS TV": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "MERCAN TV ADIYAMAN": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "METROPOL DENİZLİ": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "MUĞLA MERKEZ TV": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "MUĞLA TÜRK TV": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "NOKTA TV KOCAELİ": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "NORA TV AKSARAY": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "OGUN TV": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "OLAY TÜRK KAYSERİ TV": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "OLAY TV BURSA": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "ORDU BEL TV": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "ORT OSMANİYE TV": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "PAMUKKALE TV": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "POSTA TV ALANYA": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "RADYO KARDEŞ TV FR": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "RİZE TÜRK TV": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "SARIYER TV İST": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "SILKWAY KAZAKH (TUR)": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "SİNOP YILDIZ TV": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "SKYHABER TV": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "SLOW KARADENİZ TV": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "SUN RTV MERSİN": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "RUMELİ TV": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "TEK RUMELİ TV": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "TEMPO TV": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "TV 1 ADANA": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "TV 3 AFYONKARAHİSAR": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "TİVİ TURK": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "TON TV ÇANAKKALE": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "TOKAT TV": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "TRABZON TV": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "TRAKYA TÜRK": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "TURHAL WEB TV": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "TV KAYSERİ": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "TV 1 KAYSERİ": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "TV 25 DOĞU": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "TV 264 SAKARYA": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "TV 35 İZMİR": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "TV 41 KOCAELİ": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "TV 48 MİLAS": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "TV 52 ORDU": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "TVO ANTALYA": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "TV DEN AYDIN": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "TÜRKMENELİ TV": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "UR FANATİK TV": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "ÜSKÜDAR UNİVERSİTE TV": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "VAN GÖLÜ TV": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "VİYANA TV": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "YAŞAM TV": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "WORLD TÜRK TV": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "YOZGAT BLD TV": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "YILDIZ TV": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "BRÜKSEL TÜRK": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "BALKAN TÜRK": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "KANAL AVRUPA": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "GURME TV": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "EZGİ TV": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "*ESKİ TÜRKİYE* - NOSTALJİ TV KANALLAR...": "https://i.ibb.co/mHt7rQf/Tryerel.png",
    "BRT 1": "https://i.ibb.co/y8p46cM/Kktc.png",
    "BRT 2": "https://i.ibb.co/y8p46cM/Kktc.png",
    "ADA TV": "https://i.ibb.co/y8p46cM/Kktc.png",
    "KANAL T": "https://i.ibb.co/y8p46cM/Kktc.png",
    "GENÇ TV": "https://i.ibb.co/y8p46cM/Kktc.png",
    "KIBRIS TV": "https://i.ibb.co/y8p46cM/Kktc.png",
    "SİM TV": "https://i.ibb.co/y8p46cM/Kktc.png",
    "TV 2020": "https://i.ibb.co/y8p46cM/Kktc.png",
    "KK TV": "https://i.ibb.co/y8p46cM/Kktc.png",
    "ZAROK KURMANÎ": "https://i.ibb.co/cXd3MBV/symkr.png",
    "ZAROK SORANÎ": "https://i.ibb.co/cXd3MBV/symkr.png",
    "ZAROK": "https://i.ibb.co/cXd3MBV/symkr.png",
    "TRT KURDÎ": "https://i.ibb.co/cXd3MBV/symkr.png",
    "ZAGROS TV": "https://i.ibb.co/cXd3MBV/symkr.png",
    "KURDMAX SHOW": "https://i.ibb.co/cXd3MBV/symkr.png",
    "KURDMAX SORANÎ": "https://i.ibb.co/cXd3MBV/symkr.png",
    "KURDMAX MUSIC": "https://i.ibb.co/cXd3MBV/symkr.png",
    "RÛDAW TV": "https://i.ibb.co/cXd3MBV/symkr.png",
    "ROJAVA TV": "https://i.ibb.co/cXd3MBV/symkr.png",
    "KURD CHANNEL": "https://i.ibb.co/cXd3MBV/symkr.png",
    "KURDISTAN 24": "https://i.ibb.co/cXd3MBV/symkr.png",
    "KURDISTAN TV": "https://i.ibb.co/cXd3MBV/symkr.png",
    "KURDSAT": "https://i.ibb.co/cXd3MBV/symkr.png",
    "KURDSAT NEWS": "https://i.ibb.co/cXd3MBV/symkr.png",
    "GELÎ KURDISTAN TV": "https://i.ibb.co/cXd3MBV/symkr.png",
    "KOMALA TV": "https://i.ibb.co/cXd3MBV/symkr.png",
    "JÎN TV": "https://i.ibb.co/cXd3MBV/symkr.png",
    "CÎHAN TV": "https://i.ibb.co/cXd3MBV/symkr.png",
    "ERT NEWS": "https://i.ibb.co/qNZ259D/ertnews.png",
    "ERT NEWS 2": "https://i.ibb.co/kc1Dy1d/ertnews2.png",
    "ERT NEWS 3": "https://i.ibb.co/kx3g5tM/ertnews3.png",
    "ERT 1": "https://i.ibb.co/YDX83ph/ert1.png",
    "ERT 2": "https://i.ibb.co/bL4sJLW/ert2.png",
    "ERT 3": "https://i.ibb.co/BjHZT7x/ert3.png",
    "ERT SPORTS 1": "https://i.ibb.co/PGvP32M/ertsports1.png",
    "ERT SPORTS 2": "https://i.ibb.co/HYMZh7V/ertsports2.png",
    "ERT SPORTS 3": "https://i.ibb.co/pPkt9Yg/ertsports3.png",
    "ERT SPORTS 4": "https://i.ibb.co/KYrkMLk/ertsports4.png",
    "ERT KIDS": "https://i.ibb.co/zbvFC65/ertkids.jpg",
    "ERT MUSIC": "https://i.ibb.co/c8NJjxh/ertmusic.jpg",
    "ALPHA TV": "https://i.ibb.co/480p4sv/alpha.png",
    "ANT 1": "https://i.ibb.co/qk1SMGf/ant1.jpg",
    "SKAI": "https://i.ibb.co/df2r3NS/skai.jpg",
    "MEGA": "https://i.ibb.co/y6D9CPT/megagr.png",
    "MEGA PLAY": "https://i.ibb.co/y6D9CPT/megagr.png",
    "MEGA NEWS": "https://i.ibb.co/ynxKwfdR/meganews.png",
    "MAK TV": "https://i.ibb.co/B2Xxhty/mak.png",
    "NETMAX TV": "https://i.ibb.co/B6hwDfS/netmax.jpg",
    "OPEN TV": "https://i.ibb.co/8bgKVyb/openbyd.png",
    "ATTICA": "https://i.ibb.co/xq8t3P5/attica.jpg",
    "SIGMA TV": "https://i.ibb.co/sPtkhnL/sigma.png",
    "MAGIC TV": "https://i.ibb.co/txd3r3P/magic.png",
    "MAKEDONIA TV": "https://i.ibb.co/Gs4djtL/makedonia.png",
    "NET TV TORONTO": "https://i.ibb.co/tQmhZ0K/netmax.png",
    "NET TV EUROPE": "https://i.ibb.co/tQmhZ0K/netmax.png",
    "NET MAX TV": "https://i.ibb.co/tQmhZ0K/netmax.png",
    "ANT 1 COMEDY": "https://i.ibb.co/qk1SMGf/ant1.jpg",
    "ANT 1 DRAMA": "https://i.ibb.co/qk1SMGf/ant1.jpg",
    "ANT 1 MUSIC": "https://i.ibb.co/qk1SMGf/ant1.jpg",
    "MAD WORLD": "https://i.ibb.co/W5DZtvt/madtv.png",
    "OMEGA": "https://i.ibb.co/TPGzY4C/omega.png",
    "RIK SAT CYPRUS": "https://i.ibb.co/3sHp7pS/riksat.png",
    "RIK 1": "https://i.ibb.co/3sHp7pS/riksat.png",
    "RIK 2": "https://i.ibb.co/3sHp7pS/riksat.png",
    "RIK HD": "https://i.ibb.co/3sHp7pS/riksat.png",
    "ACTION 24": "https://i.ibb.co/56kWP6F/action24.png",
    "GROOVY TV": "https://i.ibb.co/1qXMwq2/groovy.png",
    "SKAI BIG BROTHER": "https://i.ibb.co/3m2fYyYw/skaibb.jpg",
    "NEA CRETE TV": "https://i.ibb.co/0DDXv93/nea.png",
    "BARAZA RELAXING TV": "https://i.ibb.co/b2mBMBk/baraza.jpg",
    "XALASTRA TV": "https://i.ibb.co/72657Kw/xalastra.jpg",
    "NRG TV": "https://i.ibb.co/z6zPQL8/nrg.png",
    "BOYAH TV - KANALI VOULIS": "https://i.ibb.co/L9fj1Hj/greece.png",
    "AEOLOS": "https://i.ibb.co/L9fj1Hj/greece.png",
    "EXPLORE": "https://i.ibb.co/L9fj1Hj/greece.png",
    "TOP CHANNEL": "https://i.ibb.co/L9fj1Hj/greece.png",
    "ράκη Νετ TV": "https://i.ibb.co/L9fj1Hj/greece.png",
    "TELE ΚΡΗΤΗ": "https://i.ibb.co/L9fj1Hj/greece.png",
    "START TV": "https://i.ibb.co/L9fj1Hj/greece.png",
    "PELLA TV": "https://i.ibb.co/L9fj1Hj/greece.png",
    "KONTRA TV": "https://i.ibb.co/L9fj1Hj/greece.png",
    "HIGH TV": "https://i.ibb.co/L9fj1Hj/greece.png",
    "HELLENIC TV": "https://i.ibb.co/L9fj1Hj/greece.png",
    "GREEK TV LONDON": "https://i.ibb.co/L9fj1Hj/greece.png",
    "GRD CHANNEL": "https://i.ibb.co/L9fj1Hj/greece.png",
    "CRETA": "https://i.ibb.co/L9fj1Hj/greece.png",
    "CORFU": "https://i.ibb.co/L9fj1Hj/greece.png",
    "BLUE SKY": "https://i.ibb.co/L9fj1Hj/greece.png",
    "RED MUSIC": "https://i.ibb.co/L9fj1Hj/greece.png",
    "BARAZA TV": "https://i.ibb.co/L9fj1Hj/greece.png",
    "10 CHANNEL": "https://i.ibb.co/L9fj1Hj/greece.png",
    "ERT WORLD (backup)": "https://i.ibb.co/vQZKgNX/ertworld.png",
    "ERT NEWS (backup)": "https://i.ibb.co/qNZ259D/ertnews.png",
    "ERT SPORTS 1 (backup)": "https://i.ibb.co/PGvP32M/ertsports1.png",
    "ERT SPORTS 2 (backup)": "https://i.ibb.co/HYMZh7V/ertsports2.png",
    "ERT SPORTS 3 (backup)": "https://i.ibb.co/pPkt9Yg/ertsports3.png",
    "ERT SPORTS 4 (backup)": "https://i.ibb.co/KYrkMLk/ertsports4.png",
    "ERT MUSIC (backup)": "https://i.ibb.co/c8NJjxh/ertmusic.jpg",
    "ERT KIDS (backup)": "https://i.ibb.co/zbvFC65/ertkids.jpg",
    "RIK SAT CYPRUS (backup)": "https://i.ibb.co/3sHp7pS/riksat.png",
    "SIC": "https://i.ibb.co/6r1xHn6/sic.png",
    "RTP INTERNACIONAL": "https://i.ibb.co/SPR2SDK/RTP.png",
    "CNN PORTUGAL": "https://i.ibb.co/XbSHxd5/cnn.png",
    "SIC NOTÍCIAS": "https://i.ibb.co/1QHfvZJ/sicnoc.png",
    "EURONEWS PT": "https://i.ibb.co/VxLFYSj/euronews.png",
    "TVI INT": "https://i.ibb.co/pyXp0bk/tvi.png",
    "TVI V+": "https://i.ibb.co/gDFmb2z/vplustvi.png",
    "TVI FICCAO": "https://i.ibb.co/hg8wkqj/tvific.jpg",
    "TVI REALITY": "https://i.ibb.co/xYNTr2v/tvirea.jpg",
    "SIC NOVELAS": "https://i.ibb.co/dJZR1gD/sicnov.png",
    "SIC REPLAY": "https://i.ibb.co/W2dzvHS/sicreplay.png",
    "SIC HD ALTA DEFINIÇÃO": "https://i.ibb.co/M2g53rQ/sichdad.png",
    "PORTO CANAL": "https://i.ibb.co/WVzhVbc/portoc.png",
    "TVI AFRICA": "https://i.ibb.co/vvRXDTV/tviafrica.jpg",
    "AR PARLAMENTO": "https://i.ibb.co/zZwMM3d/arparl.png",
    "ADB TV": "https://i.ibb.co/V3Hk3KC/adb.png",
    "MCA": "https://i.ibb.co/DCzRYjV/mca.png",
    "FAMA FM TV": "https://i.ibb.co/RpQj4Dd/fama.png",
    "KURIAKOS TV": "https://i.ibb.co/cX8tGgsv/Kuriakos.png",
    "KURIAKOS MUSIC": "https://i.ibb.co/KxXJddKf/Kuriakosmsc.png",
    "KURIAKOS CINE": "https://i.ibb.co/TcpshFx/kuricine.png",
    "KURIAKOS KIDS": "https://i.ibb.co/B2YCsC0/kurikids.png",
    "TRACE BRAZUCA": "https://i.ibb.co/fk0Vttj/tracebraz.png",
    "RTP 1 (backup sd)": "https://i.ibb.co/3YZFCjp/rtp1.jpg",
    "RTP 2 (backup sd)": "https://i.ibb.co/tbFT1V2/rtp2.jpg",
    "RTP 3 (backup sd)": "https://i.ibb.co/HnqCkQj/rtp3.jpg",
    "RTP 3 (tvhlsdvr)": "https://i.ibb.co/HnqCkQj/rtp3.jpg",
    "RTP 3 (tvhlsdvr_HD)": "https://i.ibb.co/HnqCkQj/rtp3.jpg",
    "RTP ACORES (backup)": "https://i.ibb.co/9GMzcw7/rtpaco.jpg",
    "EURONEWS PT (backup)": "https://i.ibb.co/VxLFYSj/euronews.png",
    "CNN PORTUGAL (backup)": "https://i.ibb.co/XbSHxd5/cnn.png",
    "SIC NOTÍCIAS (backup)": "https://i.ibb.co/1QHfvZJ/sicnoc.png",
    "SIC NOVELAS (backup)": "https://i.ibb.co/dJZR1gD/sicnov.png",
    "TVI V+ (ex-TVI FICCAO)": "https://i.ibb.co/gDFmb2z/vplustvi.png",
    "CNN PORTUGAL [find-host]": "https://i.ibb.co/XbSHxd5/cnn.png",
    "TVI [find-host]": "https://i.ibb.co/pyXp0bk/tvi.png",
    "TVI INT [find-host]": "https://i.ibb.co/pyXp0bk/tvi.png",
    "CNN PORTUGAL [tkn-blocked]": "https://i.ibb.co/XbSHxd5/cnn.png",
    "TVI [tkn-blocked]": "https://i.ibb.co/pyXp0bk/tvi.png",
    "TVI INT [tkn-blocked]": "https://i.ibb.co/pyXp0bk/tvi.png",
    "TVI FICCAO [tkn-blocked]": "https://i.ibb.co/hg8wkqj/tvific.jpg",
    "TVI REALITY [tkn-blocked]": "https://i.ibb.co/xYNTr2v/tvirea.jpg",
    "SIC NOVELAS [offline]": "https://i.ibb.co/dJZR1gD/sicnov.png",
    "TVE INTERNACIONAL": "https://i.ibb.co/ypn5DBD/tveint.png",
    "TVE LA 1": "https://i.ibb.co/VM5vGBV/la1.jpg",
    "TVE LA 2": "https://i.ibb.co/ssGmhbH/la2.jpg",
    "TVE 24 H": "https://i.ibb.co/fqg1vfr/24h.png",
    "STAR TVE": "https://i.ibb.co/3T2TS2p/tvestar.jpg",
    "TVE TDP": "https://i.ibb.co/D1Djbfj/tdp.jpg",
    "TVE CLAN": "https://i.ibb.co/BGy5vM5/clan.jpg",
    "ANTENA 3": "https://i.ibb.co/hYTkm8L/A3es.png",
    "CUATRO": "https://i.ibb.co/hRs6WrH/C4es.png",
    "TELECINCO": "https://i.ibb.co/7gMg1nb/t5es.png",
    "LA SEXTA": "https://i.ibb.co/6JF4BK4/l6es.png",
    "TVE SOMOS CINE [geo-limited]": "https://i.ibb.co/99kVf9W/somoscine.png",
    "RNE PARA TODOS": "https://i.ibb.co/SRbKtLk/rtve.png",
    "RTVE PLAY CADENA 1": "https://i.ibb.co/SRbKtLk/rtve.png",
    "RTVE PLAY CADENA 2": "https://i.ibb.co/SRbKtLk/rtve.png",
    "RTVE PLAY CADENA 3": "https://i.ibb.co/SRbKtLk/rtve.png",
    "RTVE PLAY CADENA 4": "https://i.ibb.co/SRbKtLk/rtve.png",
    "RTVE": "https://i.ibb.co/SRbKtLk/rtve.png",
    "EURONEWS ES": "https://i.ibb.co/VxLFYSj/euronews.png",
    "EL PAIS": "https://i.ibb.co/cQwqfFC/ees.jpg",
    "EL CONFIDENCIAL TV": "https://i.ibb.co/tMVTj53/elconf.jpg",
    "CANAL PARLAMENTO": "https://i.ibb.co/8xh76zN/parl.jpg",
    "CANAL DIPUTADOS": "https://i.ibb.co/8xh76zN/parl.jpg",
    "SOL MÙSICA": "https://i.ibb.co/TthjhJ6/solmusica.png",
    "TRECE INT": "https://i.ibb.co/GsLm5g5/trece.png",
    "TRECE": "https://i.ibb.co/GsLm5g5/trece.png",
    "ATRES SERIES": "https://i.ibb.co/bKLFcnD/a3cine.png",
    "ATRES CLÁSICOS": "https://i.ibb.co/h17Kt3g/fastatres.jpg",
    "ATRES COMEDIA": "https://i.ibb.co/h17Kt3g/fastatres.jpg",
    "ATRES FLOOXER": "https://i.ibb.co/h17Kt3g/fastatres.jpg",
    "ATRES MULTICINE": "https://i.ibb.co/h17Kt3g/fastatres.jpg",
    "ATRES KIDZ": "https://i.ibb.co/h17Kt3g/fastatres.jpg",
    "ATRES INQUIETOS": "https://i.ibb.co/h17Kt3g/fastatres.jpg",
    "PEQUE TV": "https://i.ibb.co/GJ3Qw6b/peque.jpg",
    "CARTOON NETWORK ES": "https://i.ibb.co/Zxd0j45/cartoonnetwork.png",
    "VIVE KANAL D DRAMA": "https://i.ibb.co/nLcKDkX/ddrama.png",
    "TRACE LATINA": "https://i.ibb.co/vvhRkHZ/tracelatina.png",
    "REAL MADRID CINEVERSE": "https://i.ibb.co/bNm7D0p/rlmdrd.png",
    "REAL MADRID TV": "https://i.ibb.co/bNm7D0p/rlmdrd.png",
    "EL TORO TV": "https://i.ibb.co/NLVj121/eltoro.png",
    "SUR 1 ANDALUCÍA": "https://i.ibb.co/Qb7LPVN/andartv.png",
    "SUR 2 ANDALUCÍA": "https://i.ibb.co/Pt5ThHQ/andatv.png",
    "SUR NOTICIAS ANDALUCÍA": "https://i.ibb.co/gWcDxx9/csnan.png",
    "CINE ANDALUCÍA": "https://i.ibb.co/0Q8h8MG/andacine.png",
    "COCINA ANDALUCÍA": "https://i.ibb.co/LrnwFnz/andacocina.png",
    "TURISMO ANDALUCÍA": "https://i.ibb.co/hHKKnt3/andaturismo.png",
    "ARAGÓN TV": "https://i.ibb.co/MkBCwH4/arag.png",
    "ARAGÓN NOTICIAS": "https://i.ibb.co/B4RNJb6/aragonot.jpg",
    "LA 1 CANARIAS": "https://i.ibb.co/VM5vGBV/la1.jpg",
    "LA 2 CANARIAS": "https://i.ibb.co/ssGmhbH/la2.jpg",
    "24 H CANARIAS": "https://i.ibb.co/fqg1vfr/24h.png",
    "CASTILLA MEDIA": "https://i.ibb.co/N7tznnD/cmm.jpg",
    "LA 1 CATALUNYA": "https://i.ibb.co/VM5vGBV/la1.jpg",
    "LA 2 CATALUNYA": "https://i.ibb.co/ssGmhbH/la2.jpg",
    "24 H CATALUNYA": "https://i.ibb.co/fqg1vfr/24h.png",
    "TV3 CATALUNYA INT": "https://i.ibb.co/xmGNS4w/tvcata.jpg",
    "TV3 CATALUNYA CAT": "https://i.ibb.co/xmGNS4w/tvcata.jpg",
    "TV3 CATALUNYA ES": "https://i.ibb.co/xmGNS4w/tvcata.jpg",
    "TV3 CATALUNYA 24H": "https://i.ibb.co/xmGNS4w/tvcata.jpg",
    "TV3 CATALUNYA FAST 1": "https://i.ibb.co/xmGNS4w/tvcata.jpg",
    "TV3 CATALUNYA FAST 2": "https://i.ibb.co/xmGNS4w/tvcata.jpg",
    "TV3 CATALUNYA LOC": "https://i.ibb.co/xmGNS4w/tvcata.jpg",
    "TV3 CATALUNYA C33": "https://i.ibb.co/xmGNS4w/tvcata.jpg",
    "CATALUNYA BON DIA TV": "https://i.ibb.co/2F2XDFd/bondia.png",
    "CATALUNYA 4 TV": "https://i.ibb.co/tM7BJP1/cata4.jpg",
    "INFOCIUDADES TV CATALUNYA": "https://i.ibb.co/hB1Y74S/infocat.jpg",
    "TENERIFE 4": "https://i.ibb.co/crzKf1n/tenerife4.jpg",
    "MELILLA TV": "https://i.ibb.co/zxnPhtW/melilla.png",
    "CEUTA RTV": "https://i.ibb.co/HKFVwnt/ceum.jpg",
    "HUELVA TV": "https://i.ibb.co/PGd1Sj9H/huelva.jpg",
    "TELE MADRID": "https://i.ibb.co/QnMxFJD/madr.jpg",
    "TELE MADRID INT": "https://i.ibb.co/QnMxFJD/madr.jpg",
    "TELE MADRID OTRA": "https://i.ibb.co/QnMxFJD/madr.jpg",
    "TELE ONDE MADRID": "https://i.ibb.co/QnMxFJD/madr.jpg",
    "CANAL EXTRAMADURA": "https://i.ibb.co/6RYq1MS/extram.png",
    "TVG GALICIA EU": "https://i.ibb.co/LtG0fMD/galic.jpg",
    "TVG GALICIA AM": "https://i.ibb.co/LtG0fMD/galic.jpg",
    "TVG GALICIA MO": "https://i.ibb.co/LtG0fMD/galic.jpg",
    "TVG CULTURAL": "https://i.ibb.co/LtG0fMD/galic.jpg",
    "TVG INFANTIL": "https://i.ibb.co/LtG0fMD/galic.jpg",
    "TVG 2": "https://i.ibb.co/LtG0fMD/galic.jpg",
    "EITB 1": "https://i.ibb.co/FhXvbPN/eitb.jpg",
    "EITB 2": "https://i.ibb.co/FhXvbPN/eitb.jpg",
    "EITB INT": "https://i.ibb.co/FhXvbPN/eitb.jpg",
    "EITB DEPORTE": "https://i.ibb.co/56TvMjR/etbs.jpg",
    "ANDORRA DIFUSIÓ": "https://i.ibb.co/ySq76W3/rtva.png",
    "TV CANARIA": "https://i.ibb.co/0rxVFbs/tvcanaria.png",
    "TV RIOJA": "https://i.ibb.co/2dHP72G/tvrioja.jpg",
    "RIOJA COCINA": "https://i.ibb.co/2dHP72G/tvrioja.jpg",
    "101TV SEVILLA": "https://i.ibb.co/3yvX74m/101sevilla.jpg",
    "TELESUR": "https://i.ibb.co/NCQtNX5/telesur.png",
    "FRANCE 24 ES": "https://i.ibb.co/hKP8X8B/f24.png",
    "DW ESPAÑOL": "https://i.ibb.co/84XLZJq/dw.png",
    "NHK WORLD ESP": "https://i.ibb.co/JCjsXZm/nhk.png",
    "CGTN ESPAÑOL": "https://i.ibb.co/CH8JGfJ/cgtnes.png",
    "PRESS HISPAN TV": "https://i.ibb.co/pRYF5QL/hispantv.png",
    "CNN EN ESPAÑOL [geoblocked]": "https://i.ibb.co/XbSHxd5/cnn.png",
    "RT ESPAÑOL [censure-blocked]": "https://i.ibb.co/D7w9h7Q/rt.png",
    "FRANCE 24 ES (backup)": "https://i.ibb.co/hKP8X8B/f24.png",
    "EURONEWS ES (backup)": "https://i.ibb.co/VxLFYSj/euronews.png",
    "TVE LA 1 (backup)": "https://i.ibb.co/VM5vGBV/la1.jpg",
    "TVE LA 2 (backup)": "https://i.ibb.co/ssGmhbH/la2.jpg",
    "TVE 24 H (backup)": "https://i.ibb.co/fqg1vfr/24h.png",
    "TVE INTERNACIONAL (backup)": "https://i.ibb.co/ypn5DBD/tveint.png",
    "TVE INTERNACIONAL (america)": "https://i.ibb.co/ypn5DBD/tveint.png",
    "TVE SOMOS CINE (backup)": "https://i.ibb.co/99kVf9W/somoscine.png",
    "STAR TVE (espana)": "https://i.ibb.co/3T2TS2p/tvestar.jpg",
    "ANTENA 3 (backup)": "https://i.ibb.co/hYTkm8L/A3es.png",
    "CUATRO (backup)": "https://i.ibb.co/hRs6WrH/C4es.png",
    "TELECINCO (backup)": "https://i.ibb.co/7gMg1nb/t5es.png",
    "LA SEXTA (backup)": "https://i.ibb.co/6JF4BK4/l6es.png",
    "TVE CLAN [geo-restricted]": "https://i.ibb.co/BGy5vM5/clan.jpg",
    "TENERIFE 4 (offlink)": "https://i.ibb.co/crzKf1n/tenerife4.jpg",
    "TELE MADRID (offlink)": "https://i.ibb.co/QnMxFJD/madr.jpg",
    "Al AOULA INT الأولى": "https://i.ibb.co/n0Pwp2S/alaoulainter.png",
    "ARRYADIA الرياضية": "https://i.ibb.co/Wk8BWg4/arryadia.png",
    "ATHAQAFIA الثقافية": "https://i.ibb.co/k8gk0Hb/arrabiaa.png",
    "AL MAGHRIBIA المغربية الإخبارية": "https://i.ibb.co/5kp5CmP/almaghribia.png",
    "ASSADISSA القرآن الكريم": "https://i.ibb.co/Gxn4XrB/assadissa.png",
    "TAMAZIGHT الأمازيغية": "https://i.ibb.co/rmRc08Z/tamazight.png",
    "MEDI 1 MG العربية": "https://i.ibb.co/rQJcGTc/medi1tv.png",
    "MEDI 1 AR العربية": "https://i.ibb.co/rQJcGTc/medi1tv.png",
    "MEDI 1 FR العربية": "https://i.ibb.co/rQJcGTc/medi1tv.png",
    "CHADA TV شدى": "https://i.ibb.co/pdd2VqB/chada.jpg",
    "WATANIA 1": "https://i.ibb.co/5M4CwmQ/watania1.png",
    "WATANIA 2": "https://i.ibb.co/TM8sRjr/watanya-2.png",
    "ATTASIA 9": "https://i.ibb.co/8DxdBPf/Attessia9.png",
    "NESSMA": "https://i.ibb.co/stZxQHF/nessma.png",
    "TV2 ALGÉRIE": "https://i.ibb.co/9tsD8WP/TV2Al.png",
    "ECHOROUK TV DZ": "https://i.ibb.co/yQmcHjz/echourouk.png",
    "ECHOROUK NEWS DZ": "https://i.ibb.co/1vH6q4L/echounws.png",
    "EL HAYAT DZ": "https://i.ibb.co/7Q4Zv2v/elhayat.png",
    "CNA": "https://i.ibb.co/H4N2sNS/cna.png",
    "WATANIA 1 (backup)": "https://i.ibb.co/5M4CwmQ/watania1.png",
    "WATANIA 2 (backup)": "https://i.ibb.co/TM8sRjr/watanya-2.png",
    "CHADA TV شدى (backup)": "https://i.ibb.co/pdd2VqB/chada.jpg",
    "MEDI 1 MG العربية (backup)": "https://i.ibb.co/rQJcGTc/medi1tv.png",
    "MEDI 1 AR العربية (backup)": "https://i.ibb.co/rQJcGTc/medi1tv.png",
    "MEDI 1 FR العربية (backup)": "https://i.ibb.co/rQJcGTc/medi1tv.png",
    "MEDI 1 MG العربية (off-backup)": "https://i.ibb.co/rQJcGTc/medi1tv.png",
    "2M MONDE (n/f) الثانية": "https://i.ibb.co/dp5Z2dh/2m.png",
    "HELWA": "https://i.ibb.co/JmRh3Xn/helwa.png",
    "SAMIRA": "https://i.ibb.co/HzvjJq6/samira.png",
    "ECHOROUK NEWS": "https://i.ibb.co/1vH6q4L/echounws.png",
    "ECHOROUK NEWS (backup)": "https://i.ibb.co/1vH6q4L/echounws.png",
    "ECHOROUK TV": "https://i.ibb.co/yQmcHjz/echourouk.png",
    "EL BILAD": "https://i.ibb.co/ByPHXnt/bilad.png",
    "TV2 ALGERIE [hta_dz-off]": "https://i.ibb.co/9tsD8WP/TV2Al.png",
    "TV1 ENTV [hta_dz-off]": "https://i.ibb.co/xY39PSC/TV1-ENTV.png",
    "TV3 ALGERIE [hta_dz-off]": "https://i.ibb.co/qR3CZP8/tv3al.png",
    "TV4 ALGERIE [hta_dz-off]": "https://i.ibb.co/4tmp0NH/tv4al.png",
    "TV5 ALGERIE [hta_dz-off]": "https://i.ibb.co/SXjJGYZ/tv5al.png",
    "TV6 ALGERIE [hta_dz-off]": "https://i.ibb.co/fXcD722/tv6al.png",
    "TV7 ELMAARIFA [hta_dz-off]": "https://i.ibb.co/hBCbJ22/tv7al.png",
    "TV8 EDHAKIRA [hta_dz-off]": "https://i.ibb.co/zSWw6QZ/tv8al.png",
    "SAMIRA TV [hta_dz-off]": "https://i.ibb.co/HzvjJq6/samira.png",
    "EL BILAD [hta_dz-off]": "https://i.ibb.co/ByPHXnt/bilad.png",
    "ENNAHAR TV [hta_dz-off]": "https://i.ibb.co/pPwR2Tc/ennahar.png",
    "EL HAYAT TV [hta_dz-off]": "https://i.ibb.co/7Q4Zv2v/elhayat.png",
    "EL FADRJ TV [hta_dz-off]": "https://i.ibb.co/Gn8kzrj/fadrj.png",
    "EL DJAZAIR N1 [hta_dz-off]": "https://i.ibb.co/BfwWGdQ/djan1.png",
    "BAHIA TV [hta_dz-off]": "https://i.ibb.co/sVMjt0y/bahia.png",
    "AL24 NEWS [hta_dz-off]": "https://i.ibb.co/fnc8K1s/al24.jpg",
    "EL HEDDAF TV [hta_dz-off]": "https://i.ibb.co/y5rY7zJ/heddaf.png",
    "ALANIS TV [hta_dz-off]": "https://i.ibb.co/3MdNH7S/alanis.png",
    "ECHOROUK TV [hta_dz-off]": "https://i.ibb.co/yQmcHjz/echourouk.png",
    "ECHOROUK NEWS  [hta_dz-off]": "https://i.ibb.co/1vH6q4L/echounws.png",
    "BEUR TV [hta_dz-off]": "https://i.ibb.co/PMpGQk6/beur.png",
    "EL DJAZAIRIA TV [downline]": "https://i.ibb.co/j8L3hMr/djaz1.png",
    "LINA TV [downline]": "https://i.ibb.co/h9yh1nr/lina.png",
    "SAMIRA TV [downline]": "https://i.ibb.co/HzvjJq6/samira.png",
    "NESSMA [offlink]": "https://i.ibb.co/stZxQHF/nessma.png",
    "KAN 11 sub-cc כאן": "https://i.ibb.co/fMMBKqc/kan11.png",
    "RESHET 13 רשת": "https://i.ibb.co/MnSQCcr/R1322.jpg",
    "RESHET 13 sub-cc רשת": "https://i.ibb.co/MnSQCcr/R1322.jpg",
    "NOW 14 עכשיו": "https://i.ibb.co/4g6BSYf/now14smgri.png",
    "i24 NEWS HE עברית": "https://i.ibb.co/j68q1Bp/i24.png",
    "HINUCHIT 23 חינוכית": "https://i.ibb.co/tLYB26T/h2322.png",
    "MAKO 24 ערוץ": "https://i.ibb.co/7nYM8MK/arutz24tvtrp.png",
    "CALCALA 10 ערוץ_הכלכלה": "https://i.ibb.co/3hN9N8X/tv10coil.png",
    "HAKNESSET 99 כנסת": "https://i.ibb.co/zP5vjLD/knesset.png",
    "HAKNESSET 99 sub-cc כנסת": "https://i.ibb.co/zP5vjLD/knesset.png",
    "RESHET 13 COMEDY": "https://i.ibb.co/sQd5XDT/13comedy.jpg",
    "RESHET 13 NOFESH": "https://i.ibb.co/tPh5D2w/13nofesh.jpg",
    "RESHET 13 REALITY": "https://i.ibb.co/9sX793L/13reality.jpg",
    "WALLA !+ וואלה! חדשות": "https://i.ibb.co/jzRyjBn/walla.png",
    "SPORT5 STUDIO RADIO LIVE": "https://i.ibb.co/Yc5Yf1q/sport5il.png",
    "YNET NEWS ידיעות אחרונות": "https://i.ibb.co/kq4XM0Y/ynet.png",
    "i24 NEWS EN": "https://i.ibb.co/j68q1Bp/i24.png",
    "i24 NEWS AR": "https://i.ibb.co/j68q1Bp/i24.png",
    "PANET 30 HALA هلا": "https://i.ibb.co/MG43H4H/hala.png",
    "KAN 33 MAKAN مكان": "https://i.ibb.co/fqTYrGY/33.png",
    "ISRAEL 9TV канал": "https://i.ibb.co/PYtP8fm/arutz9ru.png",
    "KAN 26 אפיק": "https://i.ibb.co/6yjTszg/kan26.png",
    "KABBALAH 96": "https://i.ibb.co/93bQz4t/kabalah.png",
    "HIDABROOT 97": "https://i.ibb.co/bJVPhHD/hidabroot.png",
    "MUSAYOF מוסאיוף": "https://i.ibb.co/Ph3cBMj/musayof.jpg",
    "SHELANU GOD-IL": "https://i.ibb.co/tMm7vdM/shelanug.jpg",
    "SHOPPING 21 [ended]": "https://i.ibb.co/2g7Sw4c/21.jpg",
    "RELEVANT רלוונט [ended]": "https://i.ibb.co/5MyMYqB/relevantil.png",
    "KAN 11 כאן (backup)": "https://i.ibb.co/fMMBKqc/kan11.png",
    "KESHET 12 קשת (backup)": "https://i.ibb.co/5TQ4RM3/Keshet12.png",
    "RESHET 13 רשת (backup)": "https://i.ibb.co/MnSQCcr/R1322.jpg",
    "RESHET 13 sub-cc רשת (backup)": "https://i.ibb.co/MnSQCcr/R1322.jpg",
    "HINUCHIT 23 sub-cc חינוכית (backup rescue)": "https://i.ibb.co/tLYB26T/h2322.png",
    "MAKO 24 ערוץ (backup)": "https://i.ibb.co/7nYM8MK/arutz24tvtrp.png",
    "CALCALA 10 ערוץ_הכלכלה (backup)": "https://i.ibb.co/3hN9N8X/tv10coil.png",
    "WALLA !+ וואלה! חדשות (backup)": "https://i.ibb.co/jzRyjBn/walla.png",
    "WALLA ! + (backup rescue)": "https://i.ibb.co/jzRyjBn/walla.png",
    "WALLA ! + (backup secure)": "https://i.ibb.co/jzRyjBn/walla.png",
    "RELEVANT רלוונט (backup)": "https://i.ibb.co/5MyMYqB/relevantil.png",
    "YNET NEWS (feed)": "https://i.ibb.co/kq4XM0Y/ynet.png",
    "KAN 11 כאן (backlink)": "https://i.ibb.co/fMMBKqc/kan11.png",
    "KAN 11 כאן sub-cc (backlink)": "https://i.ibb.co/fMMBKqc/kan11.png",
    "HINUCHIT 23 חינוכית (backlink)": "https://i.ibb.co/tLYB26T/h2322.png",
    "KAN 33 MAKAN مكان (backlink)": "https://i.ibb.co/fqTYrGY/33.png",
    "RESHET 13 רשת (backlink)": "https://i.ibb.co/MnSQCcr/R1322.jpg",
    "HAKNESSET 99 כנסת (backlink)": "https://i.ibb.co/zP5vjLD/knesset.png",
    "KESHET 12 קשת [find-host]": "https://i.ibb.co/5TQ4RM3/Keshet12.png",
    "MAKO 24 ערוץ [find-host]": "https://i.ibb.co/7nYM8MK/arutz24tvtrp.png",
    "NEWS 12 חדשות [find-host/offline]": "https://i.ibb.co/1rSGfFw/N12n.png",
    "NOW 14 עכשיו [deadlink]": "https://i.ibb.co/4g6BSYf/now14smgri.png",
    "ISRAEL 9TV канал [diedlink]": "https://i.ibb.co/PYtP8fm/arutz9ru.png",
    "KESHET 12 קשת [mako-src]": "https://i.ibb.co/5TQ4RM3/Keshet12.png",
    "KESHET 12 קשת [frame-issue]": "https://i.ibb.co/5TQ4RM3/Keshet12.png",
    "MAKO 24 ערוץ [mako-src]": "https://i.ibb.co/7nYM8MK/arutz24tvtrp.png",
    "NEWS 12 חדשות [mako-src/offline]": "https://i.ibb.co/1rSGfFw/N12n.png",
    "AL ALARABY 2": "https://i.ibb.co/s107QNv/araby2.png",
    "MURR LBN": "https://i.ibb.co/F3rnLz2/mtvleb.png",
    "ONE LBN": "https://i.ibb.co/vJj1gdb/onetvlb.jpg",
    "VOICE OF LBN": "https://i.ibb.co/zH7W9tX/volbn.png",
    "FUTURE LBN": "https://i.ibb.co/ZB8x8TP/futlbn.png",
    "NBN": "https://i.ibb.co/wR2jkMz/nbnlb.png",
    "LANA TV": "https://i.ibb.co/ygKx229/lana1.png",
    "NABAA TV": "https://i.ibb.co/JrFjqrc/nabaa.png",
    "TAHA TV": "https://i.ibb.co/h872gKg/taha.png",
    "OTV LBN": "https://i.ibb.co/Svnqq8G/otv.jpg",
    "AL JADEED": "https://i.ibb.co/hM98B0V/jadeed.png",
    "AL AAN TV": "https://i.ibb.co/XVGL3qH/alaan.png",
    "ABU DHABI": "https://i.ibb.co/HVLDcrR/abudhabi.png",
    "AL EMARAT": "https://i.ibb.co/yV6Jhjg/alemarat.png",
    "ABU DHABI SPORTS 1": "https://i.ibb.co/L61bf70/adspts.png",
    "ABU DHABI SPORTS 2": "https://i.ibb.co/L61bf70/adspts.png",
    "YAS TV": "https://i.ibb.co/Q6tZWdh/yas.png",
    "BAYNOUNAH TV": "https://i.ibb.co/Dr7jn2L/baynounah.png",
    "HALA LONDON": "https://i.ibb.co/b2KHBPn/halalnd.png",
    "LIBYA WATANYA": "https://i.ibb.co/mCBL5fNk/lybiawat.jpg",
    "AL MAMLKA": "https://i.ibb.co/qJ7qVTF/Al-Mamlaka.png",
    "SYDAT EL SHASHA": "https://i.ibb.co/5LvvstB/elshasha.png",
    "FUJAIRAH TV": "https://i.ibb.co/b6ZvV2r/fujairah.png",
    "ROYA TV": "https://i.ibb.co/84HtHzK/Roya-TV.png",
    "AL MASAR": "https://i.ibb.co/3mfSV6R6/almasar.jpg",
    "ALAWLA TV": "https://i.ibb.co/HtKQ15z/alw1.png",
    "ASSIRAT": "https://i.ibb.co/tqkV2sn/irflag.png",
    "SHARJAH TV": "https://i.ibb.co/nnQnFjg/sharjahtv.png",
    "SHARJAH TV 2": "https://i.ibb.co/7KSJQYX/sharjah2.png",
    "SHARJAH TV SPORTS": "https://i.ibb.co/1bpYYZ2/shrspt.png",
    "QATAR TV": "https://i.ibb.co/x8ftqHr/qattv.png",
    "QATAR TV 2": "https://i.ibb.co/y4qNK42/qattv2.png",
    "SYRIA TV": "https://i.ibb.co/d58T05P/Syria-tv.jpg",
    "SYRIA TV 2": "https://i.ibb.co/0kQdg9X/syria2.png",
    "SALAM": "https://i.ibb.co/XrC6F6JW/salam.png",
    "AL WASAT TV": "https://i.ibb.co/QPv27Qc/wtw.jpg",
    "AL RAYYAN": "https://i.ibb.co/dp728rg/rayan.png",
    "AL RAYYAN QADEEM": "https://i.ibb.co/n333gP9/rayanqdm.png",
    "AL MAYADEEN": "https://i.ibb.co/1KcjbKf/almayadeen.png",
    "AL MANAR": "https://i.ibb.co/gZKY6Tn/almanar.png",
    "AL GHAD TV": "https://i.ibb.co/mN2JhVS/alghad.png",
    "AL GHAD PLUS": "https://i.ibb.co/mN2JhVS/alghad.png",
    "AL MASIRA": "https://i.ibb.co/4Vfg55v/almasira.png",
    "AL KHALIJ TV": "https://i.ibb.co/zGHHGbj/alkhalij.jpg",
    "PANET 30 HALA": "https://i.ibb.co/MG43H4H/hala.png",
    "KAN 33 MAKAN": "https://i.ibb.co/fqTYrGY/33.png",
    "A ONE": "https://i.ibb.co/S6xK2x9/aone.jpg",
    "KAB 1": "https://i.ibb.co/qMyBBdb/kab.png",
    "AL WOUSTA": "https://i.ibb.co/fFZ3kZj/alwousta.png",
    "ATFAL": "https://i.ibb.co/5TZPHf6/atfal.jpg",
    "AJMAN TV": "https://i.ibb.co/sKJGV9q/Ajman.jpg",
    "SUDAN TV": "https://i.ibb.co/Y7PcRQCG/sudan.png",
    "DABANGA": "https://i.ibb.co/svNjxMqW/dabanga.png",
    "AMMAN TV": "https://i.ibb.co/vm3481D/amman.png",
    "ALRAIMEDIA": "https://i.ibb.co/C2c1NJN/alraimedia.png",
    "MEKAMELEEN": "https://i.ibb.co/0mtj39x/Mekameleen.png",
    "IFILM AR": "https://i.ibb.co/kDhcymF/ifilm.png",
    "ON E": "https://i.ibb.co/gZ1q6zP9/ontve.png",
    "AL IRAQIA": "https://i.ibb.co/mVPZh6Gz/Aliraqia.jpg",
    "AL MASIRAH": "https://i.ibb.co/99cj3D4g/Masirah.jpg",
    "BAHRAIN TV": "https://i.ibb.co/HCZGRZk/bahraintv.png",
    "BAHRAIN TV INT": "https://i.ibb.co/HCZGRZk/bahraintv.png",
    "BEDAYA TV": "https://i.ibb.co/M9MzqDm/bedaya.png",
    "YEMEN MAHRIAH": "https://i.ibb.co/VCfg2xY/almahriah.png",
    "AL JAYLIA": "https://i.ibb.co/PFCf0SG/jaylia.jpg",
    "ETIHAD": "https://i.ibb.co/740Znb4/ittihad.png",
    "THAQAFEYYAH": "https://i.ibb.co/GT1LMyS/thaqafeyyah.webp",
    "AL HAQIQA": "https://i.ibb.co/PYwbLwJ/haqiqat.jpg",
    "AL MASHHAD": "https://i.ibb.co/Lkwk0zB/almashd.png",
    "AL YAUM": "https://i.ibb.co/2KwY06R/alyaum.png",
    "PAYAM TV": "https://i.ibb.co/nPBCcKq/payam.jpg",
    "AL RABIAA": "https://i.ibb.co/f2XWR2M/alrabiaa.jpg",
    "SAMA TV": "https://i.ibb.co/mcd2S4f/samaatv.png",
    "AL DAFRAH": "https://i.ibb.co/FYdQXH1/aldafrah.png",
    "RAJEEN": "https://i.ibb.co/gJcnzXw/rajeen.png",
    "QUDS TV": "https://i.ibb.co/4g4VNx7/quds-tv.png",
    "PAL PBC": "https://i.ibb.co/RS72QHZ/pbcpalestine.png",
    "MUSAWA": "https://i.ibb.co/r5FwmZQ/musawa.png",
    "PAL TV": "https://i.ibb.co/TMFyykR/paltv.png",
    "PAL SAT": "https://i.ibb.co/nkfS0P4/palsat.jpg",
    "WATAR PS": "https://i.ibb.co/nkfS0P4/palsat.jpg",
    "FALASTINI TV": "https://i.ibb.co/RNHM3Xx/falastini.png",
    "PALESTINIAN TV": "https://i.ibb.co/RNHM3Xx/falastini.png",
    "YEMEN TODAY": "https://i.ibb.co/0yytb9K/yementoday.png",
    "YEMEN SHABAB": "https://i.ibb.co/230j3Kr/yemenshabab.png",
    "UTV IRAQI": "https://i.ibb.co/wK6B1QV/utv.png",
    "AL RASHEED": "https://i.ibb.co/8jK0ZR5/alrasheed.png",
    "AL RAFIDAIN": "https://i.ibb.co/MfLxCY6/alrafidain.png",
    "WATAN EGYPT": "https://i.ibb.co/zSv52T7/watanegypt.png",
    "AL SHOOB": "https://i.ibb.co/b5gcrBs4/Alshoob.jpg",
    "QAF": "https://i.ibb.co/mFb5JL3/qaftv.png",
    "SSAD TV": "https://i.ibb.co/zGS6X8G/ssad.jpg",
    "ISHTAR TV": "https://i.ibb.co/ZNQPS3x/Ishtar.jpg",
    "AL SABAH KW": "https://i.ibb.co/CQjzKk9/alsabah.png",
    "LANA TV (backup)": "https://i.ibb.co/ygKx229/lana1.png",
    "AL ALARABY 2 (backup)": "https://i.ibb.co/s107QNv/araby2.png",
    "ROYA TV (backup)": "https://i.ibb.co/84HtHzK/Roya-TV.png",
    "MTV LBN": "https://i.ibb.co/F3rnLz2/mtvleb.png",
    "ONE TV LBN": "https://i.ibb.co/vJj1gdb/onetvlb.jpg",
    "LBC LBN [geoblocked]": "https://i.ibb.co/YhMgggj/lbcb.jpg",
    "OTV LBN [brokenlink]": "https://i.ibb.co/Svnqq8G/otv.jpg",
    "DUBAI TV": "https://i.ibb.co/BCK1L31/DubaiTV.png",
    "DUBAI ONE": "https://i.ibb.co/ngKnxmq/dubaione.png",
    "DUBAI NOOR": "https://i.ibb.co/jMsSmvg/dubainoor.png",
    "DUBAI SAMA": "https://i.ibb.co/g4LTFCS/dubaisama.png",
    "DUBAI ZAMAN": "https://i.ibb.co/xDs4dGV/dubaizaman.png",
    "DUBAI SPORTS 1": "https://i.ibb.co/LR2KqPJ/dbaispt.png",
    "DUBAI SPORTS 2": "https://i.ibb.co/LR2KqPJ/dbaispt.png",
    "DUBAI SPORTS 3": "https://i.ibb.co/LR2KqPJ/dbaispt.png",
    "DUBAI RACING 1": "https://i.ibb.co/MD9vwnv/dubairacing.png",
    "DUBAI RACING 2": "https://i.ibb.co/MD9vwnv/dubairacing.png",
    "DUBAI RACING 3": "https://i.ibb.co/MD9vwnv/dubairacing.png",
    "KAS QATAR 1": "https://i.ibb.co/3h4XCtZ/kasqatar.png",
    "KAS QATAR 2": "https://i.ibb.co/3h4XCtZ/kasqatar.png",
    "KAS QATAR 3": "https://i.ibb.co/3h4XCtZ/kasqatar.png",
    "KAS QATAR 4": "https://i.ibb.co/3h4XCtZ/kasqatar.png",
    "KAS QATAR 5": "https://i.ibb.co/3h4XCtZ/kasqatar.png",
    "KAS QATAR 6": "https://i.ibb.co/3h4XCtZ/kasqatar.png",
    "KAS QATAR SHOOF": "https://i.ibb.co/3h4XCtZ/kasqatar.png",
    "SAUDI SBC SA": "https://i.ibb.co/WcQV072/saudi1sbc.png",
    "SAUDIA TV CH 1": "https://i.ibb.co/qNXgWyZ/sauditv.jpg",
    "SAUDIA TV KSA NOW": "https://i.ibb.co/qNXgWyZ/sauditv.jpg",
    "SAUDIA THIKRAYAT": "https://i.ibb.co/6PH6566/thikrayat.jpg",
    "SAUDI ACTION WALEED": "https://i.ibb.co/c6QBhj8/actionwalid.png",
    "OMAN 1": "https://i.ibb.co/GJVSFNt/oman.png",
    "OMAN MUNASHER": "https://i.ibb.co/GJVSFNt/oman.png",
    "OMAN CULTURE": "https://i.ibb.co/GJVSFNt/oman.png",
    "OMAN SPORT": "https://i.ibb.co/GJVSFNt/oman.png",
    "OMAN TV": "https://i.ibb.co/GJVSFNt/oman.png",
    "JORDAN TV": "https://i.ibb.co/y4xS49d/jordan-tv.png",
    "JORDAN TOURISM": "https://i.ibb.co/y4xS49d/jordan-tv.png",
    "JORDAN DRAMA": "https://i.ibb.co/y4xS49d/jordan-tv.png",
    "JORDAN COMEDY": "https://i.ibb.co/y4xS49d/jordan-tv.png",
    "JORDAN KITCHEN": "https://i.ibb.co/y4xS49d/jordan-tv.png",
    "JORDAN ARCHIVE": "https://i.ibb.co/y4xS49d/jordan-tv.png",
    "JORDAN SONG": "https://i.ibb.co/y4xS49d/jordan-tv.png",
    "KUWAIT TV 1": "https://i.ibb.co/tMLDMdy/kwttv.png",
    "KUWAIT TV 2": "https://i.ibb.co/tMLDMdy/kwttv.png",
    "KUWAIT TV NEWS": "https://i.ibb.co/tMLDMdy/kwttv.png",
    "KUWAIT TV ARAB": "https://i.ibb.co/tMLDMdy/kwttv.png",
    "KUWAIT TV ETHRAA": "https://i.ibb.co/tMLDMdy/kwttv.png",
    "KUWAIT TV KHALLIK": "https://i.ibb.co/tMLDMdy/kwttv.png",
    "KUWAIT TV QURAIN": "https://i.ibb.co/tMLDMdy/kwttv.png",
    "KUWAIT TV SPORTS": "https://i.ibb.co/tMLDMdy/kwttv.png",
    "KUWAIT TV SPORT PLUS": "https://i.ibb.co/tMLDMdy/kwttv.png",
    "KUWAIT TV SPORT EXTRA": "https://i.ibb.co/tMLDMdy/kwttv.png",
    "SAUDI CH 1": "https://i.ibb.co/WcQV072/saudi1sbc.png",
    "SAUDI CH 2": "https://i.ibb.co/T0Rc9mJ/saudi2.png",
    "SAUDI CH 3": "https://i.ibb.co/mtqZsZ4/saudi3.png",
    "SAUDI CH 4": "https://i.ibb.co/jh0s9P6/saudich4.png",
    "SAUDI CH 6 SUNNAH": "https://i.ibb.co/FwDhYDv/saudi6.png",
    "SAUDI CH 7 KABE": "https://i.ibb.co/9p3b0MW/saudi7.png",
    "SAUDI CH 9": "https://i.ibb.co/qNXgWyZ/sauditv.jpg",
    "SAUDI CH 10": "https://i.ibb.co/qNXgWyZ/sauditv.jpg",
    "SAUDI CH 17": "https://i.ibb.co/qNXgWyZ/sauditv.jpg",
    "AL JAZEERA": "https://i.ibb.co/jLYWYh7/Al-Jazeera.png",
    "AL ARABIYA": "https://i.ibb.co/hcCJkhq/Al-Arabiya.png",
    "AL ALARABY": "https://i.ibb.co/h27qpLJ/araby1.png",
    "AL ARABIYA HADATH": "https://i.ibb.co/nc8F1dj/Al-Hadath.png",
    "AL ARABIYA BUSINESS": "https://i.ibb.co/R4vMgQV/alarabiyabus.jpg",
    "AL ARABIYA PROGRAMS": "https://i.ibb.co/hcCJkhq/Al-Arabiya.png",
    "AL JAZEERA MUBASHER": "https://i.ibb.co/dbFBq5k/Al-Jazeera-Mubasher.png",
    "AL JAZEERA MUBASHER 2": "https://i.ibb.co/dbFBq5k/Al-Jazeera-Mubasher.png",
    "AL JAZEERA MUBASHER 24": "https://i.ibb.co/dbFBq5k/Al-Jazeera-Mubasher.png",
    "AL HURRA": "https://i.ibb.co/mNnyV1K/alhurra.png",
    "AL QAHERA NEWS": "https://i.ibb.co/CMk8DS1/alqahera.png",
    "ASHARQ NEWS": "https://i.ibb.co/nzjbYfR/asharq.png",
    "ROYA NEWS": "https://i.ibb.co/84HtHzK/Roya-TV.png",
    "INEWS IQ": "https://i.ibb.co/m4tvbmp/inewsar.png",
    "BBC NEWS ARABIA": "https://i.ibb.co/JcP5JHq/bbcaranw.png",
    "SKY NEWS ARABIA": "https://i.ibb.co/dGjByMq/Sky-News-Arabia.png",
    "CNBC ARABIA": "https://i.ibb.co/FxZYHhM/cnbc.jpg",
    "DW ARABIC": "https://i.ibb.co/L8KP0z9/DW-arabic.png",
    "CGTN ARABIC": "https://i.ibb.co/njBtvts/cgtnar.png",
    "FRANCE 24 AR": "https://i.ibb.co/hKP8X8B/f24.png",
    "TRT ARABIYA": "https://i.ibb.co/vPkb8TQ/trtar.png",
    "AL ALAM IR [censure-ifany]": "https://i.ibb.co/XDC5cBX/alalam.png",
    "RT ARABIC [censure-blocked]": "https://i.ibb.co/D7w9h7Q/rt.png",
    "ASHARQ DOCS": "https://i.ibb.co/nzjbYfR/asharq.png",
    "ASHARQ DOCS 2": "https://i.ibb.co/nzjbYfR/asharq.png",
    "AL HIWAR": "https://i.ibb.co/Fs6CgPG/Al-Hiwar.png",
    "AL SHARQIYA": "https://i.ibb.co/PNLHyhs/Al-Sharqiya-News.png",
    "AL IRAQIA NEWS": "https://i.ibb.co/nMzmrDFJ/Aliraqianews.jpg",
    "PANORAMA FM TV": "https://i.ibb.co/tsWQ5pz/panorama.jpg",
    "EL SHARQ": "https://i.ibb.co/H4shFvm/elsharq.png",
    "WANASAH": "https://i.ibb.co/KX5tK6Q/Wanasa.png",
    "MAJID": "https://i.ibb.co/DbFpsdR/majid.png",
    "SPACE TOON": "https://i.ibb.co/QFvZPd9/spacetoon.png",
    "SAT7 KIDS": "https://i.ibb.co/LYMKBP2/Sat7kids.png",
    "AFARIN TV": "https://i.ibb.co/HVLKncL/afarin.png",
    "AL SHALLAL": "https://i.ibb.co/k8Xbs2n/alshallal.jpg",
    "TEN WEYYAK": "https://i.ibb.co/Ch3FNj9/tenar.jpg",
    "IQRAA 1": "https://i.ibb.co/S3Wm3q9/iqraanew.png",
    "IQRAA 2": "https://i.ibb.co/S3Wm3q9/iqraanew.png",
    "IQRAA 3": "https://i.ibb.co/S3Wm3q9/iqraanew.png",
    "IQRAA": "https://i.ibb.co/S3Wm3q9/iqraanew.png",
    "IQRAA EUR": "https://i.ibb.co/S3Wm3q9/iqraanew.png",
    "QURAN": "https://i.ibb.co/tqkV2sn/irflag.png",
    "BAHRAIN QURAN": "https://i.ibb.co/cygNtwH/bahrain-quaran.png",
    "SHARJAH QURAN": "https://i.ibb.co/2qdGPCh/Sharjahtvquran.png",
    "AL QAMAR": "https://i.ibb.co/dQtMFVT/qamar.jpg",
    "ALMASIRA MUBASHER": "https://i.ibb.co/ypj95gJ/almasirah.png",
    "AL EKHBARIA": "https://i.ibb.co/TkVK043/ekbariya.png",
    "AL SUNNAH TV": "https://i.ibb.co/MctgDQ8/sunnah.png",
    "AL MAJD HOLY QURAN TV": "https://i.ibb.co/Qj9JJTCZ/amhquran.png",
    "QURAN KAREEM TV": "https://i.ibb.co/f0cKj4S/kareem.jpg",
    "AL ISTIQAMA": "https://i.ibb.co/HPzRmd3/alistiqama.png",
    "SAT7 ARABIC": "https://i.ibb.co/Mgm51w6/sat7ara.webp",
    "NOURSAT": "https://i.ibb.co/Tgg3JpC/noursat.png",
    "NOURSAT AL SHARQ": "https://i.ibb.co/Tgg3JpC/noursat.png",
    "NOURSAT AL KODDASS": "https://i.ibb.co/Tgg3JpC/noursat.png",
    "NOURSAT EL SHABEB": "https://i.ibb.co/Tgg3JpC/noursat.png",
    "NOURSAT MARIAM": "https://i.ibb.co/Tgg3JpC/noursat.png",
    "NOURSAT ENG": "https://i.ibb.co/Tgg3JpC/noursat.png",
    "CTV COPTIC": "https://i.ibb.co/St7FsRJ/ctvcop.jpg",
    "AL HURRA (backup)": "https://i.ibb.co/mNnyV1K/alhurra.png",
    "ASHARQ NEWS (backup)": "https://i.ibb.co/nzjbYfR/asharq.png",
    "ASHARQ NEWS (portrait mode)": "https://i.ibb.co/nzjbYfR/asharq.png",
    "AL JAZEERA (backup)": "https://i.ibb.co/jLYWYh7/Al-Jazeera.png",
    "AL ARABIYA (backup)": "https://i.ibb.co/hcCJkhq/Al-Arabiya.png",
    "AL ALARABY (backup)": "https://i.ibb.co/h27qpLJ/araby1.png",
    "AL ARABY 2 (part-time)": "https://i.ibb.co/s107QNv/araby2.png",
    "FRANCE 24 AR (backup)": "https://i.ibb.co/hKP8X8B/f24.png",
    "BBC NEWS ARABIA (backup)": "https://i.ibb.co/JcP5JHq/bbcaranw.png",
    "MAAN NEWS [issue]": "https://i.ibb.co/9nsvXcf/maannews.png",
    "CARTOON NETWORK AR [down]": "https://i.ibb.co/Zxd0j45/cartoonnetwork.png",
    "GULLI ARABI [down]": "https://i.ibb.co/PjCYRWx/gulliar.jpg",
    "MBC 1": "https://i.ibb.co/N19JFwZ/mbc.png",
    "MBC 1 USA": "https://i.ibb.co/N19JFwZ/mbc.png",
    "MBC 3": "https://i.ibb.co/bvbsV1Z/mbc3.png",
    "MBC 3 USA": "https://i.ibb.co/bvbsV1Z/mbc3.png",
    "MBC 4": "https://i.ibb.co/5smk763/mbc4.png",
    "MBC 5": "https://i.ibb.co/vzbhKTj/mbc5.png",
    "MBC DRAMA": "https://i.ibb.co/2ndSCfQ/mbcdrama0.png",
    "MBC DRAMA USA": "https://i.ibb.co/2ndSCfQ/mbcdrama0.png",
    "MBC DRAMA MASR": "https://i.ibb.co/2ndSCfQ/mbcdrama0.png",
    "MBC DRAMA PLUS": "https://i.ibb.co/xzdqq9y/mbcdrama.png",
    "MBC MASR 1": "https://i.ibb.co/BnhWg65/mbcmasr.png",
    "MBC MASR USA": "https://i.ibb.co/BnhWg65/mbcmasr.png",
    "MBC MASR 2": "https://i.ibb.co/M7B22HL/mbcmasr2.jpg",
    "MBC IRAQ": "https://i.ibb.co/rkr6JSX/mbc-iraq.png",
    "MBC BOLLYWOOD": "https://i.ibb.co/m5gGgfJ/mbcbollywood.png",
    "MBC AFLAM": "https://i.ibb.co/mc475nQ/shadidblck.jpg",
    "MBC MOVIES": "https://i.ibb.co/mc475nQ/shadidblck.jpg",
    "MBC MOVIES ACTION": "https://i.ibb.co/mc475nQ/shadidblck.jpg",
    "MBC MOVIES THRILLER": "https://i.ibb.co/mc475nQ/shadidblck.jpg",
    "MBC RABEH SAQER": "https://i.ibb.co/98TBSSm/mbcfmtv.png",
    "MBC FM LIVE TV": "https://i.ibb.co/98TBSSm/mbcfmtv.png",
    "MBC LOUD FM TV": "https://i.ibb.co/Hy2GLK8/mbcloud.png",
    "ROTANA CINEMA KSA": "https://i.ibb.co/7W5nWYV/rotanacinema.png",
    "ROTANA AFLAM PLUS": "https://i.ibb.co/7W5nWYV/rotanacinema.png",
    "ROTANA M PLUS": "https://i.ibb.co/N2C6FMyv/Mplus.png",
    "ROTANA KHALIJA": "https://i.ibb.co/5sJ9vSJ/rotanakhalijia.png",
    "ROTANA PNC DRAMA": "https://i.ibb.co/207NnrF1/pncdr.png",
    "ROYA MUSIC": "https://i.ibb.co/84HtHzK/Roya-TV.png",
    "ROYA KITCHEN": "https://i.ibb.co/84HtHzK/Roya-TV.png",
    "ROYA COMEDY": "https://i.ibb.co/84HtHzK/Roya-TV.png",
    "ROYA PALESTINE": "https://i.ibb.co/84HtHzK/Roya-TV.png",
    "ROYA KIDS": "https://i.ibb.co/84HtHzK/Roya-TV.png",
    "ROYA KIDS ORIGINALS": "https://i.ibb.co/84HtHzK/Roya-TV.png",
    "ROYA KIDS SONGS": "https://i.ibb.co/84HtHzK/Roya-TV.png",
    "ROYA KIDS STORIES": "https://i.ibb.co/84HtHzK/Roya-TV.png",
    "ROYA DRAMA": "https://i.ibb.co/84HtHzK/Roya-TV.png",
    "ROYA SPORTS": "https://i.ibb.co/84HtHzK/Roya-TV.png",
    "ROYA WORLD": "https://i.ibb.co/84HtHzK/Roya-TV.png",
    "ROYA ADVENTURES": "https://i.ibb.co/84HtHzK/Roya-TV.png",
    "ROYA MARAYA": "https://i.ibb.co/84HtHzK/Roya-TV.png",
    "ROYA CARAVAN": "https://i.ibb.co/84HtHzK/Roya-TV.png",
    "ROYA IMAM": "https://i.ibb.co/84HtHzK/Roya-TV.png",
    "ROYA PRODUCTION": "https://i.ibb.co/84HtHzK/Roya-TV.png",
    "ROYA AL HAYBA": "https://i.ibb.co/84HtHzK/Roya-TV.png",
    "ROYA ACTION": "https://i.ibb.co/84HtHzK/Roya-TV.png",
    "ROYA AH SHAMYEH": "https://i.ibb.co/84HtHzK/Roya-TV.png",
    "ROYA AL QUEBBEH": "https://i.ibb.co/84HtHzK/Roya-TV.png",
    "ROYA NADINENJAIM": "https://i.ibb.co/84HtHzK/Roya-TV.png",
    "ROYA AYMAN ZAYDAN": "https://i.ibb.co/84HtHzK/Roya-TV.png",
    "ROYA AL ZAEEM": "https://i.ibb.co/84HtHzK/Roya-TV.png",
    "ROYA HAKI MONAWWA": "https://i.ibb.co/84HtHzK/Roya-TV.png",
    "ROYA ANA BAHKILAK": "https://i.ibb.co/84HtHzK/Roya-TV.png",
    "ROYA MASRAHYYAT": "https://i.ibb.co/84HtHzK/Roya-TV.png",
    "ROYA DOCU": "https://i.ibb.co/84HtHzK/Roya-TV.png",
    "ROYA MOJTAMAII": "https://i.ibb.co/84HtHzK/Roya-TV.png",
    "ZEE AFLAM": "https://i.ibb.co/5RGbN6g/Zee-Afam.png",
    "ZEE ALWAN": "https://i.ibb.co/c1zsKkv/Zee-Alwan.png",
    "WEYYAK DRAMA": "https://i.ibb.co/3WCfsRq/weyk.png",
    "WEYYAK MIX": "https://i.ibb.co/3WCfsRq/weyk.png",
    "WEYYAK ACTION": "https://i.ibb.co/3WCfsRq/weyk.png",
    "WEYYAK NAWAEM": "https://i.ibb.co/3WCfsRq/weyk.png",
    "CBC LIVE": "https://i.ibb.co/dQV1zQG/cbclive.jpg",
    "CBC SOFRA": "https://i.ibb.co/0jpsxm7/cbcsofra.png",
    "CBC NEWS": "https://i.ibb.co/Vt0XZKf/Cbcnews.png",
    "ROTANA CINEMA MASR": "https://i.ibb.co/7W5nWYV/rotanacinema.png",
    "ROTANA PLUS": "https://i.ibb.co/RC0XZrb/rotanaplus.png",
    "ROTANA KIDS": "https://i.ibb.co/PN8G6F8/rotanakids.png",
    "ROTANA DRAMA": "https://i.ibb.co/Tw3gRvT/rotanadrama.png",
    "ROTANA DUHK WABASS": "https://i.ibb.co/YL1wKY8/Duhkwabas.png",
    "SHAHID AL ZAEEM": "https://i.ibb.co/JqnC8VY/shahid.png",
    "SHAHID AL MASRAH": "https://i.ibb.co/JqnC8VY/shahid.png",
    "SHAHID AL USTURA": "https://i.ibb.co/JqnC8VY/shahid.png",
    "SHAHID COMEDY": "https://i.ibb.co/JqnC8VY/shahid.png",
    "SHAHID 1": "https://i.ibb.co/JqnC8VY/shahid.png",
    "SHAHID SHAM": "https://i.ibb.co/JqnC8VY/shahid.png",
    "SHAHID MAQALEB": "https://i.ibb.co/JqnC8VY/shahid.png",
    "SHAHID AL ZARAQ": "https://i.ibb.co/JqnC8VY/shahid.png",
    "MBC 1 [offlink]": "https://i.ibb.co/N19JFwZ/mbc.png",
    "MBC MASR 1 [offlink]": "https://i.ibb.co/BnhWg65/mbcmasr.png",
    "RAI NEWS 24": "https://i.ibb.co/xGG27kS/raiit.png",
    "RAI 3": "https://i.ibb.co/xGG27kS/raiit.png",
    "CLASS CNBC": "https://i.imgur.com/oAiSU8O.png",
    "LA C NEWS 24": "https://i.imgur.com/02vCECa.png",
    "TELETICINO": "http://odmsto.com/uploads/tv_image/sm/teleticino.png",
    "LA 7": "https://i.imgur.com/F90mpSa.png",
    "ITALIA 2 TV": "https://i.imgur.com/ISbxfY0.png",
    "RETE TV": "https://i.imgur.com/lXGWoV9.png",
    "RETE 55": "https://i.imgur.com/EsZn2cj.png",
    "CANALE 7": "https://i.ibb.co/KmY1chC/Canale-7.png",
    "CAFE TV 24": "https://i.ibb.co/JCzkhFF/cafe24.png",
    "RADIO 105 TV": "https://i.imgur.com/3NiLKvj.png",
    "DEEJAY TV": "https://i.imgur.com/rlaKH6k.png",
    "RADIO ITALIA TV": "https://i.imgur.com/4VCEJuJ.png",
    "RADIO ITALIA TREND": "https://i.ibb.co/vj6rjWs/radioitrrend.png",
    "RADIO KISS KISS TV": "https://i.imgur.com/UTStxDW.png",
    "R101 TV": "https://i.imgur.com/mWeEa9T.png",
    "RTL 102.5": "https://i.imgur.com/KdissvS.png",
    "SUPER!": "https://i.imgur.com/zDByOwo.png",
    "EXTRA TV": "https://i.imgur.com/KCBurST.png",
    "SPORT ITALIA": "https://www.tvdream.net/img/sportitalia.png",
    "SPORT ITALIA LIVE": "http://odmsto.com/uploads/tv_image/sm/sportitalia-24-live.jpg",
    "RTV S.MARINO": "http://odmsto.com/uploads/tv_image/sm/rtv-smarino-sport.png",
    "GO-TV": "https://www.tvdream.net/img/go-tv.png",
    "SUPER TENNIS": "https://i.imgur.com/GzsPlbX.png",
    "RADIO MONTECARLO TV": "https://i.imgur.com/3TMMXmS.png",
    "VIRGIN RADIO TV": "https://i.imgur.com/7Im3HI1.png",
    "ALTO ADIGE TV": "https://i.imgur.com/S2sCFQi.png",
    "ANRENNA 2 BERGAMO": "https://i.imgur.com/NfvHIAw.png",
    "ANTENNA 3 VENETO": "https://i.imgur.com/NiVHLwp.png",
    "ANTENNA SUD": "https://i.imgur.com/b8y6ImZ.png",
    "ANTENNA SUD EXTRA": "https://i.imgur.com/6tBv8VD.png",
    "ARISTANIS TV": "https://i.imgur.com/v8PlAJO.png",
    "ARTE NETWORK": "https://i.imgur.com/DP5y0Er.png",
    "AURORA ARTE": "https://i.imgur.com/BoLZ5wG.png",
    "AZZURRA TV": "https://i.imgur.com/mSWw8uW.png",
    "EURONEWS IT": "https://i.ibb.co/VxLFYSj/euronews.png",
    "DAS ERSTE INTL": "https://i.ibb.co/GcZR4DM/daserste.png",
    "DAS ERSTE DE": "https://i.ibb.co/GcZR4DM/daserste.png",
    "RTL DE": "https://i.ibb.co/Msmh0pG/rtlde.png",
    "ALPHA ARD": "https://i.ibb.co/cc4J7ZB/Alphaard.png",
    "BR DE": "https://i.ibb.co/jkNhhLn/brfde.png",
    "HR DE": "https://i.ibb.co/JnYMnfw/hrde.png",
    "SR DE": "https://i.ibb.co/5sJk5v2/srde.png",
    "WDR DE": "https://i.ibb.co/4j4PnNL/wdr.png",
    "ARTE DE": "https://i.ibb.co/BPpZPBn/arte.png",
    "EURONEWS DE": "https://i.ibb.co/VxLFYSj/euronews.png",
    "RT DEUTSCH [censure-blocked]": "https://i.ibb.co/D7w9h7Q/rt.png",
    "RTL LUX": "https://i.ibb.co/VprDD5J/rtllux.png",
    "RTL LUX 2": "https://i.ibb.co/VprDD5J/rtllux.png",
    "DR TVA": "https://i.ibb.co/6Rdh3h1Q/drtva.png",
    "YLE TV WORLD": "https://i.ibb.co/r29pMj4B/Ylew.png",
    "TVP POLONIA": "https://i.ibb.co/yhjqqNQ/tvppol.png",
    "TVP INFO": "https://i.ibb.co/pxSC2HJ/tvpinfo.png",
    "POLSAT NEWS": "https://i.ibb.co/kx2RQ5V/polsatnews1.png",
    "EURONEWS PL": "https://i.ibb.co/VxLFYSj/euronews.png",
    "TVR INT": "https://i.ibb.co/w46x9LM/tvri.png",
    "ANTENA 1 RO": "https://i.ibb.co/9GHhm6L/ant1ro.png",
    "ANTENA 3 VOX": "https://i.ibb.co/FJbq1ML/a3ro.jpg",
    "KANAL D RO": "https://i.ibb.co/8Mngyds/kd1ro.png",
    "KANAL D2 RO": "https://i.ibb.co/gMNsZPf/kd2ro.png",
    "MOLDOVA 1": "https://i.ibb.co/KjgkLjq/md1.png",
    "MOLDOVA 2": "https://i.ibb.co/Wz954nZ/md2.png",
    "HRT 1": "https://i.ibb.co/nnkDGpc/hrthr.png",
    "HRT 2": "https://i.ibb.co/nnkDGpc/hrthr.png",
    "HRT 3": "https://i.ibb.co/nnkDGpc/hrthr.png",
    "RTL HR": "https://i.ibb.co/zNxvwRc/rtlhr.png",
    "CMC TV": "https://i.ibb.co/NgPZkKhJ/cmctv.png",
    "TV JADRAN": "https://i.ibb.co/nM7rVmT4/jadran.png",
    "N1 HRV": "https://i.ibb.co/pBZ486WC/n1bal.png",
    "BH RT": "https://i.ibb.co/HLzRKs7k/bhrt.png",
    "TELEVIZIJA M": "https://i.ibb.co/YFPPw1Wf/tvmba.png",
    "AL JAZEERA BALKANS": "https://i.ibb.co/4nyQwgwX/Aljbalk.png",
    "N1 BOS": "https://i.ibb.co/pBZ486WC/n1bal.png",
    "RTS 1": "https://i.ibb.co/xHMT7Jz/rtsrs.png",
    "RTS 2": "https://i.ibb.co/xHMT7Jz/rtsrs.png",
    "RTS SVET": "https://i.ibb.co/xHMT7Jz/rtsrs.png",
    "PINK TV": "https://i.ibb.co/ZJB71LL/pinktvrs.png",
    "PINK RED": "https://i.ibb.co/ZJB71LL/pinktvrs.png",
    "BN TV": "https://i.ibb.co/TBZ2pnKW/bntv.png",
    "TV AS": "https://i.ibb.co/Wvttv9WX/Tvas.png",
    "PI KANAL": "https://i.ibb.co/0y3F6QYq/Piknl.png",
    "N1 SRB": "https://i.ibb.co/pBZ486WC/n1bal.png",
    "EURONEWS SRB": "https://i.ibb.co/VxLFYSj/euronews.png",
    "MOBA": "https://i.ibb.co/F4FwJnNY/moba.png",
    "POP STAR": "https://i.ibb.co/gMLsMZ9P/popstar.png",
    "JEKA": "https://i.ibb.co/kVXqj9fQ/Jeka.png",
    "ZZ TV": "https://i.ibb.co/W4zhWby6/Zztv.png",
    "TVCG 1": "https://i.ibb.co/5x1cbJqN/rtcg.png",
    "TVCG 2": "https://i.ibb.co/5x1cbJqN/rtcg.png",
    "TVCG 3": "https://i.ibb.co/5x1cbJqN/rtcg.png",
    "TVCG MNE": "https://i.ibb.co/5x1cbJqN/rtcg.png",
    "NEWS 24 ALB": "https://i.ibb.co/rf1Vmfs5/Nwsalb.png",
    "GPB 2TV": "https://i.ibb.co/RN3dJQ7/geoflag.png",
    "IMEDI": "https://i.ibb.co/RN3dJQ7/geoflag.png",
    "RUSTAVI 2": "https://i.ibb.co/RN3dJQ7/geoflag.png",
    "PALITRA": "https://i.ibb.co/RN3dJQ7/geoflag.png",
    "FORMULA": "https://i.ibb.co/RN3dJQ7/geoflag.png",
    "ADJARA": "https://i.ibb.co/RN3dJQ7/geoflag.png",
    "MTAVARI ARKHI": "https://i.ibb.co/RN3dJQ7/geoflag.png",
    "GDS TV": "https://i.ibb.co/RN3dJQ7/geoflag.png",
    "H1 ARM Հանրային հեռուստաը": "https://i.ibb.co/tmkv6RC/armflag.png",
    "H1 NEWS": "https://i.ibb.co/tmkv6RC/armflag.png",
    "SONG ARM": "https://i.ibb.co/tmkv6RC/armflag.png",
    "FRESH ARM": "https://i.ibb.co/tmkv6RC/armflag.png",
    "USA ARMENIA": "https://i.ibb.co/tmkv6RC/armflag.png",
    "KINOMAN ARM": "https://i.ibb.co/tmkv6RC/armflag.png",
    "ARTN SHANT": "https://i.ibb.co/tmkv6RC/armflag.png",
    "AZ TV Azərbaycan Televiziyası": "https://i.ibb.co/VC7Q18V/azflag.png",
    "AZ TV": "https://i.ibb.co/VC7Q18V/azflag.png",
    "AZ STAR": "https://i.ibb.co/VC7Q18V/azflag.png",
    "ATV AZ": "https://i.ibb.co/VC7Q18V/azflag.png",
    "ICT TV": "https://i.ibb.co/VC7Q18V/azflag.png",
    "ARB": "https://i.ibb.co/VC7Q18V/azflag.png",
    "AZAD": "https://i.ibb.co/VC7Q18V/azflag.png",
    "CBC": "https://i.ibb.co/VC7Q18V/azflag.png",
    "BAKU TV": "https://i.ibb.co/VC7Q18V/azflag.png",
    "MEDENİYYET": "https://i.ibb.co/VC7Q18V/azflag.png",
    "SPACE TV": "https://i.ibb.co/VC7Q18V/azflag.png",
    "TMB AZ": "https://i.ibb.co/VC7Q18V/azflag.png",
    "XEZER TV": "https://i.ibb.co/VC7Q18V/azflag.png",
    "IRIB 2": "https://i.ibb.co/6ndKkPM/irib2.png",
    "IRIB 3": "https://i.ibb.co/4YQsfv9/irib3.png",
    "IRIB 4": "https://i.ibb.co/D5S2Q2z/irib4.png",
    "IRIB 1": "https://i.ibb.co/tMV7LBL/irib1.png",
    "IRIB 5 TEHRAN": "https://i.ibb.co/Kzb8VkY/irib5.png",
    "IRIB AMOOZESH": "https://i.ibb.co/GMLStpQ/amoozesh.png",
    "IRIB MOSTANAD": "https://i.ibb.co/1LmYfnH/mostanad.png",
    "IRIB NAMAYESH": "https://i.ibb.co/wsVP42F/namayesh.png",
    "IRIB NASIM": "https://i.ibb.co/pwxkFvX/nassim.jpg",
    "IRIB POOYA": "https://i.ibb.co/RgQXYbM/pooya.png",
    "IRIB SALAMAT": "https://i.ibb.co/wJHhH03/salamat.png",
    "IRIB TAMASHA": "https://i.ibb.co/PYMzQFX/tamasha.png",
    "IRIB VARZESH": "https://i.ibb.co/XsXzKJG/varzesh.png",
    "IRIB ESHAREH": "https://i.ibb.co/xHSzVy5/eshareh.png",
    "IRIB IRINN": "https://i.ibb.co/hVkbvpQ/irinn.png",
    "IRIB IRINN 2": "https://i.ibb.co/hVkbvpQ/irinn.png",
    "IFILM IR": "https://i.ibb.co/kDhcymF/ifilm.png",
    "IRIB TWSPORT": "https://i.ibb.co/X5KJmDS/aiosport1.jpg",
    "IRIB TWSPORT 2": "https://i.ibb.co/VDQwTkz/aiosport2.jpg",
    "IRIB TWSPORT 3": "https://i.ibb.co/X5KJmDS/aiosport1.jpg",
    "JJTV 1": "https://i.ibb.co/tqkV2sn/irflag.png",
    "JJTV 3": "https://i.ibb.co/tqkV2sn/irflag.png",
    "SEPEHR": "https://i.ibb.co/tqkV2sn/irflag.png",
    "OMID": "https://i.ibb.co/tqkV2sn/irflag.png",
    "OFOGH": "https://i.ibb.co/tqkV2sn/irflag.png",
    "PALESTINE": "https://i.ibb.co/tqkV2sn/irflag.png",
    "JAM": "https://i.ibb.co/tqkV2sn/irflag.png",
    "SHARAFGHAN": "https://i.ibb.co/tqkV2sn/irflag.png",
    "NAVA": "https://i.ibb.co/tqkV2sn/irflag.png",
    "NAMA": "https://i.ibb.co/tqkV2sn/irflag.png",
    "ARA": "https://i.ibb.co/tqkV2sn/irflag.png",
    "HABIB": "https://i.ibb.co/tqkV2sn/irflag.png",
    "AZARBAYJANGHARBI": "https://i.ibb.co/tqkV2sn/irflag.png",
    "SAHAND": "https://i.ibb.co/tqkV2sn/irflag.png",
    "ALBORZ": "https://i.ibb.co/tqkV2sn/irflag.png",
    "ESFAHAN": "https://i.ibb.co/tqkV2sn/irflag.png",
    "SABALAN": "https://i.ibb.co/tqkV2sn/irflag.png",
    "ILAM": "https://i.ibb.co/tqkV2sn/irflag.png",
    "BUSHEHR": "https://i.ibb.co/tqkV2sn/irflag.png",
    "JAHANBIN": "https://i.ibb.co/tqkV2sn/irflag.png",
    "ABADAN": "https://i.ibb.co/tqkV2sn/irflag.png",
    "KHORASANRAZAVI": "https://i.ibb.co/tqkV2sn/irflag.png",
    "ATRAK": "https://i.ibb.co/tqkV2sn/irflag.png",
    "KHALIJEFARS": "https://i.ibb.co/tqkV2sn/irflag.png",
    "KHOOZESTAN": "https://i.ibb.co/tqkV2sn/irflag.png",
    "SEMNAN": "https://i.ibb.co/tqkV2sn/irflag.png",
    "HAMOON": "https://i.ibb.co/tqkV2sn/irflag.png",
    "FARS": "https://i.ibb.co/tqkV2sn/irflag.png",
    "QAZVIN": "https://i.ibb.co/tqkV2sn/irflag.png",
    "NOOR": "https://i.ibb.co/tqkV2sn/irflag.png",
    "KERMAN": "https://i.ibb.co/tqkV2sn/irflag.png",
    "DENA": "https://i.ibb.co/tqkV2sn/irflag.png",
    "ZAGROS": "https://i.ibb.co/tqkV2sn/irflag.png",
    "KISH": "https://i.ibb.co/tqkV2sn/irflag.png",
    "SABZ": "https://i.ibb.co/tqkV2sn/irflag.png",
    "BARAN": "https://i.ibb.co/tqkV2sn/irflag.png",
    "KORDESTAN": "https://i.ibb.co/tqkV2sn/irflag.png",
    "TABAN": "https://i.ibb.co/tqkV2sn/irflag.png",
    "TABARESTAN": "https://i.ibb.co/tqkV2sn/irflag.png",
    "AFTAB": "https://i.ibb.co/tqkV2sn/irflag.png",
    "MAHABAD": "https://i.ibb.co/tqkV2sn/irflag.png",
    "SINA": "https://i.ibb.co/tqkV2sn/irflag.png",
    "KHAVARAN": "https://i.ibb.co/tqkV2sn/irflag.png",
    "IRIB IFILM FAR": "https://i.ibb.co/kDhcymF/ifilm.png",
    "MBC PERSIA": "https://i.ibb.co/tqkV2sn/irflag.png",
    "HASTI TV": "https://i.ibb.co/tqkV2sn/irflag.png",
    "ASIL TV": "https://i.ibb.co/tqkV2sn/irflag.png",
    "SNN TV": "https://i.ibb.co/tqkV2sn/irflag.png",
    "NEJAT TV": "https://i.ibb.co/tqkV2sn/irflag.png",
    "VOX 1": "https://i.ibb.co/tqkV2sn/irflag.png",
    "YOUR TIME": "https://i.ibb.co/tqkV2sn/irflag.png",
    "HOD HOD": "https://i.ibb.co/tqkV2sn/irflag.png",
    "24/7 BOX": "https://i.ibb.co/tqkV2sn/irflag.png",
    "OX IR": "https://i.ibb.co/tqkV2sn/irflag.png",
    "AVA FAMILY": "https://i.ibb.co/tqkV2sn/irflag.png",
    "PARS": "https://i.ibb.co/tqkV2sn/irflag.png",
    "SL ONE": "https://i.ibb.co/tqkV2sn/irflag.png",
    "SL TWO": "https://i.ibb.co/tqkV2sn/irflag.png",
    "P FILM": "https://i.ibb.co/tqkV2sn/irflag.png",
    "ITN": "https://i.ibb.co/tqkV2sn/irflag.png",
    "META FILM": "https://i.ibb.co/tqkV2sn/irflag.png",
    "AVA SERIES": "https://i.ibb.co/tqkV2sn/irflag.png",
    "BRAVOO": "https://i.ibb.co/tqkV2sn/irflag.png",
    "FX TV": "https://i.ibb.co/tqkV2sn/irflag.png",
    "OI TN": "https://i.ibb.co/tqkV2sn/irflag.png",
    "TAPESH": "https://i.ibb.co/tqkV2sn/irflag.png",
    "TAPESH IR": "https://i.ibb.co/tqkV2sn/irflag.png",
    "MIHAN TV": "https://i.ibb.co/tqkV2sn/irflag.png",
    "NEGAH TV": "https://i.ibb.co/tqkV2sn/irflag.png",
    "AL WILAYAH": "https://i.ibb.co/tqkV2sn/irflag.png",
    "PAYVAND": "https://i.ibb.co/tqkV2sn/irflag.png",
    "PJ TV": "https://i.ibb.co/tqkV2sn/irflag.png",
    "PMC TV": "https://i.ibb.co/tqkV2sn/irflag.png",
    "PERSIANA NOSTALGIA": "https://i.ibb.co/tqkV2sn/irflag.png",
    "PERSIANA MUSIC": "https://i.ibb.co/tqkV2sn/irflag.png",
    "PERSIANA TURKIYE": "https://i.ibb.co/tqkV2sn/irflag.png",
    "PERSIANA COMEDY": "https://i.ibb.co/tqkV2sn/irflag.png",
    "PERSIANA IRANIAN": "https://i.ibb.co/tqkV2sn/irflag.png",
    "PERSIANA ONE": "https://i.ibb.co/tqkV2sn/irflag.png",
    "PERSIANA TWO": "https://i.ibb.co/tqkV2sn/irflag.png",
    "PERSIANA KOREA": "https://i.ibb.co/tqkV2sn/irflag.png",
    "PERSIANA CINEMA": "https://i.ibb.co/tqkV2sn/irflag.png",
    "PERSIANA HD": "https://i.ibb.co/tqkV2sn/irflag.png",
    "PERSIANA LATINO": "https://i.ibb.co/tqkV2sn/irflag.png",
    "PERSIANA FAMILY": "https://i.ibb.co/tqkV2sn/irflag.png",
    "PERSIANA SCIENCE": "https://i.ibb.co/tqkV2sn/irflag.png",
    "PERSIANA JUNIOR": "https://i.ibb.co/tqkV2sn/irflag.png",
    "IRIB 5": "https://i.ibb.co/Kzb8VkY/irib5.png",
    "IRIB MESRAFSANJAN": "https://i.ibb.co/N6PTbMG/mesrafsanjan.png",
    "IRIB AIOSPORT": "https://i.ibb.co/X5KJmDS/aiosport1.jpg",
    "IRIB AIOSPORT 2": "https://i.ibb.co/VDQwTkz/aiosport2.jpg",
    "CNN INT": "https://i.ibb.co/XbSHxd5/cnn.png",
    "FOX NEWS": "https://i.ibb.co/hdBrzcc/fox.png",
    "NBC NEWS": "https://i.ibb.co/CKTjvj8/nbc.jpg",
    "ABC NEWS": "https://i.ibb.co/jJDxCxN/abc.jpg",
    "CBS NEWS": "https://i.ibb.co/YD3G64y/cbs.jpg",
    "CNBC NEWS": "https://i.ibb.co/FxZYHhM/cnbc.jpg",
    "CHEDDAR NEWS": "https://i.ibb.co/rH3FDN2/cheddar.jpg",
    "NEWS MAX": "https://i.ibb.co/yNdTPqt/newsmax.png",
    "REAL AMERICAS VOICE": "https://i.ibb.co/VMm5SSz/realamv.png",
    "USA TODAY": "https://i.ibb.co/nDJHCWt/Usatod.png",
    "OANN": "https://i.ibb.co/kX8ywwV/oan.png",
    "GLOBAL NEWS": "https://i.ibb.co/q0FfqdV/Globalnews.png",
    "BBC NEWS": "https://i.ibb.co/dPmZMqq/bbcn.png",
    "SKY NEWS": "https://i.ibb.co/8MBM4M1/skyn.png",
    "GB NEWS": "https://i.ibb.co/dpMQyVx/gbn.png",
    "TALK NEWS": "https://i.ibb.co/XWNXpVg/talk.png",
    "THE GUARDIAN CHANNEL": "https://i.ibb.co/GV4JLkr/Guardian.png",
    "FREE SPEECH TV": "https://i.ibb.co/W6TrwQx/freespech.png",
    "COURT TV": "https://i.ibb.co/Cs2Gv1ZG/courttv.jpg",
    "NEWS WORLD": "https://i.ibb.co/2YKQ7bR9/newsworld.jpg",
    "REUTERS TV": "https://i.ibb.co/DCntyzt/reuterstv.png",
    "VOA TV": "https://i.ibb.co/17rc425/voa.png",
    "C-SPAN": "https://i.ibb.co/x82vM4r9/Cspan.png",
    "BLOOMBERG UK": "https://i.ibb.co/Nn5x9Hq/bloom.jpg",
    "BLOOMBERG US": "https://i.ibb.co/Nn5x9Hq/bloom.jpg",
    "BLOOMBERG EU": "https://i.ibb.co/Nn5x9Hq/bloom.jpg",
    "BLOOMBERG QUICK": "https://i.ibb.co/Nn5x9Hq/bloom.jpg",
    "BLOOMBERG EVENT": "https://i.ibb.co/Nn5x9Hq/bloom.jpg",
    "BLOOMBERG ORIGINALS": "https://i.ibb.co/Nn5x9Hq/bloom.jpg",
    "EURONEWS EN": "https://i.ibb.co/R4xVMYc/enews.png",
    "AFRICANEWS EN": "https://i.ibb.co/XSYtYHZ/africanews.png",
    "EUROPE BY SAT": "https://i.ibb.co/gFjck13/ebssat.png",
    "EUROPE BY SAT +": "https://i.ibb.co/gFjck13/ebssat.png",
    "ABC NEWS AUSTRALIA": "https://i.ibb.co/mBTzvw8/Abcau.png",
    "SKY NEWS AUSTRALIA": "https://i.ibb.co/8MBM4M1/skyn.png",
    "INDIA TODAY": "https://i.ibb.co/94BB1cD/indiatod.jpg",
    "WION NEWS INDIA": "https://i.ibb.co/prZ8kjdR/Wion.png",
    "CHANNEL NEWS ASIA": "https://i.ibb.co/7J24bwVD/cnaid.png",
    "FRANCE 24 EN": "https://i.ibb.co/hKP8X8B/f24.png",
    "FRANCE 24 FAST": "https://i.ibb.co/hKP8X8B/f24.png",
    "DW ENGLISH": "https://i.ibb.co/84XLZJq/dw.png",
    "DW ENGLISH +": "https://i.ibb.co/84XLZJq/dw.png",
    "TELESUR EN": "https://i.ibb.co/NCQtNX5/telesur.png",
    "AFRICA 24 EN": "https://i.ibb.co/pdnMrZn/a24.png",
    "ARIRANG WORLD": "https://i.ibb.co/rtqXSWm/arirang.png",
    "KBS WORLD": "https://i.ibb.co/tQC0d8X/kbsw.jpg",
    "NHK WORLD": "https://i.ibb.co/JCjsXZm/nhk.png",
    "TRT WORLD": "https://i.ibb.co/nP9xpck/trtw.png",
    "TVP WORLD": "https://i.ibb.co/NrN5Gy2/tvpworld.png",
    "AL JAZEERA NEWS": "https://i.ibb.co/MGW5Vv9/aljaz.png",
    "CGTN NEWS": "https://i.ibb.co/s9gLmqv/cgtnch.png",
    "PRESS TV [censure-ifany]": "https://i.ibb.co/rwbrckj/pressir.png",
    "RT NEWS [censure-blocked]": "https://i.ibb.co/D7w9h7Q/rt.png",
    "CNN INT (backup)": "https://i.ibb.co/XbSHxd5/cnn.png",
    "CNN FAST (backup)": "https://i.ibb.co/XbSHxd5/cnn.png",
    "CNN INT [downlink]": "https://i.ibb.co/XbSHxd5/cnn.png",
    "SKY NEWS [deadlink]": "https://i.ibb.co/8MBM4M1/skyn.png",
    "SKY NEWS [diedlink]": "https://i.ibb.co/8MBM4M1/skyn.png",
    "TALK NEWS [geo-blocked]": "https://i.ibb.co/XWNXpVg/talk.png",
    "NBC NEWS [downlink]": "https://i.ibb.co/CKTjvj8/nbc.jpg",
    "BLOOMBERG EU [downlink]": "https://i.ibb.co/Nn5x9Hq/bloom.jpg",
    "EURONEWS EN [downlink]": "https://i.ibb.co/R4xVMYc/enews.png",
    "FOX NEWS [diedlink]": "https://i.ibb.co/hdBrzcc/fox.png",
    "DELUXE MUSIC English": "https://i.ibb.co/6t2ztJT/dlxmsc.png",
    "DELUXE MUSIC Flash Back": "https://i.ibb.co/jZWbT2g/dlxfbk.png",
    "DELUXE MUSIC Dance": "https://i.ibb.co/2ks2Ys7/dlxdnc.png",
    "DELUXE MUSIC Rap": "https://i.ibb.co/WBKwntS/dlxrap.png",
    "DELUXE MUSIC Rock": "https://i.ibb.co/mDFLYx3/dlxrck.png",
    "DELUXE MUSIC Deutsch Schlager": "https://i.ibb.co/TmL52ct/dlxde.png",
    "DELUXE MUSIC Deutsch Pop": "https://i.ibb.co/6RvHVvn/dlxdtschpp.png",
    "DELUXE MUSIC Winter Time": "https://i.ibb.co/1KhQxpd/dlxwnt.png",
    "DELUXE MUSIC Lounge": "https://i.ibb.co/RpfpWkr/dlxlng.png",
    "DELUXE MUSIC Lounge Extra": "https://i.ibb.co/pKt53kX/dl1.png",
}


STATIC_TV_NAMES = {
    "TV5MONDE FBSM": "TV5MONDE FBSM",
    "TF1": "TF1",
    "FRANCE 2": "FRANCE 2",
    "FRANCE 3": "FRANCE 3",
    "FRANCE 4": "FRANCE 4",
    "FRANCE 5": "FRANCE 5",
    "FRANCE TV SÉRIES": "FRANCE TV SÉRIES",
    "FRANCE TV DOCUMENTAIRES": "FRANCE TV DOCUMENTAIRES",
    "ARTE": "ARTE",
    "NRJ 12": "NRJ 12",
    "CHÉRIE 25": "CHÉRIE 25",
    "CANAL+ EN CLAIR": "CANAL+ EN CLAIR",
    "RMC STORY": "RMC STORY",
    "RMC DÉCOUVERTE": "RMC DÉCOUVERTE",
    "C8": "C8",
    "CSTAR": "CSTAR",
    "BFM TV": "BFM TV",
    "CNEWS": "CNEWS",
    "LCI": "LCI",
    "FRANCE INFO:": "FRANCE INFO:",
    "LE MÉDIA TV": "LE MÉDIA TV",
    "EURONEWS FR": "EURONEWS FR",
    "TV5MONDE INFO": "TV5MONDE INFO",
    "FRANCE 24 FR": "FRANCE 24 FR",
    "LCP-AN": "LCP-AN",
    "PUBLIC-SÉNAT": "PUBLIC-SÉNAT",
    "BFM 2": "BFM 2",
    "BFM GRAND REPORTAGES": "BFM GRAND REPORTAGES",
    "RMC TALK INFO": "RMC TALK INFO",
    "20 MINUTES TV IDF": "20 MINUTES TV IDF",
    "LE FIGARO IDF": "LE FIGARO IDF",
    "LE FIGARO LIVE": "LE FIGARO LIVE",
    "i24 NEWS FR": "i24 NEWS FR",
    "CGTN FRANÇAIS": "CGTN FRANÇAIS",
    "LN24 BE": "LN24 BE",
    "MONACO INFO": "MONACO INFO",
    "RDI CANADA": "RDI CANADA",
    "AFRICA 24 FR": "AFRICA 24 FR",
    "AFRICANEWS FR": "AFRICANEWS FR",
    "BFM BUSINESS": "BFM BUSINESS",
    "B SMART": "B SMART",
    "BLOOMBERG FR": "BLOOMBERG FR",
    "TV FINANCE": "TV FINANCE",
    "PRESS IR FRENCH [temp barker]": "PRESS IR FRENCH",
    "RT FRANÇAIS [censure-blocked]": "RT FRANÇAIS",
    "BFM TV (backup)": "BFM TV",
    "BFM 2 (backup)": "BFM 2",
    "BFM BUSINESS (backup)": "BFM BUSINESS",
    "LE MÉDIA TV (backup ok)": "LE MÉDIA TV",
    "LE MÉDIA TV (backup ko)": "LE MÉDIA TV",
    "EURONEWS FR (backup)": "EURONEWS FR",
    "FRANCE INFO: (backup)": "FRANCE INFO:",
    "FRANCE INFO: (backup-off)": "FRANCE INFO:",
    "FRANCE INFO: [find-host]": "FRANCE INFO:",
    "FRANCE 24 FR (backup)": "FRANCE 24 FR",
    "FRANCE 24 FR (backup-off)": "FRANCE 24 FR",
    "LCI (backup)": "LCI",
    "CNEWS (backup)": "CNEWS",
    "LE MÉDIA TV (backup)": "LE MÉDIA TV",
    "LCP-AN (backup)": "LCP-AN",
    "LE FIGARO IDF (backup)": "LE FIGARO IDF",
    "CGTN FRANÇAIS (backup)": "CGTN FRANÇAIS",
    "RDI CANADA (backup)": "RDI CANADA",
    "AFRICANEWS FR (backup)": "AFRICANEWS FR",
    "LCI [tkn-blocked]": "LCI",
    "TV5MONDE EUROPE [geo-area]": "TV5MONDE EUROPE",
    "TV5MONDE MOYEN-ORIENT [geo-area]": "TV5MONDE MOYEN-ORIENT",
    "TV5MONDE ASIE SUD-EST [geo-area]": "TV5MONDE ASIE SUD-EST",
    "TV5MONDE PACIFIQUE [geo-area]": "TV5MONDE PACIFIQUE",
    "CANAL+ EN CLAIR (backup)": "CANAL+ EN CLAIR",
    "C8 [tokenized]": "C8",
    "C8 [drm-keycrypted]": "C8",
    "CSTAR [drm-keycrypted]": "CSTAR",
    "CSTAR [tokenized]": "CSTAR",
    "RMC DÉCOUVERTE [drm-keycrypted]": "RMC DÉCOUVERTE",
    "RMC STORY [drm-keycrypted]": "RMC STORY",
    "M6 [drm-keycrypted]": "M6",
    "W9 [drm-keycrypted]": "W9",
    "6TER [drm-keycrypted]": "6TER",
    "M6 (backup)": "M6",
    "C8 (backup)": "C8",
    "TF1 (backup)": "TF1",
    "ARTE (backup)": "ARTE",
    "FRANCE 2 (backup)": "FRANCE 2",
    "FRANCE 3 (backup)": "FRANCE 3",
    "FRANCE 4 (backup)": "FRANCE 4",
    "FRANCE 5 (backup)": "FRANCE 5",
    "M6 (check)": "M6",
    "TMC (check)": "TMC",
    "W9 (check)": "W9",
    "FUN RADIO TV BE": "FUN RADIO TV BE",
    "FUN RADIO TV FR": "FUN RADIO TV FR",
    "GÉNÉRATIONS TV": "GÉNÉRATIONS TV",
    "MÉLODY": "MÉLODY",
    "CLUBBING TV": "CLUBBING TV",
    "TRACE URBAN": "TRACE URBAN",
    "TRACE SPORTS": "TRACE SPORTS",
    "SPORT EN FRANCE": "SPORT EN FRANCE",
    "L'ÉQUIPE LIVE 1": "L'ÉQUIPE LIVE 1",
    "L'ÉQUIPE LIVE 2": "L'ÉQUIPE LIVE 2",
    "L'ÉQUIPE LIVE FOOT": "L'ÉQUIPE LIVE FOOT",
    "L'ÉQUIPE TV": "L'ÉQUIPE TV",
    "RMC TALK SPORT": "RMC TALK SPORT",
    "JOURNAL DU GOLF": "JOURNAL DU GOLF",
    "L'ÉSPRIT SORCIER TV": "L'ÉSPRIT SORCIER TV",
    "SQOOL TV": "SQOOL TV",
    "GULLI": "GULLI",
    "GONG": "GONG",
    "SUPERTOONS FR": "SUPERTOONS FR",
    "PLUTO KIDS": "PLUTO KIDS",
    "VEVO POP": "VEVO POP",
    "VEVO HP RB": "VEVO HP RB",
    "VEVO 90 00": "VEVO 90 00",
    "MGG E-SPORT": "MGG E-SPORT",
    "MOTORVISION FR": "MOTORVISION FR",
    "MOTORVISION TV": "MOTORVISION TV",
    "MOTORVISION TV-2": "MOTORVISION TV-2",
    "TECH&CO": "TECH&CO",
    "MEN'S UP TV": "MEN'S UP TV",
    "TOP SANTÉ": "TOP SANTÉ",
    "MAISON & TRAVAUX": "MAISON & TRAVAUX",
    "TRAVEL XP": "TRAVEL XP",
    "TV5MONDE VOYAGE": "TV5MONDE VOYAGE",
    "NATURE TIME": "NATURE TIME",
    "VOYAGES ET SAVEURS": "VOYAGES ET SAVEURS",
    "PLUTO CUISINE": "PLUTO CUISINE",
    "RMC WOW": "RMC WOW",
    "RMC MYSTÈRE": "RMC MYSTÈRE",
    "RMC MECANIC": "RMC MECANIC",
    "RMC ALERTE SECOURS": "RMC ALERTE SECOURS",
    "ALLO CINÉ": "ALLO CINÉ",
    "RAKUTEN TOP FILMS TV": "RAKUTEN TOP FILMS TV",
    "WILD SIDE TV": "WILD SIDE TV",
    "TELE NOVELA TV": "TELE NOVELA TV",
    "BBLACK! AFRICA": "BBLACK! AFRICA",
    "BBLACK! CARIBBEAN": "BBLACK! CARIBBEAN",
    "BBLACK! CLASSIK": "BBLACK! CLASSIK",
    "UNIVERS CINÉ": "UNIVERS CINÉ",
    "PLUTO CINÉ": "PLUTO CINÉ",
    "PLUTO POLAR": "PLUTO POLAR",
    "CINÉ NANAR": "CINÉ NANAR",
    "CINÉ WESTERN": "CINÉ WESTERN",
    "KTO": "KTO",
    "DIEU TV": "DIEU TV",
    "EMCI TV": "EMCI TV",
    "MUSEUM": "MUSEUM",
    "MY ZEN": "MY ZEN",
    "MY ZEN WELLBEING": "MY ZEN WELLBEING",
    "FASHION TV": "FASHION TV",
    "TV5MONDE STYLE [geo-area]": "TV5MONDE STYLE",
    "TV5MONDE TiVi [geo-area]": "TV5MONDE TiVi",
    "GULLI (backup)": "GULLI",
    "FUN RADIO TV BE [died-link]": "FUN RADIO TV BE",
    "FUN RADIO TV BE (backup)": "FUN RADIO TV BE",
    "BFM ALPES": "BFM ALPES",
    "BFM ALSACE": "BFM ALSACE",
    "BFM H.PROVENCE": "BFM H.PROVENCE",
    "BFM LILLE": "BFM LILLE",
    "BFM LITTORAL": "BFM LITTORAL",
    "BFM LYON": "BFM LYON",
    "BFM MARSEILLE": "BFM MARSEILLE",
    "BFM NICE": "BFM NICE",
    "BFM NORMANDIE": "BFM NORMANDIE",
    "BFM PARIS": "BFM PARIS",
    "BFM TOULON": "BFM TOULON",
    "F3 PARIS IDF": "F3 PARIS IDF",
    "F3 PROVENCE ALPES": "F3 PROVENCE ALPES",
    "F3 CÔTE D'AZUR": "F3 CÔTE D'AZUR",
    "F3 RHÔNE ALPES": "F3 RHÔNE ALPES",
    "F3 ALPES": "F3 ALPES",
    "F3 AUVERGNE": "F3 AUVERGNE",
    "F3 BOURGOGNE": "F3 BOURGOGNE",
    "F3 FRANCHE COMPTÉ": "F3 FRANCHE COMPTÉ",
    "F3 CENTRE": "F3 CENTRE",
    "F3 CORSE VÍA STELLA": "F3 CORSE VÍA STELLA",
    "F3 ALSACE": "F3 ALSACE",
    "F3 CHAMPAGNE": "F3 CHAMPAGNE",
    "F3 LORRAINE": "F3 LORRAINE",
    "F3 NORD PDC": "F3 NORD PDC",
    "F3 PICARDIE": "F3 PICARDIE",
    "F3 B.NORMANDIE": "F3 B.NORMANDIE",
    "F3 H.NORMANDIE": "F3 H.NORMANDIE",
    "F3 AQUITAINE": "F3 AQUITAINE",
    "F3 NOA": "F3 NOA",
    "F3 LIMOUSIN": "F3 LIMOUSIN",
    "F3 POITOU CHARENTES": "F3 POITOU CHARENTES",
    "F3 MIDI PYRÉNÉES": "F3 MIDI PYRÉNÉES",
    "F3 LANGUEDOC": "F3 LANGUEDOC",
    "F3 PAYS LOIRE": "F3 PAYS LOIRE",
    "F3 BRETAGNE": "F3 BRETAGNE",
    "TÉBÉO TV": "TÉBÉO TV",
    "TVR RENNES": "TVR RENNES",
    "TÉLÉ NANTES": "TÉLÉ NANTES",
    "TV VENDÉE": "TV VENDÉE",
    "TV 78": "TV 78",
    "7A LIMOGES": "7A LIMOGES",
    "ALPE D'HUEZ TV": "ALPE D'HUEZ TV",
    "BIP TV": "BIP TV",
    "CANAL 32": "CANAL 32",
    "IL TV": "IL TV",
    "MOSELLE TV": "MOSELLE TV",
    "TV7 BORDEAUX": "TV7 BORDEAUX",
    "TV7 COLMAR": "TV7 COLMAR",
    "TV 3V": "TV 3V",
    "VIA MATÉLÉ": "VIA MATÉLÉ",
    "VIA OCCITANIE": "VIA OCCITANIE",
    "VIA TELEPAESE": "VIA TELEPAESE",
    "VOSGES TV": "VOSGES TV",
    "WÉO NORD": "WÉO NORD",
    "WÉO PICARDIE": "WÉO PICARDIE",
    "NANCY WEB TV": "NANCY WEB TV",
    "MAURIENNE TV": "MAURIENNE TV",
    "LA CHAÎNE 32": "LA CHAÎNE 32",
    "TÉLÉ GOHELLE": "TÉLÉ GOHELLE",
    "TVPI BAYONNE": "TVPI BAYONNE",
    "PUISSANCE TÉLÉVISION": "PUISSANCE TÉLÉVISION",
    "NA TV": "NA TV",
    "KANAL DUDE": "KANAL DUDE",
    "CANNES LÉRINS TV": "CANNES LÉRINS TV",
    "LITTORAL TV": "LITTORAL TV",
    "TV TARN": "TV TARN",
    "MOSAIK CRISTAL TV": "MOSAIK CRISTAL TV",
    "TV8 MONTBLANC": "TV8 MONTBLANC",
    "TVT TOURS": "TVT TOURS",
    "ANGERS TÉLÉ": "ANGERS TÉLÉ",
    "LYON CAPITALE TV": "LYON CAPITALE TV",
    "TL CHOLETAIS": "TL CHOLETAIS",
    "BRIONNAIS TV": "BRIONNAIS TV",
    "VALLOIRE TV": "VALLOIRE TV",
    "N31": "N31",
    "TÉLÉ GRENOBLE": "TÉLÉ GRENOBLE",
    "LM TV SARTHE": "LM TV SARTHE",
    "ASTV": "ASTV",
    "UBIZNEWS OM5TV": "UBIZNEWS OM5TV",
    "MADRAS FM TV": "MADRAS FM TV",
    "ANTENNE RÉUNION": "ANTENNE RÉUNION",
    "LA BRISE HAÏTI": "LA BRISE HAÏTI",
    "TNTV": "TNTV",
    "ETV GUADELOUPE": "ETV GUADELOUPE",
    "LA 1ÈRE MARTINIQUE [geo-area]": "LA 1ÈRE MARTINIQUE",
    "LA 1ÈRE GUADELOUPE [geo-area]": "LA 1ÈRE GUADELOUPE",
    "LA 1ÈRE GUYANE [geo-area]": "LA 1ÈRE GUYANE",
    "LA 1ÈRE MAYOTTE [geo-area]": "LA 1ÈRE MAYOTTE",
    "LA 1ÈRE RÉUNION [geo-area]": "LA 1ÈRE RÉUNION",
    "LA 1ÈRE N.CALÉDONIE [geo-area]": "LA 1ÈRE N.CALÉDONIE",
    "LA 1ÈRE POLYNÉSIE [geo-area]": "LA 1ÈRE POLYNÉSIE",
    "LA 1ÈRE WALLIS FUTUNA [geo-area]": "LA 1ÈRE WALLIS FUTUNA",
    "LA 1ÈRE SAINT-PIERRE MIQUELON [geo-area]": "LA 1ÈRE SAINT-PIERRE MIQUELON",
    "LA 1ÈRE MARTINIQUE (news only)": "LA 1ÈRE MARTINIQUE",
    "LA 1ÈRE GUADELOUPE (news only)": "LA 1ÈRE GUADELOUPE",
    "LA 1ÈRE GUYANE (news only)": "LA 1ÈRE GUYANE",
    "LA 1ÈRE MAYOTTE (news only)": "LA 1ÈRE MAYOTTE",
    "LA 1ÈRE RÉUNION (news only)": "LA 1ÈRE RÉUNION",
    "LA 1ÈRE N.CALÉDONIE (news only)": "LA 1ÈRE N.CALÉDONIE",
    "LA 1ÈRE POLYNÉSIE (news only)": "LA 1ÈRE POLYNÉSIE",
    "LA 1ÈRE WALLIS FUTUNA (news only)": "LA 1ÈRE WALLIS FUTUNA",
    "LA 1ÈRE SAINT-PIERRE MIQUELON (news only)": "LA 1ÈRE SAINT-PIERRE MIQUELON",
    "TV MONACO": "TV MONACO",
    "BEL RTL": "BEL RTL",
    "LA TÉLÉ": "LA TÉLÉ",
    "NO TÉLÉ": "NO TÉLÉ",
    "TÉLÉ BRUXELLES": "TÉLÉ BRUXELLES",
    "VEDIA": "VEDIA",
    "RTC TÉLÉ LIÈGE": "RTC TÉLÉ LIÈGE",
    "TÉLÉ MB": "TÉLÉ MB",
    "BOUKÈ": "BOUKÈ",
    "ANTENNE CENTRE": "ANTENNE CENTRE",
    "CANAL ZOOM": "CANAL ZOOM",
    "TV LUX": "TV LUX",
    "NOOVO": "NOOVO",
    "LÉMAN BLEU": "LÉMAN BLEU",
    "CARAC 1": "CARAC 1",
    "CARAC 2": "CARAC 2",
    "CARAC 3": "CARAC 3",
    "CARAC 4": "CARAC 4",
    "TVM 3": "TVM 3",
    "CANAL 9": "CANAL 9",
    "CANAL ALPHA": "CANAL ALPHA",
    "M LE MÉDIA": "M LE MÉDIA",
    "SAVOIR.MÉDIA": "SAVOIR.MÉDIA",
    "TÉLÉ QUÉBEC": "TÉLÉ QUÉBEC",
    "CPAC TV": "CPAC TV",
    "ICI MONTRÉAL": "ICI MONTRÉAL",
    "TRT HABER": "TRT HABER",
    "HABER TÜRK": "HABER TÜRK",
    "HABER GLOBAL": "HABER GLOBAL",
    "TV 100": "TV 100",
    "EKOL TV": "EKOL TV",
    "NTV": "NTV",
    "CNN TÜRK": "CNN TÜRK",
    "BLOOMBERG HT": "BLOOMBERG HT",
    "EKO TÜRK": "EKO TÜRK",
    "A PARA": "A PARA",
    "BUSINESS CHANNEL TÜRK": "BUSINESS CHANNEL TÜRK",
    "CNBC-e (weekday-time)": "CNBC-e",
    "TBMM TV": "TBMM TV",
    "DHA (feed 1)": "DHA",
    "DHA (feed 2)": "DHA",
    "AA (feed)": "AA",
    "TRT HABER (backup)": "TRT HABER",
    "HABER TÜRK (backup)": "HABER TÜRK",
    "HABER GLOBAL (backup)": "HABER GLOBAL",
    "HABER GLOBAL (off-action)": "HABER GLOBAL",
    "TV 100 (backup)": "TV 100",
    "CNN TÜRK (tokened)": "CNN TÜRK",
    "CNN TÜRK (backup)": "CNN TÜRK",
    "NTV (backup)": "NTV",
    "NTV (downline)": "NTV",
    "EKOL TV (backup)": "EKOL TV",
    "BLOOMBERG HT (backup)": "BLOOMBERG HT",
    "CNBC-e (weekday-time) [backup]": "CNBC-e",
    "FLASH HABER": "FLASH HABER",
    "SÖZCÜ TV": "SÖZCÜ TV",
    "KRT": "KRT",
    "TELE 1": "TELE 1",
    "HALK TV": "HALK TV",
    "ULUSAL KANAL": "ULUSAL KANAL",
    "TV 5": "TV 5",
    "BENGÜ TÜRK": "BENGÜ TÜRK",
    "TGRT HABER": "TGRT HABER",
    "TV NET": "TV NET",
    "24": "24",
    "A HABER": "A HABER",
    "ÜLKE": "ÜLKE",
    "AKIT TV": "AKIT TV",
    "ARTI TV": "ARTI TV",
    "YOL TV": "YOL TV",
    "SÖZCÜ TV (backup)": "SÖZCÜ TV",
    "KRT (backup)": "KRT",
    "HALK TV (backup)": "HALK TV",
    "ULUSAL KANAL (backup)": "ULUSAL KANAL",
    "BENGÜ TÜRK (backup)": "BENGÜ TÜRK",
    "TV NET (backup)": "TV NET",
    "TGRT HABER (backup)": "TGRT HABER",
    "24 (backup)": "24",
    "TV 5 (backup yt_ch)": "TV 5",
    "TV 5 (backup yt_vd)": "TV 5",
    "TRT 1": "TRT 1",
    "KANAL D": "KANAL D",
    "STAR": "STAR",
    "SHOW": "SHOW",
    "TV8": "TV8",
    "ATV": "ATV",
    "KANAL 7": "KANAL 7",
    "BEYAZ TV": "BEYAZ TV",
    "TRT 1 (backup)": "TRT 1",
    "KANAL D (backup)": "KANAL D",
    "STAR (backup)": "STAR",
    "SHOW [downline]": "SHOW",
    "NOW (backup)": "NOW",
    "ATV (backup)": "ATV",
    "ATV [youtube-src]": "ATV",
    "ATV [tkn-blocked]": "ATV",
    "TV8 (backup)": "TV8",
    "KANAL 7 (backup)": "KANAL 7",
    "BEYAZ TV (backup)": "BEYAZ TV",
    "TEVE 2 (backup)": "TEVE 2",
    "TRT BELGESEL": "TRT BELGESEL",
    "TRT 2": "TRT 2",
    "DMAX": "DMAX",
    "TLC TR": "TLC TR",
    "360": "360",
    "TV 4": "TV 4",
    "TİVİ 6": "TİVİ 6",
    "CİNE 1": "CİNE 1",
    "CINE5 TV": "CINE5 TV",
    "TÜRKİYE KLİNİKLERİ TV": "TÜRKİYE KLİNİKLERİ TV",
    "CGTN BELGESEL": "CGTN BELGESEL",
    "SAĞLIK CHANNEL": "SAĞLIK CHANNEL",
    "WOMAN KADIN TV": "WOMAN KADIN TV",
    "WOMAN LIFE TV": "WOMAN LIFE TV",
    "MOR TV": "MOR TV",
    "TEVE 2": "TEVE 2",
    "SHOW MAX": "SHOW MAX",
    "A2": "A2",
    "FİL TV": "FİL TV",
    "SHOW MAX (backup)": "SHOW MAX",
    "SHOW MAX [tkn-blocked]": "SHOW MAX",
    "A2 (backup)": "A2",
    "A2 [tkn-blocked]": "A2",
    "TRT BELGESEL (backup)": "TRT BELGESEL",
    "DMAX (backup)": "DMAX",
    "DMAX [downline]": "DMAX",
    "TLC TR [downline]": "TLC TR",
    "TLC TR (backup)": "TLC TR",
    "360 [tkn-blocked]": "360",
    "360 (backup)": "360",
    "WOMAN KADIN TV (backup)": "WOMAN KADIN TV",
    "TRT ÇOCUK": "TRT ÇOCUK",
    "TRT DİYANET ÇOCUK": "TRT DİYANET ÇOCUK",
    "DİYANET ÇOCUK TV": "DİYANET ÇOCUK TV",
    "CARTOON NETWORK TR": "CARTOON NETWORK TR",
    "GALATASARAY TV": "GALATASARAY TV",
    "FENERBAHÇE TV": "FENERBAHÇE TV",
    "HT SPOR": "HT SPOR",
    "BIS HABER": "BIS HABER",
    "A SPOR": "A SPOR",
    "SPORTS TV": "SPORTS TV",
    "TRT SPOR [geo-blocked]": "TRT SPOR",
    "TRT SPOR2 YILDIZ [geo-blocked]": "TRT SPOR2 YILDIZ",
    "TABİİ SPOR 1 [geoblocked]": "TABİİ SPOR 1",
    "TABİİ SPOR 2 [geoblocked]": "TABİİ SPOR 2",
    "TABİİ SPOR 3 [geoblocked]": "TABİİ SPOR 3",
    "TABİİ SPOR 4 [geoblocked]": "TABİİ SPOR 4",
    "TABİİ SPOR 5 [geoblocked]": "TABİİ SPOR 5",
    "TABİİ SPOR 6 [geoblocked]": "TABİİ SPOR 6",
    "TJK TV [geo-blocked]": "TJK TV",
    "TJK TV": "TJK TV",
    "BY HORSES TV": "BY HORSES TV",
    "TAY TV": "TAY TV",
    "TV8 BUÇUK": "TV8 BUÇUK",
    "TRT EBA TV": "TRT EBA TV",
    "MİNİKA ÇOCUK": "MİNİKA ÇOCUK",
    "MİNİKA GO": "MİNİKA GO",
    "HT SPOR (backup)": "HT SPOR",
    "BIS HABER (backup)": "BIS HABER",
    "TRT SPOR (backup)": "TRT SPOR",
    "TRT SPOR2 YILDIZ (backup)": "TRT SPOR2 YILDIZ",
    "TRT3 SPOR [offline]": "TRT3 SPOR",
    "TRT ÇOCUK (backup)": "TRT ÇOCUK",
    "SPORTS TV (backup)": "SPORTS TV",
    "TV8 BUÇUK (backup)": "TV8 BUÇUK",
    "TV8 BUÇUK [tkn-blocked]": "TV8 BUÇUK",
    "A SPOR (backup)": "A SPOR",
    "A SPOR [tkn-blocked]": "A SPOR",
    "TRT MÜZİK": "TRT MÜZİK",
    "SPOTIFY TURKEY • TRLIST 👤": "SPOTIFY TURKEY • TRLIST 👤",
    "SPOTIFY TURKEY • 2024 🎧": "SPOTIFY TURKEY • 2024 🎧",
    "KRAL - KRAL POP": "KRAL - KRAL POP",
    "DREAM TÜRK": "DREAM TÜRK",
    "POWER TÜRK": "POWER TÜRK",
    "POWER TÜRK TAPTAZE": "POWER TÜRK TAPTAZE",
    "POWER TÜRK SLOW": "POWER TÜRK SLOW",
    "POWER TÜRK AKUSTİK": "POWER TÜRK AKUSTİK",
    "TATLISES": "TATLISES",
    "MİLYON TV": "MİLYON TV",
    "NUMBER ONE TÜRK": "NUMBER ONE TÜRK",
    "NUMBER ONE TÜRK ASK": "NUMBER ONE TÜRK ASK",
    "NUMBER ONE TÜRK DAMAR": "NUMBER ONE TÜRK DAMAR",
    "NUMBER ONE TÜRK DANCE": "NUMBER ONE TÜRK DANCE",
    "NUMBER ONE": "NUMBER ONE",
    "FASHION ONE": "FASHION ONE",
    "POWER TV": "POWER TV",
    "POWER DANCE": "POWER DANCE",
    "POWER LOVE": "POWER LOVE",
    "NUMBER ONE (backup)": "NUMBER ONE",
    "KRAL - KRAL POP (backup)": "KRAL - KRAL POP",
    "DİNÎ, DİĞER",TRT AVAZ": "DİNÎ, DİĞER",TRT AVAZ",
    "TRT TÜRK": "TRT TÜRK",
    "KANAL 7 AVRUPA": "KANAL 7 AVRUPA",
    "SHOW TÜRK": "SHOW TÜRK",
    "EURO D": "EURO D",
    "EURO D (geçici geçerli)": "EURO D",
    "EURO STAR": "EURO STAR",
    "EURO STAR (geçici geçerli)": "EURO STAR",
    "ATV AVRUPA (geçici geçerli)": "ATV AVRUPA",
    "TV8 INT (geçici geçerli)": "TV8 INT",
    "TGRT EU": "TGRT EU",
    "AGRO TV": "AGRO TV",
    "ÇİFTÇİ TV": "ÇİFTÇİ TV",
    "TARIM TV": "TARIM TV",
    "MELTEM": "MELTEM",
    "KANAL B": "KANAL B",
    "EM TV": "EM TV",
    "DİYANET TV": "DİYANET TV",
    "SEMERKAND": "SEMERKAND",
    "SEMERKAND WAY": "SEMERKAND WAY",
    "DOST TV": "DOST TV",
    "REHBER TV": "REHBER TV",
    "LALEGÜL TV": "LALEGÜL TV",
    "BERAT TV": "BERAT TV",
    "CAN TV": "CAN TV",
    "ON4 TV": "ON4 TV",
    "AFRO TURK TV": "AFRO TURK TV",
    "LUYS TV": "LUYS TV",
    "SAT 7 TÜRK": "SAT 7 TÜRK",
    "KANAL HAYAT": "KANAL HAYAT",
    "ABN TURKEY": "ABN TURKEY",
    "TGRT BELGESEL": "TGRT BELGESEL",
    "TGRT EU (backup)": "TGRT EU",
    "TGRT BELGESEL (backup)": "TGRT BELGESEL",
    "TGRT BELGESEL (checkalt)": "TGRT BELGESEL",
    "KANAL 7 AVRUPA [off-link]": "KANAL 7 AVRUPA",
    "KANAL 7 AVRUPA (backup)": "KANAL 7 AVRUPA",
    "SHOW TÜRK (geçici geçerli)": "SHOW TÜRK",
    "ANADOLU NET TV": "ANADOLU NET TV",
    "AKSU TV KAHRAMANMARAŞ": "AKSU TV KAHRAMANMARAŞ",
    "ALANYA POSTA TV": "ALANYA POSTA TV",
    "ALANYA TV": "ALANYA TV",
    "ALTAS TV ORDU": "ALTAS TV ORDU",
    "ART AMASYA": "ART AMASYA",
    "AS TV BURSA": "AS TV BURSA",
    "BARTIN TV": "BARTIN TV",
    "BEYKENT TV": "BEYKENT TV",
    "BİR TV İZMİR": "BİR TV İZMİR",
    "BRTV KARABÜK": "BRTV KARABÜK",
    "BURSA LINE TV": "BURSA LINE TV",
    "BURSA ON6 TV": "BURSA ON6 TV",
    "BÜLTEN TV ANKARA": "BÜLTEN TV ANKARA",
    "ÇAY TV RİZE": "ÇAY TV RİZE",
    "ÇEKMEKÖY BELEDİYE TV": "ÇEKMEKÖY BELEDİYE TV",
    "ÇORUM BLD TV": "ÇORUM BLD TV",
    "DEHA TV DENİZLİ": "DEHA TV DENİZLİ",
    "DENİZ POSTASI TV": "DENİZ POSTASI TV",
    "DİM TV ALANYA": "DİM TV ALANYA",
    "DİYAR TV": "DİYAR TV",
    "DRT DENİZLİ": "DRT DENİZLİ",
    "DÜĞÜN TV ÇİNE": "DÜĞÜN TV ÇİNE",
    "EDESSA TV ŞANLIURFA": "EDESSA TV ŞANLIURFA",
    "EGE TV İZMİR": "EGE TV İZMİR",
    "EGE LIVE TV": "EGE LIVE TV",
    "ELMAS TV ZONGULDAK": "ELMAS TV ZONGULDAK",
    "ER TV MALATYA": "ER TV MALATYA",
    "ERCİS TV": "ERCİS TV",
    "ERCİYES TV": "ERCİYES TV",
    "ERT ŞAH TV ERZİNCAN": "ERT ŞAH TV ERZİNCAN",
    "ERZURUM WEB TV": "ERZURUM WEB TV",
    "ES TV ESKİŞEHİR": "ES TV ESKİŞEHİR",
    "EDİRNE TV": "EDİRNE TV",
    "EFES DOST TV": "EFES DOST TV",
    "ESENLER ŞEHİR TV": "ESENLER ŞEHİR TV",
    "ETV KAYSERİ": "ETV KAYSERİ",
    "FRT FETHİYE": "FRT FETHİYE",
    "GRT GAZİANTEP TV": "GRT GAZİANTEP TV",
    "GÜNEY TV TARSUS": "GÜNEY TV TARSUS",
    "GÜNEYDOĞU TV": "GÜNEYDOĞU TV",
    "GURBET 24 TV": "GURBET 24 TV",
    "HEDEF TV KOCAELİ": "HEDEF TV KOCAELİ",
    "HABER61 TRABZON": "HABER61 TRABZON",
    "HRT HATAY AKDENİZ": "HRT HATAY AKDENİZ",
    "HUNAT TV KAYSERİ": "HUNAT TV KAYSERİ",
    "İÇEL TV MERSİN": "İÇEL TV MERSİN",
    "İZMİR TIME 35 TV": "İZMİR TIME 35 TV",
    "İZMİR TÜRK TV": "İZMİR TÜRK TV",
    "LİDER HABER TV": "LİDER HABER TV",
    "KANAL 15 BURDUR": "KANAL 15 BURDUR",
    "KANAL 19 ÇORUM": "KANAL 19 ÇORUM",
    "KANAL 23 ELAZIĞ": "KANAL 23 ELAZIĞ",
    "KANAL 26 ESKİŞEHİR": "KANAL 26 ESKİŞEHİR",
    "KANAL 3 AFYONKARAHİSAR": "KANAL 3 AFYONKARAHİSAR",
    "KANAL 32 ISPARTA": "KANAL 32 ISPARTA",
    "KANAL 33 MERSİN": "KANAL 33 MERSİN",
    "KANAL 34 İSTANBUL": "KANAL 34 İSTANBUL",
    "KANAL 53 RİZE": "KANAL 53 RİZE",
    "KANAL 56 SİİRT": "KANAL 56 SİİRT",
    "KANAL 58 SİVAS": "KANAL 58 SİVAS",
    "KANAL 68 AKSARAY": "KANAL 68 AKSARAY",
    "KANAL EGE": "KANAL EGE",
    "KANAL FIRAT": "KANAL FIRAT",
    "KANAL S SAMSUN": "KANAL S SAMSUN",
    "KANAL URFA": "KANAL URFA",
    "KANAL V ANTALYA": "KANAL V ANTALYA",
    "KANAL Z ZONGULDAK": "KANAL Z ZONGULDAK",
    "KASTAMONU TV": "KASTAMONU TV",
    "KARABÜK DERİN TV": "KARABÜK DERİN TV",
    "KARDELEN TV": "KARDELEN TV",
    "KAY TV KAYSERİ": "KAY TV KAYSERİ",
    "KEÇİÖREN TV ANKARA": "KEÇİÖREN TV ANKARA",
    "KENT 38 TV KAYSERİ": "KENT 38 TV KAYSERİ",
    "KENT TV BODRUM": "KENT TV BODRUM",
    "KOCAELİ TV": "KOCAELİ TV",
    "KONYA KTV": "KONYA KTV",
    "KONYA OLAY TV": "KONYA OLAY TV",
    "KOZA TV ADANA": "KOZA TV ADANA",
    "KIBRIS BRT 1": "KIBRIS BRT 1",
    "KIBRIS BRT 2": "KIBRIS BRT 2",
    "KIBRIS BRT 3": "KIBRIS BRT 3",
    "KIBRIS ADA TV": "KIBRIS ADA TV",
    "KIBRIS KANAL T": "KIBRIS KANAL T",
    "KIBRIS GENÇ TV": "KIBRIS GENÇ TV",
    "KIBRIS TV": "KIBRIS TV",
    "KIBRIS SİM TV": "KIBRIS SİM TV",
    "KIBRIS TV2020": "KIBRIS TV2020",
    "KIBRIS KK TV": "KIBRIS KK TV",
    "LIFE TV KAYSERİ": "LIFE TV KAYSERİ",
    "MALATYA VUSLAT TV": "MALATYA VUSLAT TV",
    "MANISA ETV": "MANISA ETV",
    "MARMARİS TV": "MARMARİS TV",
    "MAVİ KARADENİZ TV": "MAVİ KARADENİZ TV",
    "MERCAN TV ADIYAMAN": "MERCAN TV ADIYAMAN",
    "METROPOL DENİZLİ": "METROPOL DENİZLİ",
    "MUĞLA MERKEZ TV": "MUĞLA MERKEZ TV",
    "MUĞLA TÜRK TV": "MUĞLA TÜRK TV",
    "NOKTA TV KOCAELİ": "NOKTA TV KOCAELİ",
    "NORA TV AKSARAY": "NORA TV AKSARAY",
    "OGUN TV": "OGUN TV",
    "OLAY TÜRK KAYSERİ TV": "OLAY TÜRK KAYSERİ TV",
    "OLAY TV BURSA": "OLAY TV BURSA",
    "ORDU BEL TV": "ORDU BEL TV",
    "ORT OSMANİYE TV": "ORT OSMANİYE TV",
    "PAMUKKALE TV": "PAMUKKALE TV",
    "POSTA TV ALANYA": "POSTA TV ALANYA",
    "RADYO KARDEŞ TV FR": "RADYO KARDEŞ TV FR",
    "RİZE TÜRK TV": "RİZE TÜRK TV",
    "SARIYER TV İST": "SARIYER TV İST",
    "SILKWAY KAZAKH (TUR)": "SILKWAY KAZAKH",
    "SİNOP YILDIZ TV": "SİNOP YILDIZ TV",
    "SKYHABER TV": "SKYHABER TV",
    "SLOW KARADENİZ TV": "SLOW KARADENİZ TV",
    "SUN RTV MERSİN": "SUN RTV MERSİN",
    "RUMELİ TV": "RUMELİ TV",
    "TEK RUMELİ TV": "TEK RUMELİ TV",
    "TEMPO TV": "TEMPO TV",
    "TV 1 ADANA": "TV 1 ADANA",
    "TİVİ TURK": "TİVİ TURK",
    "TON TV ÇANAKKALE": "TON TV ÇANAKKALE",
    "TOKAT TV": "TOKAT TV",
    "TRABZON TV": "TRABZON TV",
    "TRAKYA TÜRK": "TRAKYA TÜRK",
    "TURHAL WEB TV": "TURHAL WEB TV",
    "TV KAYSERİ": "TV KAYSERİ",
    "TV 1 KAYSERİ": "TV 1 KAYSERİ",
    "TV 25 DOĞU": "TV 25 DOĞU",
    "TV 264 SAKARYA": "TV 264 SAKARYA",
    "TV 35 İZMİR": "TV 35 İZMİR",
    "TV 41 KOCAELİ": "TV 41 KOCAELİ",
    "TV 48 MİLAS": "TV 48 MİLAS",
    "TV 52 ORDU": "TV 52 ORDU",
    "TVO ANTALYA": "TVO ANTALYA",
    "TV DEN AYDIN": "TV DEN AYDIN",
    "TÜRKMENELİ TV": "TÜRKMENELİ TV",
    "UR FANATİK TV": "UR FANATİK TV",
    "ÜSKÜDAR UNİVERSİTE TV": "ÜSKÜDAR UNİVERSİTE TV",
    "VAN GÖLÜ TV": "VAN GÖLÜ TV",
    "VİYANA TV": "VİYANA TV",
    "YAŞAM TV": "YAŞAM TV",
    "WORLD TÜRK TV": "WORLD TÜRK TV",
    "YOZGAT BLD TV": "YOZGAT BLD TV",
    "ZAROK KURMANÎ": "ZAROK KURMANÎ",
    "ZAROK SORANÎ": "ZAROK SORANÎ",
    "TRT KURDÎ": "TRT KURDÎ",
    "ZAGROS TV": "ZAGROS TV",
    "KURDMAX SHOW": "KURDMAX SHOW",
    "KURDMAX SORANÎ": "KURDMAX SORANÎ",
    "RÛDAW TV": "RÛDAW TV",
    "KURD CHANNEL": "KURD CHANNEL",
    "KURDISTAN 24": "KURDISTAN 24",
    "KURDISTAN TV": "KURDISTAN TV",
    "KURDSAT": "KURDSAT",
    "KURDSAT NEWS": "KURDSAT NEWS",
    "KURDMAX MUSIC": "KURDMAX MUSIC",
    "GELÎ KURDISTAN TV": "GELÎ KURDISTAN TV",
    "KOMALA TV": "KOMALA TV",
    "JÎN TV": "JÎN TV",
    "CÎHAN TV": "CÎHAN TV",
    "ERT WORLD": "ERT WORLD",
    "ERT NEWS": "ERT NEWS",
    "ERT 1 [geoblocked]": "ERT 1",
    "ERT 2 [geoblocked]": "ERT 2",
    "ERT 3 [geoblocked]": "ERT 3",
    "ERT KIDS [geoblocked]": "ERT KIDS",
    "ERT MUSIC [geoblocked]": "ERT MUSIC",
    "ERT SPORTS [geoblocked]": "ERT SPORTS",
    "ALPHA TV": "ALPHA TV",
    "ANT 1": "ANT 1",
    "SKAI": "SKAI",
    "MEGA": "MEGA",
    "MAK TV": "MAK TV",
    "NETMAX TV": "NETMAX TV",
    "OPEN TV": "OPEN TV",
    "ATTICA": "ATTICA",
    "SIGMA TV": "SIGMA TV",
    "MAGIC TV": "MAGIC TV",
    "MAKEDONIA TV": "MAKEDONIA TV",
    "NET TV TORONTO": "NET TV TORONTO",
    "NET TV EUROPE": "NET TV EUROPE",
    "NET MAX TV": "NET MAX TV",
    "ANT 1 DRAMA": "ANT 1 DRAMA",
    "MAD WORLD": "MAD WORLD",
    "RIK SAT CYPRUS": "RIK SAT CYPRUS",
    "ACTION 24": "ACTION 24",
    "GROOVY TV": "GROOVY TV",
    "NEA CRETE TV": "NEA CRETE TV",
    "BARAZA RELAXING TV": "BARAZA RELAXING TV",
    "XALASTRA TV": "XALASTRA TV",
    "NRG TV": "NRG TV",
    "BOYAH TV": "BOYAH TV",
    "AEOLOS": "AEOLOS",
    "EXPLORE": "EXPLORE",
    "TOP CHANNEL": "TOP CHANNEL",
    "ράκη Νετ TV": "ράκη Νετ TV",
    "TELE ΚΡΗΤΗ": "TELE ΚΡΗΤΗ",
    "START TV": "START TV",
    "PELLA TV": "PELLA TV",
    "KONTRA TV": "KONTRA TV",
    "HIGH TV": "HIGH TV",
    "HELLENIC TV": "HELLENIC TV",
    "GREEK TV LONDON": "GREEK TV LONDON",
    "GRD CHANNEL": "GRD CHANNEL",
    "CRETA": "CRETA",
    "CORFU": "CORFU",
    "BLUE SKY": "BLUE SKY",
    "ERT NEWS 2": "ERT NEWS 2",
    "ERT NEWS 3": "ERT NEWS 3",
    "ERT WORLD (backup)": "ERT WORLD",
    "ERT NEWS (backup)": "ERT NEWS",
    "RIK SAT CYPRUS [geoblocked]": "RIK SAT CYPRUS",
    "EURONEWS PT": "EURONEWS PT",
    "CNN PORTUGAL": "CNN PORTUGAL",
    "SIC NOTÍCIAS": "SIC NOTÍCIAS",
    "SIC": "SIC",
    "TVI": "TVI",
    "TVI INT": "TVI INT",
    "TVI V+": "TVI V+",
    "TVI REALITY": "TVI REALITY",
    "SIC NOVELAS": "SIC NOVELAS",
    "SIC REPLAY": "SIC REPLAY",
    "SIC HD ALTA DEFINIÇÃO": "SIC HD ALTA DEFINIÇÃO",
    "PORTO CANAL": "PORTO CANAL",
    "TVI AFRICA": "TVI AFRICA",
    "AR PARLAMENTO": "AR PARLAMENTO",
    "ADB TV": "ADB TV",
    "MCA": "MCA",
    "FAMA FM TV": "FAMA FM TV",
    "KURIAKOS CINE": "KURIAKOS CINE",
    "KURIAKOS KIDS": "KURIAKOS KIDS",
    "TRACE BRAZUCA": "TRACE BRAZUCA",
    "RTP 1 (backup sd)": "RTP 1",
    "RTP 2 (backup sd)": "RTP 2",
    "RTP 3 (backup sd)": "RTP 3",
    "RTP 3 (tvhlsdvr)": "RTP 3",
    "RTP 3 (tvhlsdvr_HD)": "RTP 3",
    "RTP ACORES (backup)": "RTP ACORES",
    "EURONEWS PT (backup)": "EURONEWS PT",
    "CNN PORTUGAL (backup)": "CNN PORTUGAL",
    "SIC NOTÍCIAS (backup)": "SIC NOTÍCIAS",
    "SIC NOVELAS (backup)": "SIC NOVELAS",
    "TVI V+ (ex-TVI FICCAO)": "TVI V+",
    "CNN PORTUGAL [find-host]": "CNN PORTUGAL",
    "TVI [find-host]": "TVI",
    "TVI INT [find-host]": "TVI INT",
    "CNN PORTUGAL [tkn-blocked]": "CNN PORTUGAL",
    "TVI [tkn-blocked]": "TVI",
    "TVI INT [tkn-blocked]": "TVI INT",
    "TVI FICCAO [tkn-blocked]": "TVI FICCAO",
    "TVI REALITY [tkn-blocked]": "TVI REALITY",
    "SIC NOVELAS [offline]": "SIC NOVELAS",
    "TVE INTERNACIONAL": "TVE INTERNACIONAL",
    "TVE LA 1": "TVE LA 1",
    "TVE LA 2": "TVE LA 2",
    "TVE 24 H": "TVE 24 H",
    "STAR TVE": "STAR TVE",
    "TVE TDP": "TVE TDP",
    "TVE CLAN": "TVE CLAN",
    "ANTENNA 3": "ANTENNA 3",
    "CUATRO": "CUATRO",
    "TELECINCO": "TELECINCO",
    "LA SEXTA": "LA SEXTA",
    "TVE SOMOS CINE [geo-limited]": "TVE SOMOS CINE",
    "RTVE PLAY CADENA 1": "RTVE PLAY CADENA 1",
    "RTVE PLAY CADENA 2": "RTVE PLAY CADENA 2",
    "RTVE PLAY CADENA 3": "RTVE PLAY CADENA 3",
    "RTVE PLAY CADENA 4": "RTVE PLAY CADENA 4",
    "RTVE": "RTVE",
    "EURONEWS ES": "EURONEWS ES",
    "EL PAIS": "EL PAIS",
    "EL CONFIDENCIAL TV": "EL CONFIDENCIAL TV",
    "CANAL PARLAMENTO": "CANAL PARLAMENTO",
    "CANAL DIPUTADOS": "CANAL DIPUTADOS",
    "SOL MÙSICA": "SOL MÙSICA",
    "TRECE": "TRECE",
    "TRECE INT": "TRECE INT",
    "ATRES SERIES": "ATRES SERIES",
    "ATRES CLÁSICOS": "ATRES CLÁSICOS",
    "ATRES COMEDIA": "ATRES COMEDIA",
    "ATRES FLOOXER": "ATRES FLOOXER",
    "ATRES MULTICINE": "ATRES MULTICINE",
    "ATRES KIDZ": "ATRES KIDZ",
    "PEQUE TV": "PEQUE TV",
    "CARTOON NETWORK ES": "CARTOON NETWORK ES",
    "VIVE KANAL D DRAMA": "VIVE KANAL D DRAMA",
    "TRACE LATINA": "TRACE LATINA",
    "REAL MADRID CINEVERSE": "REAL MADRID CINEVERSE",
    "REAL MADRID TV": "REAL MADRID TV",
    "EL TORO TV": "EL TORO TV",
    "SUR 1 ANDALUCÍA": "SUR 1 ANDALUCÍA",
    "SUR 2 ANDALUCÍA": "SUR 2 ANDALUCÍA",
    "SUR NOTICIAS ANDALUCÍA": "SUR NOTICIAS ANDALUCÍA",
    "CINE ANDALUCÍA": "CINE ANDALUCÍA",
    "COCINA ANDALUCÍA": "COCINA ANDALUCÍA",
    "TURISMO ANDALUCÍA": "TURISMO ANDALUCÍA",
    "ARAGÓN TV": "ARAGÓN TV",
    "ARAGÓN NOTICIAS": "ARAGÓN NOTICIAS",
    "LA 1 CANARIAS": "LA 1 CANARIAS",
    "LA 2 CANARIAS": "LA 2 CANARIAS",
    "24 H CANARIAS": "24 H CANARIAS",
    "CASTILLA MEDIA": "CASTILLA MEDIA",
    "LA 1 CATALUNYA": "LA 1 CATALUNYA",
    "LA 2 CATALUNYA": "LA 2 CATALUNYA",
    "24 H CATALUNYA": "24 H CATALUNYA",
    "TV3 CATALUNYA INT": "TV3 CATALUNYA INT",
    "TV3 CATALUNYA 24H": "TV3 CATALUNYA 24H",
    "TV3 CATALUNYA FAST 1": "TV3 CATALUNYA FAST 1",
    "TV3 CATALUNYA FAST 2": "TV3 CATALUNYA FAST 2",
    "TV3 CATALUNYA LOC": "TV3 CATALUNYA LOC",
    "TV3 CATALUNYA C33": "TV3 CATALUNYA C33",
    "CATALUNYA BON DIA TV": "CATALUNYA BON DIA TV",
    "INFOCIUDADES TV CATALUNYA": "INFOCIUDADES TV CATALUNYA",
    "CATALUNYA 8": "CATALUNYA 8",
    "TENERIFE 4": "TENERIFE 4",
    "CEUTA RTV": "CEUTA RTV",
    "TELE MADRID": "TELE MADRID",
    "TELE MADRID INT": "TELE MADRID INT",
    "TELE MADRID OTRA": "TELE MADRID OTRA",
    "CANAL EXTRAMADURA": "CANAL EXTRAMADURA",
    "TVG GALICIA EU": "TVG GALICIA EU",
    "TVG GALICIA AM": "TVG GALICIA AM",
    "TVG GALICIA MO": "TVG GALICIA MO",
    "TVG CULTURAL": "TVG CULTURAL",
    "TVG INFANTIL": "TVG INFANTIL",
    "TVG 2": "TVG 2",
    "EITB 1": "EITB 1",
    "EITB 2": "EITB 2",
    "EITB INT": "EITB INT",
    "EITB DEPORTE": "EITB DEPORTE",
    "ANDORRA DIFUSIÓ": "ANDORRA DIFUSIÓ",
    "TV CANARIA": "TV CANARIA",
    "TV RIOJA": "TV RIOJA",
    "RIOJA COCINA": "RIOJA COCINA",
    "101TV SEVILLA": "101TV SEVILLA",
    "TELESUR": "TELESUR",
    "FRANCE 24 ES": "FRANCE 24 ES",
    "DW ESPAÑOL": "DW ESPAÑOL",
    "NHK WORLD ESP": "NHK WORLD ESP",
    "CGTN ESPAÑOL": "CGTN ESPAÑOL",
    "PRESS HISPAN TV": "PRESS HISPAN TV",
    "CNN EN ESPAÑOL [geoblocked]": "CNN EN ESPAÑOL",
    "RT ESPAÑOL [censure-blocked]": "RT ESPAÑOL",
    "EURONEWS ES (backup)": "EURONEWS ES",
    "TVE LA 1 (backup)": "TVE LA 1",
    "TVE LA 2 (backup)": "TVE LA 2",
    "TVE 24 H (backup)": "TVE 24 H",
    "TVE INTERNACIONAL (backup)": "TVE INTERNACIONAL",
    "TVE INTERNACIONAL (america)": "TVE INTERNACIONAL",
    "TVE SOMOS CINE (backup)": "TVE SOMOS CINE",
    "STAR TVE (espana)": "STAR TVE",
    "TVE CLAN [geo-restricted]": "TVE CLAN",
    "TENERIFE 4 (offlink)": "TENERIFE 4",
    "TELE MADRID (offlink)": "TELE MADRID",
    "2M MONDE الثانية": "2M MONDE الثانية",
    "M24 TV للأنباء": "M24 TV للأنباء",
    "TELE MAROC قناة المغرب": "TELE MAROC قناة المغرب",
    "MEDI 1 MG العربية": "MEDI 1 MG العربية",
    "MEDI 1 AR العربية": "MEDI 1 AR العربية",
    "MEDI 1 FR العربية": "MEDI 1 FR العربية",
    "CHADA TV شدى": "CHADA TV شدى",
    "WATANIA 1": "WATANIA 1",
    "WATANIA 2": "WATANIA 2",
    "ATTASIA 9": "ATTASIA 9",
    "TV2 ALGÉRIE": "TV2 ALGÉRIE",
    "CNA": "CNA",
    "WATANIA 1 (backup)": "WATANIA 1",
    "WATANIA 2 (backup)": "WATANIA 2",
    "CHADA TV شدى (backup)": "CHADA TV شدى",
    "MEDI 1 MG العربية (backup)": "MEDI 1 MG العربية",
    "MEDI 1 AR العربية (backup)": "MEDI 1 AR العربية",
    "MEDI 1 FR العربية (backup)": "MEDI 1 FR العربية",
    "MEDI 1 MG العربية (off-backup)": "MEDI 1 MG العربية",
    "AL AOULA LAÂYOUNE الأولى (backup)": "AL AOULA LAÂYOUNE الأولى",
    "Al AOULA INT الأولى (backup)": "Al AOULA INT الأولى",
    "2M MONDE الثانية (backup)": "2M MONDE الثانية",
    "ARRYADIA الرياضية (backup)": "ARRYADIA الرياضية",
    "ATHAQAFIA الثقافية (backup)": "ATHAQAFIA الثقافية",
    "AL MAGHRIBIA المغربية الإخبارية (backup)": "AL MAGHRIBIA المغربية الإخبارية",
    "ASSADISSA القرآن الكريم (backup)": "ASSADISSA القرآن الكريم",
    "TAMAZIGHT الأمازيغية (backup)": "TAMAZIGHT الأمازيغية",
    "NESSMA": "NESSMA",
    "HELWA": "HELWA",
    "SAMIRA": "SAMIRA",
    "ECHOROUK NEWS": "ECHOROUK NEWS",
    "ECHOROUK NEWS (backup)": "ECHOROUK NEWS",
    "ECHOROUK TV": "ECHOROUK TV",
    "EL BILAD": "EL BILAD",
    "TV2 ALGERIE [hta_dz-off]": "TV2 ALGERIE",
    "TV1 ENTV [hta_dz-off]": "TV1 ENTV",
    "TV3 ALGERIE [hta_dz-off]": "TV3 ALGERIE",
    "TV4 ALGERIE [hta_dz-off]": "TV4 ALGERIE",
    "TV5 ALGERIE [hta_dz-off]": "TV5 ALGERIE",
    "TV6 ALGERIE [hta_dz-off]": "TV6 ALGERIE",
    "TV7 ELMAARIFA [hta_dz-off]": "TV7 ELMAARIFA",
    "TV8 EDHAKIRA [hta_dz-off]": "TV8 EDHAKIRA",
    "SAMIRA TV [hta_dz-off]": "SAMIRA TV",
    "EL BILAD [hta_dz-off]": "EL BILAD",
    "ENNAHAR TV [hta_dz-off]": "ENNAHAR TV",
    "EL HAYAT TV [hta_dz-off]": "EL HAYAT TV",
    "EL FADRJ TV [hta_dz-off]": "EL FADRJ TV",
    "EL DJAZAIR N1 [hta_dz-off]": "EL DJAZAIR N1",
    "BAHIA TV [hta_dz-off]": "BAHIA TV",
    "AL24 NEWS [hta_dz-off]": "AL24 NEWS",
    "EL HEDDAF TV [hta_dz-off]": "EL HEDDAF TV",
    "ALANIS TV [hta_dz-off]": "ALANIS TV",
    "ECHOROUK TV [hta_dz-off]": "ECHOROUK TV",
    "ECHOROUK NEWS  [hta_dz-off]": "ECHOROUK NEWS",
    "BEUR TV [hta_dz-off]": "BEUR TV",
    "EL DJAZAIRIA TV [downline]": "EL DJAZAIRIA TV",
    "LINA TV [downline]": "LINA TV",
    "SAMIRA TV [downline]": "SAMIRA TV",
    "NESSMA [offlink]": "NESSMA",
    "KAN 11 כאן": "KAN 11 כאן",
    "KAN 11 sub-cc כאן": "KAN 11 sub-cc כאן",
    "RESHET 13 רשת": "RESHET 13 רשת",
    "RESHET 13 sub-cc רשת": "RESHET 13 sub-cc רשת",
    "NOW 14 עכשיו": "NOW 14 עכשיו",
    "i24 NEWS HE עברית": "i24 NEWS HE עברית",
    "HINUCHIT 23 חינוכית": "HINUCHIT 23 חינוכית",
    "MAKO 24 ערוץ": "MAKO 24 ערוץ",
    "HAKNESSET 99 כנסת": "HAKNESSET 99 כנסת",
    "RESHET 13 COMEDY": "RESHET 13 COMEDY",
    "RESHET 13 NOFESH": "RESHET 13 NOFESH",
    "RESHET 13 REALITY": "RESHET 13 REALITY",
    "WALLA !+ וואלה! חדשות": "WALLA !+ וואלה! חדשות",
    "RELEVANT רלוונט": "RELEVANT רלוונט",
    "KAN 26 אפיק": "KAN 26 אפיק",
    "YNET NEWS ידיעות אחרונות": "YNET NEWS ידיעות אחרונות",
    "i24 NEWS EN": "i24 NEWS EN",
    "i24 NEWS AR": "i24 NEWS AR",
    "PANET 30 HALA هلا": "PANET 30 HALA هلا",
    "KAN 33 MAKAN مكان": "KAN 33 MAKAN مكان",
    "ISRAEL 9TV канал": "ISRAEL 9TV канал",
    "SPORT5 STUDIO RADIO LIVE": "SPORT5 STUDIO RADIO LIVE",
    "KABBALAH 96": "KABBALAH 96",
    "HIDABROOT 97": "HIDABROOT 97",
    "MUSAYOF מוסאיוף": "MUSAYOF מוסאיוף",
    "SHELANU GOD-IL": "SHELANU GOD-IL",
    "SHOPPING 21": "SHOPPING 21",
    "KAN 11 כאן (backup)": "KAN 11 כאן",
    "KESHET 12 קשת (backup)": "KESHET 12 קשת",
    "RESHET 13 רשת (backup)": "RESHET 13 רשת",
    "HINUCHIT 23 sub-cc חינוכית (backup rescue)": "HINUCHIT 23 sub-cc חינוכית",
    "MAKO 24 ערוץ (backup)": "MAKO 24 ערוץ",
    "WALLA !+ וואלה! חדשות (backup)": "WALLA !+ וואלה! חדשות",
    "WALLA ! + (backup rescue)": "WALLA ! +",
    "WALLA ! + (backup secure)": "WALLA ! +",
    "RELEVANT רלוונט (backup)": "RELEVANT רלוונט",
    "YNET NEWS (feed)": "YNET NEWS",
    "KAN 11 כאן (backlink)": "KAN 11 כאן",
    "KAN 11 כאן sub-cc (backlink)": "KAN 11 כאן sub-cc",
    "HINUCHIT 23 חינוכית (backlink)": "HINUCHIT 23 חינוכית",
    "KAN 33 MAKAN مكان (backlink)": "KAN 33 MAKAN مكان",
    "RESHET 13 רשת (backlink)": "RESHET 13 רשת",
    "HAKNESSET 99 כנסת (backlink)": "HAKNESSET 99 כנסת",
    "KESHET 12 קשת [find-host]": "KESHET 12 קשת",
    "MAKO 24 ערוץ [find-host]": "MAKO 24 ערוץ",
    "NEWS 12 חדשות [find-host/offline]": "NEWS 12 חדשות",
    "NOW 14 עכשיו [deadlink]": "NOW 14 עכשיו",
    "KESHET 12 קשת [mako-src]": "KESHET 12 קשת",
    "KESHET 12 קשת [frame-issue]": "KESHET 12 קשת",
    "MAKO 24 ערוץ [mako-src]": "MAKO 24 ערוץ",
    "NEWS 12 חדשות [mako-src/offline]": "NEWS 12 חדשות",
    "AL ALARABY 2": "AL ALARABY 2",
    "MTV LBN": "MTV LBN",
    "ONE TV LBN": "ONE TV LBN",
    "VOICE OF LBN": "VOICE OF LBN",
    "LANA TV": "LANA TV",
    "NABAA TV": "NABAA TV",
    "TAHA TV": "TAHA TV",
    "LBC LBN": "LBC LBN",
    "AL AAN TV": "AL AAN TV",
    "ABU DHABI": "ABU DHABI",
    "AL EMARAT": "AL EMARAT",
    "ABU DHABI SPORTS 1": "ABU DHABI SPORTS 1",
    "ABU DHABI SPORTS 2": "ABU DHABI SPORTS 2",
    "YAS TV": "YAS TV",
    "BAYNOUNAH TV": "BAYNOUNAH TV",
    "AL MAMLKA": "AL MAMLKA",
    "SYDAT EL SHASHA": "SYDAT EL SHASHA",
    "FUJAIRAH TV": "FUJAIRAH TV",
    "ROYA TV": "ROYA TV",
    "ALAWLA TV": "ALAWLA TV",
    "SHARJAH TV": "SHARJAH TV",
    "SHARJAH TV 2": "SHARJAH TV 2",
    "SHARJAH TV SPORTS": "SHARJAH TV SPORTS",
    "QATAR TV": "QATAR TV",
    "QATAR TV 2": "QATAR TV 2",
    "SYRIA TV": "SYRIA TV",
    "AL RAYYAN": "AL RAYYAN",
    "AL RAYYAN QADEEM": "AL RAYYAN QADEEM",
    "AL MAYADEEN": "AL MAYADEEN",
    "AL MANAR": "AL MANAR",
    "AL MASIRA": "AL MASIRA",
    "AL KHALIJ TV": "AL KHALIJ TV",
    "PANET 30 HALA": "PANET 30 HALA",
    "KAN 33 MAKAN": "KAN 33 MAKAN",
    "A ONE": "A ONE",
    "KAB 1": "KAB 1",
    "AL WOUSTA": "AL WOUSTA",
    "ATFAL": "ATFAL",
    "AJMAN TV": "AJMAN TV",
    "AMMAN TV": "AMMAN TV",
    "ALRAIMEDIA": "ALRAIMEDIA",
    "MEKAMELEEN": "MEKAMELEEN",
    "IFILM AR": "IFILM AR",
    "YEMEN MAHRIAH": "YEMEN MAHRIAH",
    "AL JAYLIA": "AL JAYLIA",
    "ETIHAD": "ETIHAD",
    "THAQAFEYYAH": "THAQAFEYYAH",
    "AL HAQIQA": "AL HAQIQA",
    "AL MASHHAD": "AL MASHHAD",
    "AL YAUM": "AL YAUM",
    "AL RABIAA": "AL RABIAA",
    "SAMA TV": "SAMA TV",
    "AL DAFRAH": "AL DAFRAH",
    "RAJEEN": "RAJEEN",
    "QUDS TV": "QUDS TV",
    "PAL PBC": "PAL PBC",
    "MUSAWA": "MUSAWA",
    "PAL TV": "PAL TV",
    "PAL SAT": "PAL SAT",
    "FALASTINI TV": "FALASTINI TV",
    "YEMEN TODAY": "YEMEN TODAY",
    "YEMEN SHABAB": "YEMEN SHABAB",
    "UTV IRAQI": "UTV IRAQI",
    "AL RASHEED": "AL RASHEED",
    "AL RAFIDAIN": "AL RAFIDAIN",
    "WATAN EGYPT": "WATAN EGYPT",
    "QAF": "QAF",
    "SSAD TV": "SSAD TV",
    "ISHTAR TV": "ISHTAR TV",
    "LANA TV (backup)": "LANA TV",
    "AL ALARABY 2 (backup)": "AL ALARABY 2",
    "ROYA TV (backup)": "ROYA TV",
    "ROYA TV [geoblocked]": "ROYA TV",
    "LBC LBN [geoblocked]": "LBC LBN",
    "OTV LBN [brokenlink]": "OTV LBN",
    "DUBAI TV": "DUBAI TV",
    "DUBAI ONE": "DUBAI ONE",
    "DUBAI NOOR": "DUBAI NOOR",
    "DUBAI SAMA": "DUBAI SAMA",
    "DUBAI ZAMAN": "DUBAI ZAMAN",
    "DUBAI SPORTS 1": "DUBAI SPORTS 1",
    "DUBAI SPORTS 2": "DUBAI SPORTS 2",
    "DUBAI SPORTS 3": "DUBAI SPORTS 3",
    "DUBAI RACING 1": "DUBAI RACING 1",
    "DUBAI RACING 2": "DUBAI RACING 2",
    "DUBAI RACING 3": "DUBAI RACING 3",
    "KAS QATAR 1": "KAS QATAR 1",
    "KAS QATAR 2": "KAS QATAR 2",
    "KAS QATAR 3": "KAS QATAR 3",
    "KAS QATAR 4": "KAS QATAR 4",
    "KAS QATAR 5": "KAS QATAR 5",
    "KAS QATAR 6": "KAS QATAR 6",
    "SAUDI SBC CH": "SAUDI SBC CH",
    "SAUDIA TV CH 1": "SAUDIA TV CH 1",
    "SAUDIA THIKRAYAT": "SAUDIA THIKRAYAT",
    "SAUDI ACTION WALEED": "SAUDI ACTION WALEED",
    "OMAN 1": "OMAN 1",
    "OMAN MUNASHER": "OMAN MUNASHER",
    "OMAN CULTURE": "OMAN CULTURE",
    "OMAN SPORT": "OMAN SPORT",
    "JORDAN TV": "JORDAN TV",
    "JORDAN TOURISM": "JORDAN TOURISM",
    "JORDAN DRAMA": "JORDAN DRAMA",
    "JORDAN COMEDY": "JORDAN COMEDY",
    "KUWAIT TV 1": "KUWAIT TV 1",
    "KUWAIT TV 2": "KUWAIT TV 2",
    "KUWAIT TV ARAB": "KUWAIT TV ARAB",
    "KUWAIT TV ETHRAA": "KUWAIT TV ETHRAA",
    "KUWAIT TV KHALLIK": "KUWAIT TV KHALLIK",
    "KUWAIT TV PLUS": "KUWAIT TV PLUS",
    "KUWAIT TV SPORTS": "KUWAIT TV SPORTS",
    "KUWAIT TV SPORT PLUS": "KUWAIT TV SPORT PLUS",
    "KUWAIT TV SPORT EXTRA": "KUWAIT TV SPORT EXTRA",
    "SAUDI CH 1": "SAUDI CH 1",
    "SAUDI CH 2": "SAUDI CH 2",
    "SAUDI CH 3": "SAUDI CH 3",
    "SAUDI CH 4": "SAUDI CH 4",
    "SAUDI CH 6 SUNNAH": "SAUDI CH 6 SUNNAH",
    "SAUDI CH 7 KABE": "SAUDI CH 7 KABE",
    "SAUDI CH 9": "SAUDI CH 9",
    "SAUDI CH 10": "SAUDI CH 10",
    "SAUDI CH 17": "SAUDI CH 17",
    "AL JAZEERA": "AL JAZEERA",
    "AL ARABIYA": "AL ARABIYA",
    "AL ALARABY": "AL ALARABY",
    "AL ARABIYA HADATH": "AL ARABIYA HADATH",
    "AL ARABIYA BUSINESS": "AL ARABIYA BUSINESS",
    "AL JAZEERA MUBASHER": "AL JAZEERA MUBASHER",
    "AL JAZEERA MUBASHER 2": "AL JAZEERA MUBASHER 2",
    "AL HURRA": "AL HURRA",
    "AL QAHERA NEWS": "AL QAHERA NEWS",
    "ASHARQ NEWS": "ASHARQ NEWS",
    "ROYA NEWS": "ROYA NEWS",
    "INEWS IQ": "INEWS IQ",
    "BBC NEWS ARABIA": "BBC NEWS ARABIA",
    "SKY NEWS ARABIA": "SKY NEWS ARABIA",
    "CNBC ARABIA": "CNBC ARABIA",
    "DW ARABIC": "DW ARABIC",
    "CGTN ARABIC": "CGTN ARABIC",
    "FRANCE 24 AR": "FRANCE 24 AR",
    "TRT ARABIYA": "TRT ARABIYA",
    "AL ALAM IR [censure-ifany]": "AL ALAM IR",
    "RT ARABIC [censure-blocked]": "RT ARABIC",
    "ASHARQ DOCS": "ASHARQ DOCS",
    "ASHARQ DOCS 2": "ASHARQ DOCS 2",
    "AL HIWAR": "AL HIWAR",
    "AL SHARQIYA": "AL SHARQIYA",
    "PANORAMA FM TV": "PANORAMA FM TV",
    "EL SHARQ": "EL SHARQ",
    "WANASAH": "WANASAH",
    "MAJID": "MAJID",
    "SPACE TOON": "SPACE TOON",
    "SAT7 KIDS": "SAT7 KIDS",
    "AL SHALLAL": "AL SHALLAL",
    "TEN WEYYAK  [geoblocked]": "TEN WEYYAK",
    "IQRAA": "IQRAA",
    "IQRAA EUR": "IQRAA EUR",
    "IQRAA 2": "IQRAA 2",
    "QURAN": "QURAN",
    "BAHRAIN QURAN": "BAHRAIN QURAN",
    "SHARJAH QURAN": "SHARJAH QURAN",
    "SALAM": "SALAM",
    "AL QAMAR": "AL QAMAR",
    "ALMASIRA MUBASHER": "ALMASIRA MUBASHER",
    "AL EKHBARIA": "AL EKHBARIA",
    "AL SUNNAH TV": "AL SUNNAH TV",
    "QURAN KAREEM TV": "QURAN KAREEM TV",
    "AL ISTIQAMA": "AL ISTIQAMA",
    "SAT7 ARABIC": "SAT7 ARABIC",
    "NOURSAT": "NOURSAT",
    "NOURSAT AL SHARQ": "NOURSAT AL SHARQ",
    "NOURSAT AL KODDASS": "NOURSAT AL KODDASS",
    "NOURSAT EL SHABEB": "NOURSAT EL SHABEB",
    "NOURSAT MARIAM": "NOURSAT MARIAM",
    "NOURSAT ENG": "NOURSAT ENG",
    "CTV COPTIC": "CTV COPTIC",
    "ASHARQ NEWS (backup)": "ASHARQ NEWS",
    "ASHARQ NEWS (portrait mode)": "ASHARQ NEWS",
    "AL ARABY (backup)": "AL ARABY",
    "AL ARABY 2 (part-time)": "AL ARABY 2",
    "BBC NEWS ARABIA (backup)": "BBC NEWS ARABIA",
    "MAAN NEWS [issue]": "MAAN NEWS",
    "CARTOON NETWORK AR [down]": "CARTOON NETWORK AR",
    "GULLI ARABI [down]": "GULLI ARABI",
    "MBC 1": "MBC 1",
    "MBC 3": "MBC 3",
    "MBC 4": "MBC 4",
    "MBC 5": "MBC 5",
    "MBC DRAMA": "MBC DRAMA",
    "MBC DRAMA PLUS": "MBC DRAMA PLUS",
    "MBC MASR 1": "MBC MASR 1",
    "MBC MASR 2": "MBC MASR 2",
    "MBC IRAQ": "MBC IRAQ",
    "MBC BOLLYWOOD": "MBC BOLLYWOOD",
    "MBC AFLAM": "MBC AFLAM",
    "MBC MOVIES": "MBC MOVIES",
    "MBC MOVIES ACTION": "MBC MOVIES ACTION",
    "MBC MOVIES THRILLER": "MBC MOVIES THRILLER",
    "MBC FM LIVE TV": "MBC FM LIVE TV",
    "ROTANA CINEMA KSA": "ROTANA CINEMA KSA",
    "ROTANA KHALIJA": "ROTANA KHALIJA",
    "ROTANA CLIP": "ROTANA CLIP",
    "ROTANA COMEDY": "ROTANA COMEDY",
    "CBC LIVE": "CBC LIVE",
    "CBC SOFRA": "CBC SOFRA",
    "CBC NEWS": "CBC NEWS",
    "ROTANA CINEMA MASR": "ROTANA CINEMA MASR",
    "ROTANA PLUS": "ROTANA PLUS",
    "ROTANA KIDS": "ROTANA KIDS",
    "ROTANA CLASSIC": "ROTANA CLASSIC",
    "ROTANA DRAMA": "ROTANA DRAMA",
    "ROTANA DUHK WABASS": "ROTANA DUHK WABASS",
    "SHAHID AL ZAEEM": "SHAHID AL ZAEEM",
    "SHAHID AL MASRAH": "SHAHID AL MASRAH",
    "SHAHID AL USTURA": "SHAHID AL USTURA",
    "SHAHID COMEDY": "SHAHID COMEDY",
    "SHAHID 1": "SHAHID 1",
    "SHAHID SHAM": "SHAHID SHAM",
    "SHAHID MAQALEB": "SHAHID MAQALEB",
    "SHAHID AL ZARAQ": "SHAHID AL ZARAQ",
    "ZEE AFLAM [geoblocked]": "ZEE AFLAM",
    "ZEE ALWAN [geoblocked]": "ZEE ALWAN",
    "WEYYAK DRAMA [geoblocked]": "WEYYAK DRAMA",
    "WEYYAK MIX [geoblocked]": "WEYYAK MIX",
    "WEYYAK ACTION [geoblocked]": "WEYYAK ACTION",
    "WEYYAK NAWAEM [geoblocked]": "WEYYAK NAWAEM",
    "MBC 1 [offlink]": "MBC 1",
    "MBC MASR 1 [offlink]": "MBC MASR 1",
    "RAI NEWS 24 (sometimes)": "RAI NEWS 24",
    "RAI 3": "RAI 3",
    "CLASS CNBC": "CLASS CNBC",
    "LA C NEWS 24": "LA C NEWS 24",
    "TELETICINO": "TELETICINO",
    "LA 7": "LA 7",
    "LA 7D": "LA 7D",
    "ITALIA 2 TV": "ITALIA 2 TV",
    "RETE TV": "RETE TV",
    "RETE 55": "RETE 55",
    "CANALE 7": "CANALE 7",
    "CAFE TV 24": "CAFE TV 24",
    "RADIO 105 TV": "RADIO 105 TV",
    "DEEJAY TV": "DEEJAY TV",
    "RADIO ITALIA TV": "RADIO ITALIA TV",
    "RADIO KISS KISS TV": "RADIO KISS KISS TV",
    "R101 TV": "R101 TV",
    "RTL 102.5": "RTL 102.5",
    "SUPER!": "SUPER!",
    "EXTRA TV": "EXTRA TV",
    "SPORT ITALIA": "SPORT ITALIA",
    "SPORT ITALIA LIVE": "SPORT ITALIA LIVE",
    "RTV S.MARINO": "RTV S.MARINO",
    "GO-TV": "GO-TV",
    "SUPER TENNIS": "SUPER TENNIS",
    "RADIO MONTECARLO TV": "RADIO MONTECARLO TV",
    "VIRGIN RADIO TV": "VIRGIN RADIO TV",
    "ALTO ADIGE TV": "ALTO ADIGE TV",
    "ANRENNA 2 BERGAMO": "ANRENNA 2 BERGAMO",
    "ANTENNA 3 VENETO": "ANTENNA 3 VENETO",
    "ANTENNA SUD": "ANTENNA SUD",
    "ANTENNA SUD EXTRA": "ANTENNA SUD EXTRA",
    "ARISTANIS TV": "ARISTANIS TV",
    "ARTE NETWORK": "ARTE NETWORK",
    "AURORA ARTE": "AURORA ARTE",
    "AZZURRA TV": "AZZURRA TV",
    "EURONEWS IT": "EURONEWS IT",
    "TAGESSCHAU 24": "TAGESSCHAU 24",
    "DAS ERSTE INTL": "DAS ERSTE INTL",
    "DAS ERSTE DE": "DAS ERSTE DE",
    "RTL DE": "RTL DE",
    "ALPHA ARD": "ALPHA ARD",
    "BR DE": "BR DE",
    "HR DE": "HR DE",
    "SR DE": "SR DE",
    "WDR DE": "WDR DE",
    "ARTE DE": "ARTE DE",
    "EURONEWS DE": "EURONEWS DE",
    "RT DEUTSCH [censure-blocked]": "RT DEUTSCH",
    "RTL LUX": "RTL LUX",
    "RTL HR": "RTL HR",
    "HRT 1": "HRT 1",
    "HRT 2": "HRT 2",
    "HRT 3": "HRT 3",
    "RTS 1": "RTS 1",
    "RTS 2": "RTS 2",
    "PINK": "PINK",
    "TVR INT": "TVR INT",
    "ANTENA 1 RO": "ANTENA 1 RO",
    "ANTENA 3 VOX": "ANTENA 3 VOX",
    "KANAL D RO": "KANAL D RO",
    "KANAL D2 RO": "KANAL D2 RO",
    "MOLDOVA 1": "MOLDOVA 1",
    "MOLDOVA 2": "MOLDOVA 2",
    "GPB 1TV პირველი არხი": "GPB 1TV პირველი არხი",
    "GPB 2TV": "GPB 2TV",
    "IMEDI": "IMEDI",
    "RUSTAVI 2": "RUSTAVI 2",
    "PALITRA": "PALITRA",
    "FORMULA": "FORMULA",
    "ADJARA": "ADJARA",
    "MTAVARI ARKHI": "MTAVARI ARKHI",
    "H1 ARM Հանրային հեռուստաը": "H1 ARM Հանրային հեռուստաը",
    "H1 NEWS": "H1 NEWS",
    "SONG ARM": "SONG ARM",
    "AZ TV Azərbaycan Televiziyası": "AZ TV Azərbaycan Televiziyası",
    "AZ NEWS": "AZ NEWS",
    "AZ STAR": "AZ STAR",
    "ATV AZ": "ATV AZ",
    "BAKU TV": "BAKU TV",
    "UMİT TV": "UMİT TV",
    "MEDENİYYET": "MEDENİYYET",
    "IRIB 1": "IRIB 1",
    "IRIB 2": "IRIB 2",
    "IRIB 3": "IRIB 3",
    "IRIB 4": "IRIB 4",
    "IRIB 5": "IRIB 5",
    "IRIB AMOOZESH": "IRIB AMOOZESH",
    "IRIB MOSTANAD": "IRIB MOSTANAD",
    "IRIB NAMAYESH": "IRIB NAMAYESH",
    "IRIB NASIM": "IRIB NASIM",
    "IRIB POOYA": "IRIB POOYA",
    "IRIB SALAMAT": "IRIB SALAMAT",
    "IRIB TAMASHA": "IRIB TAMASHA",
    "IRIB VARZESH": "IRIB VARZESH",
    "IRIB MESRAFSANJAN": "IRIB MESRAFSANJAN",
    "IRIB ESHAREH": "IRIB ESHAREH",
    "IRIB IRINN": "IRIB IRINN",
    "IRIB AIOSPORT": "IRIB AIOSPORT",
    "IRIB AIOSPORT 2": "IRIB AIOSPORT 2",
    "IRIB IFILM FAR 1": "IRIB IFILM FAR 1",
    "IRIB IFILM FAR 2": "IRIB IFILM FAR 2",
    "MBC PERSIA": "MBC PERSIA",
    "HASTI TV": "HASTI TV",
    "ASIL TV": "ASIL TV",
    "SNN TV": "SNN TV",
    "NEJAT TV": "NEJAT TV",
    "VOX 1": "VOX 1",
    "YOUR TIME": "YOUR TIME",
    "HOD HOD": "HOD HOD",
    "24/7 BOX": "24/7 BOX",
    "OX IR": "OX IR",
    "AVA FAMILY": "AVA FAMILY",
    "PARS": "PARS",
    "SL ONE": "SL ONE",
    "SL TWO": "SL TWO",
    "P FILM": "P FILM",
    "ITN": "ITN",
    "META FILM": "META FILM",
    "AVA SERIES": "AVA SERIES",
    "BRAVOO": "BRAVOO",
    "FX TV": "FX TV",
    "OI TN": "OI TN",
    "TAPESH": "TAPESH",
    "TAPESH IR": "TAPESH IR",
    "MIHAN TV": "MIHAN TV",
    "NEGAH TV": "NEGAH TV",
    "AL WILAYAH": "AL WILAYAH",
    "PAYVAND": "PAYVAND",
    "PJ TV": "PJ TV",
    "ASSIRAT": "ASSIRAT",
    "PERSIANA NOSTALGIA": "PERSIANA NOSTALGIA",
    "PERSIANA MUSIC": "PERSIANA MUSIC",
    "PERSIANA TURKIYE": "PERSIANA TURKIYE",
    "PERSIANA COMEDY": "PERSIANA COMEDY",
    "PERSIANA IRANIAN": "PERSIANA IRANIAN",
    "PERSIANA ONE": "PERSIANA ONE",
    "PERSIANA TWO": "PERSIANA TWO",
    "PERSIANA KOREA": "PERSIANA KOREA",
    "PERSIANA CINEMA": "PERSIANA CINEMA",
    "PERSIANA HD": "PERSIANA HD",
    "PERSIANA LATINO": "PERSIANA LATINO",
    "PERSIANA FAMILY": "PERSIANA FAMILY",
    "PERSIANA SCIENCE": "PERSIANA SCIENCE",
    "PERSIANA JUNIOR": "PERSIANA JUNIOR",
    "IRIB 1 (backup)": "IRIB 1",
    "IRIB 2 (backup)": "IRIB 2",
    "IRIB 3 (backup)": "IRIB 3",
    "IRIB 4 (backup)": "IRIB 4",
    "IRIB 5 (backup)": "IRIB 5",
    "IRIB IRINN (backup)": "IRIB IRINN",
}


STATIC_CATEGORIES = {
    "TV5MONDE FBSM": "🇫🇷法兰西",
    "TF1": "🇫🇷法兰西",
    "FRANCE 2": "🇫🇷法兰西",
    "FRANCE 3": "🇫🇷法兰西",
    "FRANCE 4": "🇫🇷法兰西",
    "FRANCE 5": "🇫🇷法兰西",
    "FRANCE TV SÉRIES": "🇫🇷法兰西",
    "FRANCE TV DOCUMENTAIRES": "🇫🇷法兰西",
    "ARTE": "🇫🇷法兰西",
    "NRJ 12": "🇫🇷法兰西",
    "CHÉRIE 25": "🇫🇷法兰西",
    "CANAL+ EN CLAIR": "🇫🇷法兰西",
    "RMC STORY": "🇫🇷法兰西",
    "RMC DÉCOUVERTE": "🇫🇷法兰西",
    "C8": "🇫🇷法兰西",
    "CSTAR": "🇫🇷法兰西",
    "BFM TV": "🇫🇷法兰西",
    "CNEWS": "🇫🇷法兰西",
    "LCI": "🇫🇷法兰西",
    "FRANCE INFO:": "🇫🇷法兰西",
    "LE MÉDIA TV": "🇫🇷法兰西",
    "EURONEWS FR": "🇫🇷法兰西",
    "TV5MONDE INFO": "🇫🇷法兰西",
    "FRANCE 24 FR": "🇫🇷法兰西",
    "LCP-AN": "🇫🇷法兰西",
    "PUBLIC-SÉNAT": "🇫🇷法兰西",
    "BFM 2": "🇫🇷法兰西",
    "BFM GRAND REPORTAGES": "🇫🇷法兰西",
    "RMC TALK INFO": "🇫🇷法兰西",
    "20 MINUTES TV IDF": "🇫🇷法兰西",
    "LE FIGARO IDF": "🇫🇷法兰西",
    "LE FIGARO LIVE": "🇫🇷法兰西",
    "i24 NEWS FR": "🇮🇱以色列",
    "CGTN FRANÇAIS": "🇫🇷法兰西",
    "LN24 BE": "🇫🇷法兰西",
    "MONACO INFO": "🇫🇷法兰西",
    "RDI CANADA": "🇫🇷法兰西",
    "AFRICA 24 FR": "🇫🇷法兰西",
    "AFRICANEWS FR": "🇫🇷法兰西",
    "BFM BUSINESS": "🇫🇷法兰西",
    "B SMART": "🇫🇷法兰西",
    "BLOOMBERG FR": "🇫🇷法兰西",
    "TV FINANCE": "🇫🇷法兰西",
    "PRESS IR FRENCH [temp barker]": "🇫🇷法兰西",
    "RT FRANÇAIS [censure-blocked]": "🇫🇷法兰西",
    "BFM TV (backup)": "🇫🇷法兰西",
    "BFM 2 (backup)": "🇫🇷法兰西",
    "BFM BUSINESS (backup)": "🇫🇷法兰西",
    "LE MÉDIA TV (backup ok)": "🇫🇷法兰西",
    "LE MÉDIA TV (backup ko)": "🇫🇷法兰西",
    "EURONEWS FR (backup)": "🇫🇷法兰西",
    "FRANCE INFO: (backup)": "🇫🇷法兰西",
    "FRANCE INFO: (backup-off)": "🇫🇷法兰西",
    "FRANCE INFO: [find-host]": "🇫🇷法兰西",
    "FRANCE 24 FR (backup)": "🇫🇷法兰西",
    "FRANCE 24 FR (backup-off)": "🇫🇷法兰西",
    "LCI (backup)": "🇫🇷法兰西",
    "CNEWS (backup)": "🇫🇷法兰西",
    "LE MÉDIA TV (backup)": "🇫🇷法兰西",
    "LCP-AN (backup)": "🇫🇷法兰西",
    "LE FIGARO IDF (backup)": "🇫🇷法兰西",
    "CGTN FRANÇAIS (backup)": "🇫🇷法兰西",
    "RDI CANADA (backup)": "🇫🇷法兰西",
    "AFRICANEWS FR (backup)": "🇫🇷法兰西",
    "LCI [tkn-blocked]": "🇫🇷法兰西",
    "TV5MONDE EUROPE [geo-area]": "🇫🇷法兰西",
    "TV5MONDE MOYEN-ORIENT [geo-area]": "🇫🇷法兰西",
    "TV5MONDE ASIE SUD-EST [geo-area]": "🇫🇷法兰西",
    "TV5MONDE PACIFIQUE [geo-area]": "🇫🇷法兰西",
    "CANAL+ EN CLAIR (backup)": "🇫🇷法兰西",
    "C8 [tokenized]": "🇫🇷法兰西",
    "C8 [drm-keycrypted]": "🇫🇷法兰西",
    "CSTAR [drm-keycrypted]": "🇫🇷法兰西",
    "CSTAR [tokenized]": "🇫🇷法兰西",
    "RMC DÉCOUVERTE [drm-keycrypted]": "🇫🇷法兰西",
    "RMC STORY [drm-keycrypted]": "🇫🇷法兰西",
    "M6 [drm-keycrypted]": "🇫🇷法兰西",
    "W9 [drm-keycrypted]": "🇫🇷法兰西",
    "6TER [drm-keycrypted]": "🇫🇷法兰西",
    "M6 (backup)": "🇫🇷法兰西",
    "C8 (backup)": "🇫🇷法兰西",
    "TF1 (backup)": "🇫🇷法兰西",
    "ARTE (backup)": "🇫🇷法兰西",
    "FRANCE 2 (backup)": "🇫🇷法兰西",
    "FRANCE 3 (backup)": "🇫🇷法兰西",
    "FRANCE 4 (backup)": "🇫🇷法兰西",
    "FRANCE 5 (backup)": "🇫🇷法兰西",
    "M6 (check)": "🇫🇷法兰西",
    "TMC (check)": "🇫🇷法兰西",
    "W9 (check)": "🇫🇷法兰西",
    "FUN RADIO TV BE": "🇫🇷法兰西",
    "FUN RADIO TV FR": "🇫🇷法兰西",
    "GÉNÉRATIONS TV": "🇫🇷法兰西",
    "MÉLODY": "🇫🇷法兰西",
    "CLUBBING TV": "🇫🇷法兰西",
    "TRACE URBAN": "🇫🇷法兰西",
    "TRACE SPORTS": "🇫🇷法兰西",
    "SPORT EN FRANCE": "🇫🇷法兰西",
    "L'ÉQUIPE LIVE 1": "🇫🇷法兰西",
    "L'ÉQUIPE LIVE 2": "🇫🇷法兰西",
    "L'ÉQUIPE LIVE FOOT": "🇫🇷法兰西",
    "L'ÉQUIPE TV": "🇫🇷法兰西",
    "RMC TALK SPORT": "🇫🇷法兰西",
    "JOURNAL DU GOLF": "🇫🇷法兰西",
    "L'ÉSPRIT SORCIER TV": "🇫🇷法兰西",
    "SQOOL TV": "🇫🇷法兰西",
    "GULLI": "🇫🇷法兰西",
    "GONG": "🇫🇷法兰西",
    "SUPERTOONS FR": "🇫🇷法兰西",
    "PLUTO KIDS": "🇫🇷法兰西",
    "VEVO POP": "🇫🇷法兰西",
    "VEVO HP RB": "🇫🇷法兰西",
    "VEVO 90 00": "🇫🇷法兰西",
    "MGG E-SPORT": "🇫🇷法兰西",
    "MOTORVISION FR": "🇫🇷法兰西",
    "MOTORVISION TV": "🇫🇷法兰西",
    "MOTORVISION TV-2": "🇫🇷法兰西",
    "TECH&CO": "🇫🇷法兰西",
    "MEN'S UP TV": "🇫🇷法兰西",
    "TOP SANTÉ": "🇫🇷法兰西",
    "MAISON & TRAVAUX": "🇫🇷法兰西",
    "TRAVEL XP": "🇫🇷法兰西",
    "TV5MONDE VOYAGE": "🇫🇷法兰西",
    "NATURE TIME": "🇫🇷法兰西",
    "VOYAGES ET SAVEURS": "🇫🇷法兰西",
    "PLUTO CUISINE": "🇫🇷法兰西",
    "RMC WOW": "🇫🇷法兰西",
    "RMC MYSTÈRE": "🇫🇷法兰西",
    "RMC MECANIC": "🇫🇷法兰西",
    "RMC ALERTE SECOURS": "🇫🇷法兰西",
    "ALLO CINÉ": "🇫🇷法兰西",
    "RAKUTEN TOP FILMS TV": "🇫🇷法兰西",
    "WILD SIDE TV": "🇫🇷法兰西",
    "TELE NOVELA TV": "🇫🇷法兰西",
    "BBLACK! AFRICA": "🇫🇷法兰西",
    "BBLACK! CARIBBEAN": "🇫🇷法兰西",
    "BBLACK! CLASSIK": "🇫🇷法兰西",
    "UNIVERS CINÉ": "🇫🇷法兰西",
    "PLUTO CINÉ": "🇫🇷法兰西",
    "PLUTO POLAR": "🇫🇷法兰西",
    "CINÉ NANAR": "🇫🇷法兰西",
    "CINÉ WESTERN": "🇫🇷法兰西",
    "KTO": "🇫🇷法兰西",
    "DIEU TV": "🇫🇷法兰西",
    "EMCI TV": "🇫🇷法兰西",
    "MUSEUM": "🇫🇷法兰西",
    "MY ZEN": "🇫🇷法兰西",
    "MY ZEN WELLBEING": "🇫🇷法兰西",
    "FASHION TV": "🇫🇷法兰西",
    "TV5MONDE STYLE [geo-area]": "🇫🇷法兰西",
    "TV5MONDE TiVi [geo-area]": "🇫🇷法兰西",
    "GULLI (backup)": "🇫🇷法兰西",
    "FUN RADIO TV BE [died-link]": "🇫🇷法兰西",
    "FUN RADIO TV BE (backup)": "🇫🇷法兰西",
    "BFM ALPES": "🇫🇷法兰西",
    "BFM ALSACE": "🇫🇷法兰西",
    "BFM H.PROVENCE": "🇫🇷法兰西",
    "BFM LILLE": "🇫🇷法兰西",
    "BFM LITTORAL": "🇫🇷法兰西",
    "BFM LYON": "🇫🇷法兰西",
    "BFM MARSEILLE": "🇫🇷法兰西",
    "BFM NICE": "🇫🇷法兰西",
    "BFM NORMANDIE": "🇫🇷法兰西",
    "BFM PARIS": "🇫🇷法兰西",
    "BFM TOULON": "🇫🇷法兰西",
    "F3 PARIS IDF": "🇫🇷法兰西",
    "F3 PROVENCE ALPES": "🇫🇷法兰西",
    "F3 CÔTE D'AZUR": "🇫🇷法兰西",
    "F3 RHÔNE ALPES": "🇫🇷法兰西",
    "F3 ALPES": "🇫🇷法兰西",
    "F3 AUVERGNE": "🇫🇷法兰西",
    "F3 BOURGOGNE": "🇫🇷法兰西",
    "F3 FRANCHE COMPTÉ": "🇫🇷法兰西",
    "F3 CENTRE": "🇫🇷法兰西",
    "F3 CORSE VÍA STELLA": "🇫🇷法兰西",
    "F3 ALSACE": "🇫🇷法兰西",
    "F3 CHAMPAGNE": "🇫🇷法兰西",
    "F3 LORRAINE": "🇫🇷法兰西",
    "F3 NORD PDC": "🇫🇷法兰西",
    "F3 PICARDIE": "🇫🇷法兰西",
    "F3 B.NORMANDIE": "🇫🇷法兰西",
    "F3 H.NORMANDIE": "🇫🇷法兰西",
    "F3 AQUITAINE": "🇫🇷法兰西",
    "F3 NOA": "🇫🇷法兰西",
    "F3 LIMOUSIN": "🇫🇷法兰西",
    "F3 POITOU CHARENTES": "🇫🇷法兰西",
    "F3 MIDI PYRÉNÉES": "🇫🇷法兰西",
    "F3 LANGUEDOC": "🇫🇷法兰西",
    "F3 PAYS LOIRE": "🇫🇷法兰西",
    "F3 BRETAGNE": "🇫🇷法兰西",
    "TÉBÉO TV": "🇫🇷法兰西",
    "TVR RENNES": "🇫🇷法兰西",
    "TÉLÉ NANTES": "🇫🇷法兰西",
    "TV VENDÉE": "🇫🇷法兰西",
    "TV 78": "🇫🇷法兰西",
    "7A LIMOGES": "🇫🇷法兰西",
    "ALPE D'HUEZ TV": "🇫🇷法兰西",
    "BIP TV": "🇫🇷法兰西",
    "CANAL 32": "🇫🇷法兰西",
    "IL TV": "🇫🇷法兰西",
    "MOSELLE TV": "🇫🇷法兰西",
    "TV7 BORDEAUX": "🇫🇷法兰西",
    "TV7 COLMAR": "🇫🇷法兰西",
    "TV 3V": "🇫🇷法兰西",
    "VIA MATÉLÉ": "🇫🇷法兰西",
    "VIA OCCITANIE": "🇫🇷法兰西",
    "VIA TELEPAESE": "🇫🇷法兰西",
    "VOSGES TV": "🇫🇷法兰西",
    "WÉO NORD": "🇫🇷法兰西",
    "WÉO PICARDIE": "🇫🇷法兰西",
    "NANCY WEB TV": "🇫🇷法兰西",
    "MAURIENNE TV": "🇫🇷法兰西",
    "LA CHAÎNE 32": "🇫🇷法兰西",
    "TÉLÉ GOHELLE": "🇫🇷法兰西",
    "TVPI BAYONNE": "🇫🇷法兰西",
    "PUISSANCE TÉLÉVISION": "🇫🇷法兰西",
    "NA TV": "🇫🇷法兰西",
    "KANAL DUDE": "🇫🇷法兰西",
    "CANNES LÉRINS TV": "🇫🇷法兰西",
    "LITTORAL TV": "🇫🇷法兰西",
    "TV TARN": "🇫🇷法兰西",
    "MOSAIK CRISTAL TV": "🇫🇷法兰西",
    "TV8 MONTBLANC": "🇫🇷法兰西",
    "TVT TOURS": "🇫🇷法兰西",
    "ANGERS TÉLÉ": "🇫🇷法兰西",
    "LYON CAPITALE TV": "🇫🇷法兰西",
    "TL CHOLETAIS": "🇫🇷法兰西",
    "BRIONNAIS TV": "🇫🇷法兰西",
    "VALLOIRE TV": "🇫🇷法兰西",
    "N31": "🇫🇷法兰西",
    "TÉLÉ GRENOBLE": "🇫🇷法兰西",
    "LM TV SARTHE": "🇫🇷法兰西",
    "ASTV": "🇫🇷法兰西",
    "UBIZNEWS OM5TV": "🇫🇷法兰西",
    "MADRAS FM TV": "🇫🇷法兰西",
    "ANTENNE RÉUNION": "🇫🇷法兰西",
    "LA BRISE HAÏTI": "🇫🇷法兰西",
    "TNTV": "🇫🇷法兰西",
    "ETV GUADELOUPE": "🇫🇷法兰西",
    "LA 1ÈRE MARTINIQUE [geo-area]": "🇫🇷法兰西",
    "LA 1ÈRE GUADELOUPE [geo-area]": "🇫🇷法兰西",
    "LA 1ÈRE GUYANE [geo-area]": "🇫🇷法兰西",
    "LA 1ÈRE MAYOTTE [geo-area]": "🇫🇷法兰西",
    "LA 1ÈRE RÉUNION [geo-area]": "🇫🇷法兰西",
    "LA 1ÈRE N.CALÉDONIE [geo-area]": "🇫🇷法兰西",
    "LA 1ÈRE POLYNÉSIE [geo-area]": "🇫🇷法兰西",
    "LA 1ÈRE WALLIS FUTUNA [geo-area]": "🇫🇷法兰西",
    "LA 1ÈRE SAINT-PIERRE MIQUELON [geo-area]": "🇫🇷法兰西",
    "LA 1ÈRE MARTINIQUE (news only)": "🇫🇷法兰西",
    "LA 1ÈRE GUADELOUPE (news only)": "🇫🇷法兰西",
    "LA 1ÈRE GUYANE (news only)": "🇫🇷法兰西",
    "LA 1ÈRE MAYOTTE (news only)": "🇫🇷法兰西",
    "LA 1ÈRE RÉUNION (news only)": "🇫🇷法兰西",
    "LA 1ÈRE N.CALÉDONIE (news only)": "🇫🇷法兰西",
    "LA 1ÈRE POLYNÉSIE (news only)": "🇫🇷法兰西",
    "LA 1ÈRE WALLIS FUTUNA (news only)": "🇫🇷法兰西",
    "LA 1ÈRE SAINT-PIERRE MIQUELON (news only)": "🇫🇷法兰西",
    "TV MONACO": "🇫🇷法兰西",
    "BEL RTL": "🇫🇷法兰西",
    "LA TÉLÉ": "🇫🇷法兰西",
    "NO TÉLÉ": "🇫🇷法兰西",
    "TÉLÉ BRUXELLES": "🇫🇷法兰西",
    "VEDIA": "🇫🇷法兰西",
    "RTC TÉLÉ LIÈGE": "🇫🇷法兰西",
    "TÉLÉ MB": "🇫🇷法兰西",
    "BOUKÈ": "🇫🇷法兰西",
    "ANTENNE CENTRE": "🇫🇷法兰西",
    "CANAL ZOOM": "🇫🇷法兰西",
    "TV LUX": "🇫🇷法兰西",
    "NOOVO": "🇫🇷法兰西",
    "LÉMAN BLEU": "🇫🇷法兰西",
    "CARAC 1": "🇫🇷法兰西",
    "CARAC 2": "🇫🇷法兰西",
    "CARAC 3": "🇫🇷法兰西",
    "CARAC 4": "🇫🇷法兰西",
    "TVM 3": "🇫🇷法兰西",
    "CANAL 9": "🇫🇷法兰西",
    "CANAL ALPHA": "🇫🇷法兰西",
    "M LE MÉDIA": "🇫🇷法兰西",
    "SAVOIR.MÉDIA": "🇫🇷法兰西",
    "TÉLÉ QUÉBEC": "🇫🇷法兰西",
    "CPAC TV": "🇫🇷法兰西",
    "ICI MONTRÉAL": "🇫🇷法兰西",
    "TRT HABER": "🇹🇷土耳其",
    "HABER TÜRK": "🇹🇷土耳其",
    "HABER GLOBAL": "🇹🇷土耳其",
    "TV 100": "🇹🇷土耳其",
    "EKOL TV": "🇹🇷土耳其",
    "NTV": "🇹🇷土耳其",
    "CNN TÜRK": "🇹🇷土耳其",
    "BLOOMBERG HT": "🇹🇷土耳其",
    "EKO TÜRK": "🇹🇷土耳其",
    "A PARA": "🇹🇷土耳其",
    "BUSINESS CHANNEL TÜRK": "🇹🇷土耳其",
    "CNBC-e (weekday-time)": "🇹🇷土耳其",
    "TBMM TV": "🇹🇷土耳其",
    "DHA (feed 1)": "🇹🇷土耳其",
    "DHA (feed 2)": "🇹🇷土耳其",
    "AA (feed)": "🇹🇷土耳其",
    "TRT HABER (backup)": "🇹🇷土耳其",
    "HABER TÜRK (backup)": "🇹🇷土耳其",
    "HABER GLOBAL (backup)": "🇹🇷土耳其",
    "HABER GLOBAL (off-action)": "🇹🇷土耳其",
    "TV 100 (backup)": "🇹🇷土耳其",
    "CNN TÜRK (tokened)": "🇹🇷土耳其",
    "CNN TÜRK (backup)": "🇹🇷土耳其",
    "NTV (backup)": "🇹🇷土耳其",
    "NTV (downline)": "🇹🇷土耳其",
    "EKOL TV (backup)": "🇹🇷土耳其",
    "BLOOMBERG HT (backup)": "🇹🇷土耳其",
    "CNBC-e (weekday-time) [backup]": "🇹🇷土耳其",
    "FLASH HABER": "🇹🇷土耳其",
    "SÖZCÜ TV": "🇹🇷土耳其",
    "KRT": "🇹🇷土耳其",
    "TELE 1": "🇹🇷土耳其",
    "HALK TV": "🇹🇷土耳其",
    "ULUSAL KANAL": "🇹🇷土耳其",
    "TV 5": "🇹🇷土耳其",
    "BENGÜ TÜRK": "🇹🇷土耳其",
    "TGRT HABER": "🇹🇷土耳其",
    "TV NET": "🇹🇷土耳其",
    "24": "🇹🇷土耳其",
    "A HABER": "🇹🇷土耳其",
    "ÜLKE": "🇹🇷土耳其",
    "AKIT TV": "🇹🇷土耳其",
    "ARTI TV": "🇹🇷土耳其",
    "YOL TV": "🇹🇷土耳其",
    "SÖZCÜ TV (backup)": "🇹🇷土耳其",
    "KRT (backup)": "🇹🇷土耳其",
    "HALK TV (backup)": "🇹🇷土耳其",
    "ULUSAL KANAL (backup)": "🇹🇷土耳其",
    "BENGÜ TÜRK (backup)": "🇹🇷土耳其",
    "TV NET (backup)": "🇹🇷土耳其",
    "TGRT HABER (backup)": "🇹🇷土耳其",
    "24 (backup)": "🇹🇷土耳其",
    "TV 5 (backup yt_ch)": "🇹🇷土耳其",
    "TV 5 (backup yt_vd)": "🇹🇷土耳其",
    "TRT 1": "🇹🇷土耳其",
    "KANAL D": "🇹🇷土耳其",
    "STAR": "🇬🇷希腊",
    "SHOW": "🇹🇷土耳其",
    "TV8": "🇹🇷土耳其",
    "ATV": "🇹🇷土耳其",
    "KANAL 7": "🇹🇷土耳其",
    "BEYAZ TV": "🇹🇷土耳其",
    "TRT 1 (backup)": "🇹🇷土耳其",
    "KANAL D (backup)": "🇹🇷土耳其",
    "STAR (backup)": "🇹🇷土耳其",
    "SHOW [downline]": "🇹🇷土耳其",
    "NOW (backup)": "🇹🇷土耳其",
    "ATV (backup)": "🇹🇷土耳其",
    "ATV [youtube-src]": "🇹🇷土耳其",
    "ATV [tkn-blocked]": "🇹🇷土耳其",
    "TV8 (backup)": "🇹🇷土耳其",
    "KANAL 7 (backup)": "🇹🇷土耳其",
    "BEYAZ TV (backup)": "🇹🇷土耳其",
    "TEVE 2 (backup)": "🇹🇷土耳其",
    "TRT BELGESEL": "🇹🇷土耳其",
    "TRT 2": "🇹🇷土耳其",
    "DMAX": "🇹🇷土耳其",
    "TLC TR": "🇹🇷土耳其",
    "360": "🇹🇷土耳其",
    "TV 4": "🇹🇷土耳其",
    "TİVİ 6": "🇹🇷土耳其",
    "CİNE 1": "🇹🇷土耳其",
    "CINE5 TV": "🇹🇷土耳其",
    "TÜRKİYE KLİNİKLERİ TV": "🇹🇷土耳其",
    "CGTN BELGESEL": "🇹🇷土耳其",
    "SAĞLIK CHANNEL": "🇹🇷土耳其",
    "WOMAN KADIN TV": "🇹🇷土耳其",
    "WOMAN LIFE TV": "🇹🇷土耳其",
    "MOR TV": "🇹🇷土耳其",
    "TEVE 2": "🇹🇷土耳其",
    "SHOW MAX": "🇹🇷土耳其",
    "A2": "🇹🇷土耳其",
    "FİL TV": "🇹🇷土耳其",
    "SHOW MAX (backup)": "🇹🇷土耳其",
    "SHOW MAX [tkn-blocked]": "🇹🇷土耳其",
    "A2 (backup)": "🇹🇷土耳其",
    "A2 [tkn-blocked]": "🇹🇷土耳其",
    "TRT BELGESEL (backup)": "🇹🇷土耳其",
    "DMAX (backup)": "🇹🇷土耳其",
    "DMAX [downline]": "🇹🇷土耳其",
    "TLC TR [downline]": "🇹🇷土耳其",
    "TLC TR (backup)": "🇹🇷土耳其",
    "360 [tkn-blocked]": "🇹🇷土耳其",
    "360 (backup)": "🇹🇷土耳其",
    "WOMAN KADIN TV (backup)": "🇹🇷土耳其",
    "TRT ÇOCUK": "🇹🇷土耳其",
    "TRT DİYANET ÇOCUK": "🇹🇷土耳其",
    "DİYANET ÇOCUK TV": "🇹🇷土耳其",
    "CARTOON NETWORK TR": "🇹🇷土耳其",
    "GALATASARAY TV": "🇹🇷土耳其",
    "FENERBAHÇE TV": "🇹🇷土耳其",
    "HT SPOR": "🇹🇷土耳其",
    "BIS HABER": "🇹🇷土耳其",
    "A SPOR": "🇹🇷土耳其",
    "SPORTS TV": "🇹🇷土耳其",
    "TRT SPOR [geo-blocked]": "🇹🇷土耳其",
    "TRT SPOR2 YILDIZ [geo-blocked]": "🇹🇷土耳其",
    "TABİİ SPOR 1 [geoblocked]": "🇹🇷土耳其",
    "TABİİ SPOR 2 [geoblocked]": "🇹🇷土耳其",
    "TABİİ SPOR 3 [geoblocked]": "🇹🇷土耳其",
    "TABİİ SPOR 4 [geoblocked]": "🇹🇷土耳其",
    "TABİİ SPOR 5 [geoblocked]": "🇹🇷土耳其",
    "TABİİ SPOR 6 [geoblocked]": "🇹🇷土耳其",
    "TJK TV [geo-blocked]": "🇹🇷土耳其",
    "TJK TV": "🇹🇷土耳其",
    "BY HORSES TV": "🇹🇷土耳其",
    "TAY TV": "🇹🇷土耳其",
    "TV8 BUÇUK": "🇹🇷土耳其",
    "TRT EBA TV": "🇹🇷土耳其",
    "MİNİKA ÇOCUK": "🇹🇷土耳其",
    "MİNİKA GO": "🇹🇷土耳其",
    "HT SPOR (backup)": "🇹🇷土耳其",
    "BIS HABER (backup)": "🇹🇷土耳其",
    "TRT SPOR (backup)": "🇹🇷土耳其",
    "TRT SPOR2 YILDIZ (backup)": "🇹🇷土耳其",
    "TRT3 SPOR [offline]": "🇹🇷土耳其",
    "TRT ÇOCUK (backup)": "🇹🇷土耳其",
    "SPORTS TV (backup)": "🇹🇷土耳其",
    "TV8 BUÇUK (backup)": "🇹🇷土耳其",
    "TV8 BUÇUK [tkn-blocked]": "🇹🇷土耳其",
    "A SPOR (backup)": "🇹🇷土耳其",
    "A SPOR [tkn-blocked]": "🇹🇷土耳其",
    "TRT MÜZİK": "🇹🇷土耳其",
    "SPOTIFY TURKEY • TRLIST 👤": "🇹🇷土耳其",
    "SPOTIFY TURKEY • 2024 🎧": "🇹🇷土耳其",
    "KRAL - KRAL POP": "🇹🇷土耳其",
    "DREAM TÜRK": "🇹🇷土耳其",
    "POWER TÜRK": "🇹🇷土耳其",
    "POWER TÜRK TAPTAZE": "🇹🇷土耳其",
    "POWER TÜRK SLOW": "🇹🇷土耳其",
    "POWER TÜRK AKUSTİK": "🇹🇷土耳其",
    "TATLISES": "🇹🇷土耳其",
    "MİLYON TV": "🇹🇷土耳其",
    "NUMBER ONE TÜRK": "🇹🇷土耳其",
    "NUMBER ONE TÜRK ASK": "🇹🇷土耳其",
    "NUMBER ONE TÜRK DAMAR": "🇹🇷土耳其",
    "NUMBER ONE TÜRK DANCE": "🇹🇷土耳其",
    "NUMBER ONE": "🇹🇷土耳其",
    "FASHION ONE": "🇹🇷土耳其",
    "POWER TV": "🇹🇷土耳其",
    "POWER DANCE": "🇹🇷土耳其",
    "POWER LOVE": "🇹🇷土耳其",
    "NUMBER ONE (backup)": "🇹🇷土耳其",
    "KRAL - KRAL POP (backup)": "🇹🇷土耳其",
    "DİNÎ, DİĞER",TRT AVAZ": "🇹🇷土耳其",
    "TRT TÜRK": "🇹🇷土耳其",
    "KANAL 7 AVRUPA": "🇹🇷土耳其",
    "SHOW TÜRK": "🇹🇷土耳其",
    "EURO D": "🇹🇷土耳其",
    "EURO D (geçici geçerli)": "🇹🇷土耳其",
    "EURO STAR": "🇹🇷土耳其",
    "EURO STAR (geçici geçerli)": "🇹🇷土耳其",
    "ATV AVRUPA (geçici geçerli)": "🇹🇷土耳其",
    "TV8 INT (geçici geçerli)": "🇹🇷土耳其",
    "TGRT EU": "🇹🇷土耳其",
    "AGRO TV": "🇹🇷土耳其",
    "ÇİFTÇİ TV": "🇹🇷土耳其",
    "TARIM TV": "🇹🇷土耳其",
    "MELTEM": "🇹🇷土耳其",
    "KANAL B": "🇹🇷土耳其",
    "EM TV": "🇹🇷土耳其",
    "DİYANET TV": "🇹🇷土耳其",
    "SEMERKAND": "🇹🇷土耳其",
    "SEMERKAND WAY": "🇹🇷土耳其",
    "DOST TV": "🇹🇷土耳其",
    "REHBER TV": "🇹🇷土耳其",
    "LALEGÜL TV": "🇹🇷土耳其",
    "BERAT TV": "🇹🇷土耳其",
    "CAN TV": "🇹🇷土耳其",
    "ON4 TV": "🇹🇷土耳其",
    "AFRO TURK TV": "🇹🇷土耳其",
    "LUYS TV": "🇹🇷土耳其",
    "SAT 7 TÜRK": "🇹🇷土耳其",
    "KANAL HAYAT": "🇹🇷土耳其",
    "ABN TURKEY": "🇹🇷土耳其",
    "TGRT BELGESEL": "🇹🇷土耳其",
    "TGRT EU (backup)": "🇹🇷土耳其",
    "TGRT BELGESEL (backup)": "🇹🇷土耳其",
    "TGRT BELGESEL (checkalt)": "🇹🇷土耳其",
    "KANAL 7 AVRUPA [off-link]": "🇹🇷土耳其",
    "KANAL 7 AVRUPA (backup)": "🇹🇷土耳其",
    "SHOW TÜRK (geçici geçerli)": "🇹🇷土耳其",
    "ANADOLU NET TV": "🇹🇷土耳其",
    "AKSU TV KAHRAMANMARAŞ": "🇹🇷土耳其",
    "ALANYA POSTA TV": "🇹🇷土耳其",
    "ALANYA TV": "🇹🇷土耳其",
    "ALTAS TV ORDU": "🇹🇷土耳其",
    "ART AMASYA": "🇹🇷土耳其",
    "AS TV BURSA": "🇹🇷土耳其",
    "BARTIN TV": "🇹🇷土耳其",
    "BEYKENT TV": "🇹🇷土耳其",
    "BİR TV İZMİR": "🇹🇷土耳其",
    "BRTV KARABÜK": "🇹🇷土耳其",
    "BURSA LINE TV": "🇹🇷土耳其",
    "BURSA ON6 TV": "🇹🇷土耳其",
    "BÜLTEN TV ANKARA": "🇹🇷土耳其",
    "ÇAY TV RİZE": "🇹🇷土耳其",
    "ÇEKMEKÖY BELEDİYE TV": "🇹🇷土耳其",
    "ÇORUM BLD TV": "🇹🇷土耳其",
    "DEHA TV DENİZLİ": "🇹🇷土耳其",
    "DENİZ POSTASI TV": "🇹🇷土耳其",
    "DİM TV ALANYA": "🇹🇷土耳其",
    "DİYAR TV": "🇹🇷土耳其",
    "DRT DENİZLİ": "🇹🇷土耳其",
    "DÜĞÜN TV ÇİNE": "🇹🇷土耳其",
    "EDESSA TV ŞANLIURFA": "🇹🇷土耳其",
    "EGE TV İZMİR": "🇹🇷土耳其",
    "EGE LIVE TV": "🇹🇷土耳其",
    "ELMAS TV ZONGULDAK": "🇹🇷土耳其",
    "ER TV MALATYA": "🇹🇷土耳其",
    "ERCİS TV": "🇹🇷土耳其",
    "ERCİYES TV": "🇹🇷土耳其",
    "ERT ŞAH TV ERZİNCAN": "🇹🇷土耳其",
    "ERZURUM WEB TV": "🇹🇷土耳其",
    "ES TV ESKİŞEHİR": "🇹🇷土耳其",
    "EDİRNE TV": "🇹🇷土耳其",
    "EFES DOST TV": "🇹🇷土耳其",
    "ESENLER ŞEHİR TV": "🇹🇷土耳其",
    "ETV KAYSERİ": "🇹🇷土耳其",
    "FRT FETHİYE": "🇹🇷土耳其",
    "GRT GAZİANTEP TV": "🇹🇷土耳其",
    "GÜNEY TV TARSUS": "🇹🇷土耳其",
    "GÜNEYDOĞU TV": "🇹🇷土耳其",
    "GURBET 24 TV": "🇹🇷土耳其",
    "HEDEF TV KOCAELİ": "🇹🇷土耳其",
    "HABER61 TRABZON": "🇹🇷土耳其",
    "HRT HATAY AKDENİZ": "🇹🇷土耳其",
    "HUNAT TV KAYSERİ": "🇹🇷土耳其",
    "İÇEL TV MERSİN": "🇹🇷土耳其",
    "İZMİR TIME 35 TV": "🇹🇷土耳其",
    "İZMİR TÜRK TV": "🇹🇷土耳其",
    "LİDER HABER TV": "🇹🇷土耳其",
    "KANAL 15 BURDUR": "🇹🇷土耳其",
    "KANAL 19 ÇORUM": "🇹🇷土耳其",
    "KANAL 23 ELAZIĞ": "🇹🇷土耳其",
    "KANAL 26 ESKİŞEHİR": "🇹🇷土耳其",
    "KANAL 3 AFYONKARAHİSAR": "🇹🇷土耳其",
    "KANAL 32 ISPARTA": "🇹🇷土耳其",
    "KANAL 33 MERSİN": "🇹🇷土耳其",
    "KANAL 34 İSTANBUL": "🇹🇷土耳其",
    "KANAL 53 RİZE": "🇹🇷土耳其",
    "KANAL 56 SİİRT": "🇹🇷土耳其",
    "KANAL 58 SİVAS": "🇹🇷土耳其",
    "KANAL 68 AKSARAY": "🇹🇷土耳其",
    "KANAL EGE": "🇹🇷土耳其",
    "KANAL FIRAT": "🇹🇷土耳其",
    "KANAL S SAMSUN": "🇹🇷土耳其",
    "KANAL URFA": "🇹🇷土耳其",
    "KANAL V ANTALYA": "🇹🇷土耳其",
    "KANAL Z ZONGULDAK": "🇹🇷土耳其",
    "KASTAMONU TV": "🇹🇷土耳其",
    "KARABÜK DERİN TV": "🇹🇷土耳其",
    "KARDELEN TV": "🇹🇷土耳其",
    "KAY TV KAYSERİ": "🇹🇷土耳其",
    "KEÇİÖREN TV ANKARA": "🇹🇷土耳其",
    "KENT 38 TV KAYSERİ": "🇹🇷土耳其",
    "KENT TV BODRUM": "🇹🇷土耳其",
    "KOCAELİ TV": "🇹🇷土耳其",
    "KONYA KTV": "🇹🇷土耳其",
    "KONYA OLAY TV": "🇹🇷土耳其",
    "KOZA TV ADANA": "🇹🇷土耳其",
    "KIBRIS BRT 1": "🇹🇷土耳其",
    "KIBRIS BRT 2": "🇹🇷土耳其",
    "KIBRIS BRT 3": "🇹🇷土耳其",
    "KIBRIS ADA TV": "🇹🇷土耳其",
    "KIBRIS KANAL T": "🇹🇷土耳其",
    "KIBRIS GENÇ TV": "🇹🇷土耳其",
    "KIBRIS TV": "🇹🇷土耳其",
    "KIBRIS SİM TV": "🇹🇷土耳其",
    "KIBRIS TV2020": "🇹🇷土耳其",
    "KIBRIS KK TV": "🇹🇷土耳其",
    "LIFE TV KAYSERİ": "🇹🇷土耳其",
    "MALATYA VUSLAT TV": "🇹🇷土耳其",
    "MANISA ETV": "🇹🇷土耳其",
    "MARMARİS TV": "🇹🇷土耳其",
    "MAVİ KARADENİZ TV": "🇹🇷土耳其",
    "MERCAN TV ADIYAMAN": "🇹🇷土耳其",
    "METROPOL DENİZLİ": "🇹🇷土耳其",
    "MUĞLA MERKEZ TV": "🇹🇷土耳其",
    "MUĞLA TÜRK TV": "🇹🇷土耳其",
    "NOKTA TV KOCAELİ": "🇹🇷土耳其",
    "NORA TV AKSARAY": "🇹🇷土耳其",
    "OGUN TV": "🇹🇷土耳其",
    "OLAY TÜRK KAYSERİ TV": "🇹🇷土耳其",
    "OLAY TV BURSA": "🇹🇷土耳其",
    "ORDU BEL TV": "🇹🇷土耳其",
    "ORT OSMANİYE TV": "🇹🇷土耳其",
    "PAMUKKALE TV": "🇹🇷土耳其",
    "POSTA TV ALANYA": "🇹🇷土耳其",
    "RADYO KARDEŞ TV FR": "🇹🇷土耳其",
    "RİZE TÜRK TV": "🇹🇷土耳其",
    "SARIYER TV İST": "🇹🇷土耳其",
    "SILKWAY KAZAKH (TUR)": "🇹🇷土耳其",
    "SİNOP YILDIZ TV": "🇹🇷土耳其",
    "SKYHABER TV": "🇹🇷土耳其",
    "SLOW KARADENİZ TV": "🇹🇷土耳其",
    "SUN RTV MERSİN": "🇹🇷土耳其",
    "RUMELİ TV": "🇹🇷土耳其",
    "TEK RUMELİ TV": "🇹🇷土耳其",
    "TEMPO TV": "🇹🇷土耳其",
    "TV 1 ADANA": "🇹🇷土耳其",
    "TİVİ TURK": "🇹🇷土耳其",
    "TON TV ÇANAKKALE": "🇹🇷土耳其",
    "TOKAT TV": "🇹🇷土耳其",
    "TRABZON TV": "🇹🇷土耳其",
    "TRAKYA TÜRK": "🇹🇷土耳其",
    "TURHAL WEB TV": "🇹🇷土耳其",
    "TV KAYSERİ": "🇹🇷土耳其",
    "TV 1 KAYSERİ": "🇹🇷土耳其",
    "TV 25 DOĞU": "🇹🇷土耳其",
    "TV 264 SAKARYA": "🇹🇷土耳其",
    "TV 35 İZMİR": "🇹🇷土耳其",
    "TV 41 KOCAELİ": "🇹🇷土耳其",
    "TV 48 MİLAS": "🇹🇷土耳其",
    "TV 52 ORDU": "🇹🇷土耳其",
    "TVO ANTALYA": "🇹🇷土耳其",
    "TV DEN AYDIN": "🇹🇷土耳其",
    "TÜRKMENELİ TV": "🇹🇷土耳其",
    "UR FANATİK TV": "🇹🇷土耳其",
    "ÜSKÜDAR UNİVERSİTE TV": "🇹🇷土耳其",
    "VAN GÖLÜ TV": "🇹🇷土耳其",
    "VİYANA TV": "🇹🇷土耳其",
    "YAŞAM TV": "🇹🇷土耳其",
    "WORLD TÜRK TV": "🇹🇷土耳其",
    "YOZGAT BLD TV": "🇹🇷土耳其",
    "ZAROK KURMANÎ": "🇹🇷土耳其",
    "ZAROK SORANÎ": "🇹🇷土耳其",
    "TRT KURDÎ": "🇹🇷土耳其",
    "ZAGROS TV": "🇹🇷土耳其",
    "KURDMAX SHOW": "🇹🇷土耳其",
    "KURDMAX SORANÎ": "🇹🇷土耳其",
    "RÛDAW TV": "🇹🇷土耳其",
    "KURD CHANNEL": "🇹🇷土耳其",
    "KURDISTAN 24": "🇹🇷土耳其",
    "KURDISTAN TV": "🇹🇷土耳其",
    "KURDSAT": "🇹🇷土耳其",
    "KURDSAT NEWS": "🇹🇷土耳其",
    "KURDMAX MUSIC": "🇹🇷土耳其",
    "GELÎ KURDISTAN TV": "🇹🇷土耳其",
    "KOMALA TV": "🇹🇷土耳其",
    "JÎN TV": "🇹🇷土耳其",
    "CÎHAN TV": "🇹🇷土耳其",
    "ERT WORLD": "🇬🇷希腊",
    "ERT NEWS": "🇬🇷希腊",
    "ERT 1 [geoblocked]": "🇬🇷希腊",
    "ERT 2 [geoblocked]": "🇬🇷希腊",
    "ERT 3 [geoblocked]": "🇬🇷希腊",
    "ERT KIDS [geoblocked]": "🇬🇷希腊",
    "ERT MUSIC [geoblocked]": "🇬🇷希腊",
    "ERT SPORTS [geoblocked]": "🇬🇷希腊",
    "ALPHA TV": "🇬🇷希腊",
    "ANT 1": "🇬🇷希腊",
    "SKAI": "🇬🇷希腊",
    "MEGA": "🇬🇷希腊",
    "MAK TV": "🇬🇷希腊",
    "NETMAX TV": "🇬🇷希腊",
    "OPEN TV": "🇬🇷希腊",
    "ATTICA": "🇬🇷希腊",
    "SIGMA TV": "🇬🇷希腊",
    "MAGIC TV": "🇬🇷希腊",
    "MAKEDONIA TV": "🇬🇷希腊",
    "NET TV TORONTO": "🇬🇷希腊",
    "NET TV EUROPE": "🇬🇷希腊",
    "NET MAX TV": "🇬🇷希腊",
    "ANT 1 DRAMA": "🇬🇷希腊",
    "MAD WORLD": "🇬🇷希腊",
    "RIK SAT CYPRUS": "🇬🇷希腊",
    "ACTION 24": "🇬🇷希腊",
    "GROOVY TV": "🇬🇷希腊",
    "NEA CRETE TV": "🇬🇷希腊",
    "BARAZA RELAXING TV": "🇬🇷希腊",
    "XALASTRA TV": "🇬🇷希腊",
    "NRG TV": "🇬🇷希腊",
    "BOYAH TV": "🇬🇷希腊",
    "AEOLOS": "🇬🇷希腊",
    "EXPLORE": "🇬🇷希腊",
    "TOP CHANNEL": "🇬🇷希腊",
    "ράκη Νετ TV": "🇬🇷希腊",
    "TELE ΚΡΗΤΗ": "🇬🇷希腊",
    "START TV": "🇬🇷希腊",
    "PELLA TV": "🇬🇷希腊",
    "KONTRA TV": "🇬🇷希腊",
    "HIGH TV": "🇬🇷希腊",
    "HELLENIC TV": "🇬🇷希腊",
    "GREEK TV LONDON": "🇬🇷希腊",
    "GRD CHANNEL": "🇬🇷希腊",
    "CRETA": "🇬🇷希腊",
    "CORFU": "🇬🇷希腊",
    "BLUE SKY": "🇬🇷希腊",
    "ERT NEWS 2": "🇬🇷希腊",
    "ERT NEWS 3": "🇬🇷希腊",
    "ERT WORLD (backup)": "🇬🇷希腊",
    "ERT NEWS (backup)": "🇬🇷希腊",
    "RIK SAT CYPRUS [geoblocked]": "🇬🇷希腊",
    "EURONEWS PT": "🇵🇹葡萄牙",
    "CNN PORTUGAL": "🇵🇹葡萄牙",
    "SIC NOTÍCIAS": "🇵🇹葡萄牙",
    "SIC": "🇵🇹葡萄牙",
    "TVI": "🇵🇹葡萄牙",
    "TVI INT": "🇵🇹葡萄牙",
    "TVI V+": "🇵🇹葡萄牙",
    "TVI REALITY": "🇵🇹葡萄牙",
    "SIC NOVELAS": "🇵🇹葡萄牙",
    "SIC REPLAY": "🇵🇹葡萄牙",
    "SIC HD ALTA DEFINIÇÃO": "🇵🇹葡萄牙",
    "PORTO CANAL": "🇵🇹葡萄牙",
    "TVI AFRICA": "🇵🇹葡萄牙",
    "AR PARLAMENTO": "🇵🇹葡萄牙",
    "ADB TV": "🇵🇹葡萄牙",
    "MCA": "🇵🇹葡萄牙",
    "FAMA FM TV": "🇵🇹葡萄牙",
    "KURIAKOS CINE": "🇵🇹葡萄牙",
    "KURIAKOS KIDS": "🇵🇹葡萄牙",
    "TRACE BRAZUCA": "🇵🇹葡萄牙",
    "RTP 1 (backup sd)": "🇵🇹葡萄牙",
    "RTP 2 (backup sd)": "🇵🇹葡萄牙",
    "RTP 3 (backup sd)": "🇵🇹葡萄牙",
    "RTP 3 (tvhlsdvr)": "🇵🇹葡萄牙",
    "RTP 3 (tvhlsdvr_HD)": "🇵🇹葡萄牙",
    "RTP ACORES (backup)": "🇵🇹葡萄牙",
    "EURONEWS PT (backup)": "🇵🇹葡萄牙",
    "CNN PORTUGAL (backup)": "🇵🇹葡萄牙",
    "SIC NOTÍCIAS (backup)": "🇵🇹葡萄牙",
    "SIC NOVELAS (backup)": "🇵🇹葡萄牙",
    "TVI V+ (ex-TVI FICCAO)": "🇵🇹葡萄牙",
    "CNN PORTUGAL [find-host]": "🇵🇹葡萄牙",
    "TVI [find-host]": "🇵🇹葡萄牙",
    "TVI INT [find-host]": "🇵🇹葡萄牙",
    "CNN PORTUGAL [tkn-blocked]": "🇵🇹葡萄牙",
    "TVI [tkn-blocked]": "🇵🇹葡萄牙",
    "TVI INT [tkn-blocked]": "🇵🇹葡萄牙",
    "TVI FICCAO [tkn-blocked]": "🇵🇹葡萄牙",
    "TVI REALITY [tkn-blocked]": "🇵🇹葡萄牙",
    "SIC NOVELAS [offline]": "🇵🇹葡萄牙",
    "TVE INTERNACIONAL": "🇪🇸西班牙",
    "TVE LA 1": "🇪🇸西班牙",
    "TVE LA 2": "🇪🇸西班牙",
    "TVE 24 H": "🇪🇸西班牙",
    "STAR TVE": "🇪🇸西班牙",
    "TVE TDP": "🇪🇸西班牙",
    "TVE CLAN": "🇪🇸西班牙",
    "ANTENNA 3": "🇪🇸西班牙",
    "CUATRO": "🇪🇸西班牙",
    "TELECINCO": "🇪🇸西班牙",
    "LA SEXTA": "🇪🇸西班牙",
    "TVE SOMOS CINE [geo-limited]": "🇪🇸西班牙",
    "RTVE PLAY CADENA 1": "🇪🇸西班牙",
    "RTVE PLAY CADENA 2": "🇪🇸西班牙",
    "RTVE PLAY CADENA 3": "🇪🇸西班牙",
    "RTVE PLAY CADENA 4": "🇪🇸西班牙",
    "RTVE": "🇪🇸西班牙",
    "EURONEWS ES": "🇪🇸西班牙",
    "EL PAIS": "🇪🇸西班牙",
    "EL CONFIDENCIAL TV": "🇪🇸西班牙",
    "CANAL PARLAMENTO": "🇪🇸西班牙",
    "CANAL DIPUTADOS": "🇪🇸西班牙",
    "SOL MÙSICA": "🇪🇸西班牙",
    "TRECE": "🇪🇸西班牙",
    "TRECE INT": "🇪🇸西班牙",
    "ATRES SERIES": "🇪🇸西班牙",
    "ATRES CLÁSICOS": "🇪🇸西班牙",
    "ATRES COMEDIA": "🇪🇸西班牙",
    "ATRES FLOOXER": "🇪🇸西班牙",
    "ATRES MULTICINE": "🇪🇸西班牙",
    "ATRES KIDZ": "🇪🇸西班牙",
    "PEQUE TV": "🇪🇸西班牙",
    "CARTOON NETWORK ES": "🇪🇸西班牙",
    "VIVE KANAL D DRAMA": "🇪🇸西班牙",
    "TRACE LATINA": "🇪🇸西班牙",
    "REAL MADRID CINEVERSE": "🇪🇸西班牙",
    "REAL MADRID TV": "🇪🇸西班牙",
    "EL TORO TV": "🇪🇸西班牙",
    "SUR 1 ANDALUCÍA": "🇪🇸西班牙",
    "SUR 2 ANDALUCÍA": "🇪🇸西班牙",
    "SUR NOTICIAS ANDALUCÍA": "🇪🇸西班牙",
    "CINE ANDALUCÍA": "🇪🇸西班牙",
    "COCINA ANDALUCÍA": "🇪🇸西班牙",
    "TURISMO ANDALUCÍA": "🇪🇸西班牙",
    "ARAGÓN TV": "🇪🇸西班牙",
    "ARAGÓN NOTICIAS": "🇪🇸西班牙",
    "LA 1 CANARIAS": "🇪🇸西班牙",
    "LA 2 CANARIAS": "🇪🇸西班牙",
    "24 H CANARIAS": "🇪🇸西班牙",
    "CASTILLA MEDIA": "🇪🇸西班牙",
    "LA 1 CATALUNYA": "🇪🇸西班牙",
    "LA 2 CATALUNYA": "🇪🇸西班牙",
    "24 H CATALUNYA": "🇪🇸西班牙",
    "TV3 CATALUNYA INT": "🇪🇸西班牙",
    "TV3 CATALUNYA 24H": "🇪🇸西班牙",
    "TV3 CATALUNYA FAST 1": "🇪🇸西班牙",
    "TV3 CATALUNYA FAST 2": "🇪🇸西班牙",
    "TV3 CATALUNYA LOC": "🇪🇸西班牙",
    "TV3 CATALUNYA C33": "🇪🇸西班牙",
    "CATALUNYA BON DIA TV": "🇪🇸西班牙",
    "INFOCIUDADES TV CATALUNYA": "🇪🇸西班牙",
    "CATALUNYA 8": "🇪🇸西班牙",
    "TENERIFE 4": "🇪🇸西班牙",
    "CEUTA RTV": "🇪🇸西班牙",
    "TELE MADRID": "🇪🇸西班牙",
    "TELE MADRID INT": "🇪🇸西班牙",
    "TELE MADRID OTRA": "🇪🇸西班牙",
    "CANAL EXTRAMADURA": "🇪🇸西班牙",
    "TVG GALICIA EU": "🇪🇸西班牙",
    "TVG GALICIA AM": "🇪🇸西班牙",
    "TVG GALICIA MO": "🇪🇸西班牙",
    "TVG CULTURAL": "🇪🇸西班牙",
    "TVG INFANTIL": "🇪🇸西班牙",
    "TVG 2": "🇪🇸西班牙",
    "EITB 1": "🇪🇸西班牙",
    "EITB 2": "🇪🇸西班牙",
    "EITB INT": "🇪🇸西班牙",
    "EITB DEPORTE": "🇪🇸西班牙",
    "ANDORRA DIFUSIÓ": "🇪🇸西班牙",
    "TV CANARIA": "🇪🇸西班牙",
    "TV RIOJA": "🇪🇸西班牙",
    "RIOJA COCINA": "🇪🇸西班牙",
    "101TV SEVILLA": "🇪🇸西班牙",
    "TELESUR": "🇪🇸西班牙",
    "FRANCE 24 ES": "🇪🇸西班牙",
    "DW ESPAÑOL": "🇪🇸西班牙",
    "NHK WORLD ESP": "🇪🇸西班牙",
    "CGTN ESPAÑOL": "🇪🇸西班牙",
    "PRESS HISPAN TV": "🇪🇸西班牙",
    "CNN EN ESPAÑOL [geoblocked]": "🇪🇸西班牙",
    "RT ESPAÑOL [censure-blocked]": "🇪🇸西班牙",
    "EURONEWS ES (backup)": "🇪🇸西班牙",
    "TVE LA 1 (backup)": "🇪🇸西班牙",
    "TVE LA 2 (backup)": "🇪🇸西班牙",
    "TVE 24 H (backup)": "🇪🇸西班牙",
    "TVE INTERNACIONAL (backup)": "🇪🇸西班牙",
    "TVE INTERNACIONAL (america)": "🇪🇸西班牙",
    "TVE SOMOS CINE (backup)": "🇪🇸西班牙",
    "STAR TVE (espana)": "🇪🇸西班牙",
    "TVE CLAN [geo-restricted]": "🇪🇸西班牙",
    "TENERIFE 4 (offlink)": "🇪🇸西班牙",
    "TELE MADRID (offlink)": "🇪🇸西班牙",
    "2M MONDE الثانية": "摩洛哥-阿尔及利亚-突尼斯",
    "M24 TV للأنباء": "摩洛哥-阿尔及利亚-突尼斯",
    "TELE MAROC قناة المغرب": "摩洛哥-阿尔及利亚-突尼斯",
    "MEDI 1 MG العربية": "摩洛哥-阿尔及利亚-突尼斯",
    "MEDI 1 AR العربية": "摩洛哥-阿尔及利亚-突尼斯",
    "MEDI 1 FR العربية": "摩洛哥-阿尔及利亚-突尼斯",
    "CHADA TV شدى": "摩洛哥-阿尔及利亚-突尼斯",
    "WATANIA 1": "摩洛哥-阿尔及利亚-突尼斯",
    "WATANIA 2": "摩洛哥-阿尔及利亚-突尼斯",
    "ATTASIA 9": "摩洛哥-阿尔及利亚-突尼斯",
    "TV2 ALGÉRIE": "摩洛哥-阿尔及利亚-突尼斯",
    "CNA": "摩洛哥-阿尔及利亚-突尼斯",
    "WATANIA 1 (backup)": "摩洛哥-阿尔及利亚-突尼斯",
    "WATANIA 2 (backup)": "摩洛哥-阿尔及利亚-突尼斯",
    "CHADA TV شدى (backup)": "摩洛哥-阿尔及利亚-突尼斯",
    "MEDI 1 MG العربية (backup)": "摩洛哥-阿尔及利亚-突尼斯",
    "MEDI 1 AR العربية (backup)": "摩洛哥-阿尔及利亚-突尼斯",
    "MEDI 1 FR العربية (backup)": "摩洛哥-阿尔及利亚-突尼斯",
    "MEDI 1 MG العربية (off-backup)": "摩洛哥-阿尔及利亚-突尼斯",
    "AL AOULA LAÂYOUNE الأولى (backup)": "摩洛哥-阿尔及利亚-突尼斯",
    "Al AOULA INT الأولى (backup)": "摩洛哥-阿尔及利亚-突尼斯",
    "2M MONDE الثانية (backup)": "摩洛哥-阿尔及利亚-突尼斯",
    "ARRYADIA الرياضية (backup)": "摩洛哥-阿尔及利亚-突尼斯",
    "ATHAQAFIA الثقافية (backup)": "摩洛哥-阿尔及利亚-突尼斯",
    "AL MAGHRIBIA المغربية الإخبارية (backup)": "摩洛哥-阿尔及利亚-突尼斯",
    "ASSADISSA القرآن الكريم (backup)": "摩洛哥-阿尔及利亚-突尼斯",
    "TAMAZIGHT الأمازيغية (backup)": "摩洛哥-阿尔及利亚-突尼斯",
    "NESSMA": "摩洛哥-阿尔及利亚-突尼斯",
    "HELWA": "摩洛哥-阿尔及利亚-突尼斯",
    "SAMIRA": "摩洛哥-阿尔及利亚-突尼斯",
    "ECHOROUK NEWS": "摩洛哥-阿尔及利亚-突尼斯",
    "ECHOROUK NEWS (backup)": "摩洛哥-阿尔及利亚-突尼斯",
    "ECHOROUK TV": "摩洛哥-阿尔及利亚-突尼斯",
    "EL BILAD": "摩洛哥-阿尔及利亚-突尼斯",
    "TV2 ALGERIE [hta_dz-off]": "摩洛哥-阿尔及利亚-突尼斯",
    "TV1 ENTV [hta_dz-off]": "摩洛哥-阿尔及利亚-突尼斯",
    "TV3 ALGERIE [hta_dz-off]": "摩洛哥-阿尔及利亚-突尼斯",
    "TV4 ALGERIE [hta_dz-off]": "摩洛哥-阿尔及利亚-突尼斯",
    "TV5 ALGERIE [hta_dz-off]": "摩洛哥-阿尔及利亚-突尼斯",
    "TV6 ALGERIE [hta_dz-off]": "摩洛哥-阿尔及利亚-突尼斯",
    "TV7 ELMAARIFA [hta_dz-off]": "摩洛哥-阿尔及利亚-突尼斯",
    "TV8 EDHAKIRA [hta_dz-off]": "摩洛哥-阿尔及利亚-突尼斯",
    "SAMIRA TV [hta_dz-off]": "摩洛哥-阿尔及利亚-突尼斯",
    "EL BILAD [hta_dz-off]": "摩洛哥-阿尔及利亚-突尼斯",
    "ENNAHAR TV [hta_dz-off]": "摩洛哥-阿尔及利亚-突尼斯",
    "EL HAYAT TV [hta_dz-off]": "摩洛哥-阿尔及利亚-突尼斯",
    "EL FADRJ TV [hta_dz-off]": "摩洛哥-阿尔及利亚-突尼斯",
    "EL DJAZAIR N1 [hta_dz-off]": "摩洛哥-阿尔及利亚-突尼斯",
    "BAHIA TV [hta_dz-off]": "摩洛哥-阿尔及利亚-突尼斯",
    "AL24 NEWS [hta_dz-off]": "摩洛哥-阿尔及利亚-突尼斯",
    "EL HEDDAF TV [hta_dz-off]": "摩洛哥-阿尔及利亚-突尼斯",
    "ALANIS TV [hta_dz-off]": "摩洛哥-阿尔及利亚-突尼斯",
    "ECHOROUK TV [hta_dz-off]": "摩洛哥-阿尔及利亚-突尼斯",
    "ECHOROUK NEWS  [hta_dz-off]": "摩洛哥-阿尔及利亚-突尼斯",
    "BEUR TV [hta_dz-off]": "摩洛哥-阿尔及利亚-突尼斯",
    "EL DJAZAIRIA TV [downline]": "摩洛哥-阿尔及利亚-突尼斯",
    "LINA TV [downline]": "摩洛哥-阿尔及利亚-突尼斯",
    "SAMIRA TV [downline]": "摩洛哥-阿尔及利亚-突尼斯",
    "NESSMA [offlink]": "摩洛哥-阿尔及利亚-突尼斯",
    "KAN 11 כאן": "🇮🇱以色列",
    "KAN 11 sub-cc כאן": "🇮🇱以色列",
    "RESHET 13 רשת": "🇮🇱以色列",
    "RESHET 13 sub-cc רשת": "🇮🇱以色列",
    "NOW 14 עכשיו": "🇮🇱以色列",
    "i24 NEWS HE עברית": "🇮🇱以色列",
    "HINUCHIT 23 חינוכית": "🇮🇱以色列",
    "MAKO 24 ערוץ": "🇮🇱以色列",
    "HAKNESSET 99 כנסת": "🇮🇱以色列",
    "RESHET 13 COMEDY": "🇮🇱以色列",
    "RESHET 13 NOFESH": "🇮🇱以色列",
    "RESHET 13 REALITY": "🇮🇱以色列",
    "WALLA !+ וואלה! חדשות": "🇮🇱以色列",
    "RELEVANT רלוונט": "🇮🇱以色列",
    "KAN 26 אפיק": "🇮🇱以色列",
    "YNET NEWS ידיעות אחרונות": "🇮🇱以色列",
    "i24 NEWS EN": "🇮🇱以色列",
    "i24 NEWS AR": "🇦🇷阿根廷",
    "PANET 30 HALA هلا": "🇮🇱以色列",
    "KAN 33 MAKAN مكان": "🇮🇱以色列",
    "ISRAEL 9TV канал": "🇮🇱以色列",
    "SPORT5 STUDIO RADIO LIVE": "🇮🇱以色列",
    "KABBALAH 96": "🇮🇱以色列",
    "HIDABROOT 97": "🇮🇱以色列",
    "MUSAYOF מוסאיוף": "🇮🇱以色列",
    "SHELANU GOD-IL": "🇮🇱以色列",
    "SHOPPING 21": "🇮🇱以色列",
    "KAN 11 כאן (backup)": "🇮🇱以色列",
    "KESHET 12 קשת (backup)": "🇮🇱以色列",
    "RESHET 13 רשת (backup)": "🇮🇱以色列",
    "HINUCHIT 23 sub-cc חינוכית (backup rescue)": "🇮🇱以色列",
    "MAKO 24 ערוץ (backup)": "🇮🇱以色列",
    "WALLA !+ וואלה! חדשות (backup)": "🇮🇱以色列",
    "WALLA ! + (backup rescue)": "🇮🇱以色列",
    "WALLA ! + (backup secure)": "🇮🇱以色列",
    "RELEVANT רלוונט (backup)": "🇮🇱以色列",
    "YNET NEWS (feed)": "🇮🇱以色列",
    "KAN 11 כאן (backlink)": "🇮🇱以色列",
    "KAN 11 כאן sub-cc (backlink)": "🇮🇱以色列",
    "HINUCHIT 23 חינוכית (backlink)": "🇮🇱以色列",
    "KAN 33 MAKAN مكان (backlink)": "🇮🇱以色列",
    "RESHET 13 רשת (backlink)": "🇮🇱以色列",
    "HAKNESSET 99 כנסת (backlink)": "🇮🇱以色列",
    "KESHET 12 קשת [find-host]": "🇮🇱以色列",
    "MAKO 24 ערוץ [find-host]": "🇮🇱以色列",
    "NEWS 12 חדשות [find-host/offline]": "🇮🇱以色列",
    "NOW 14 עכשיו [deadlink]": "🇮🇱以色列",
    "KESHET 12 קשת [mako-src]": "🇮🇱以色列",
    "KESHET 12 קשת [frame-issue]": "🇮🇱以色列",
    "MAKO 24 ערוץ [mako-src]": "🇮🇱以色列",
    "NEWS 12 חדשות [mako-src/offline]": "🇮🇱以色列",
    "AL ALARABY 2": "🇦🇷阿根廷",
    "MTV LBN": "🇦🇷阿根廷",
    "ONE TV LBN": "🇦🇷阿根廷",
    "VOICE OF LBN": "🇦🇷阿根廷",
    "LANA TV": "🇦🇷阿根廷",
    "NABAA TV": "🇦🇷阿根廷",
    "TAHA TV": "🇦🇷阿根廷",
    "LBC LBN": "🇦🇷阿根廷",
    "AL AAN TV": "🇦🇷阿根廷",
    "ABU DHABI": "🇦🇷阿根廷",
    "AL EMARAT": "🇦🇷阿根廷",
    "ABU DHABI SPORTS 1": "🇦🇷阿根廷",
    "ABU DHABI SPORTS 2": "🇦🇷阿根廷",
    "YAS TV": "🇦🇷阿根廷",
    "BAYNOUNAH TV": "🇦🇷阿根廷",
    "AL MAMLKA": "🇦🇷阿根廷",
    "SYDAT EL SHASHA": "🇦🇷阿根廷",
    "FUJAIRAH TV": "🇦🇷阿根廷",
    "ROYA TV": "🇦🇷阿根廷",
    "ALAWLA TV": "🇦🇷阿根廷",
    "SHARJAH TV": "🇦🇷阿根廷",
    "SHARJAH TV 2": "🇦🇷阿根廷",
    "SHARJAH TV SPORTS": "🇦🇷阿根廷",
    "QATAR TV": "🇦🇷阿根廷",
    "QATAR TV 2": "🇦🇷阿根廷",
    "SYRIA TV": "🇦🇷阿根廷",
    "AL RAYYAN": "🇦🇷阿根廷",
    "AL RAYYAN QADEEM": "🇦🇷阿根廷",
    "AL MAYADEEN": "🇦🇷阿根廷",
    "AL MANAR": "🇦🇷阿根廷",
    "AL MASIRA": "🇦🇷阿根廷",
    "AL KHALIJ TV": "🇦🇷阿根廷",
    "PANET 30 HALA": "🇦🇷阿根廷",
    "KAN 33 MAKAN": "🇦🇷阿根廷",
    "A ONE": "🇦🇷阿根廷",
    "KAB 1": "🇦🇷阿根廷",
    "AL WOUSTA": "🇦🇷阿根廷",
    "ATFAL": "🇦🇷阿根廷",
    "AJMAN TV": "🇦🇷阿根廷",
    "AMMAN TV": "🇦🇷阿根廷",
    "ALRAIMEDIA": "🇦🇷阿根廷",
    "MEKAMELEEN": "🇦🇷阿根廷",
    "IFILM AR": "🇦🇷阿根廷",
    "YEMEN MAHRIAH": "🇦🇷阿根廷",
    "AL JAYLIA": "🇦🇷阿根廷",
    "ETIHAD": "🇦🇷阿根廷",
    "THAQAFEYYAH": "🇦🇷阿根廷",
    "AL HAQIQA": "🇦🇷阿根廷",
    "AL MASHHAD": "🇦🇷阿根廷",
    "AL YAUM": "🇦🇷阿根廷",
    "AL RABIAA": "🇦🇷阿根廷",
    "SAMA TV": "🇦🇷阿根廷",
    "AL DAFRAH": "🇦🇷阿根廷",
    "RAJEEN": "🇦🇷阿根廷",
    "QUDS TV": "🇦🇷阿根廷",
    "PAL PBC": "🇦🇷阿根廷",
    "MUSAWA": "🇦🇷阿根廷",
    "PAL TV": "🇦🇷阿根廷",
    "PAL SAT": "🇦🇷阿根廷",
    "FALASTINI TV": "🇦🇷阿根廷",
    "YEMEN TODAY": "🇦🇷阿根廷",
    "YEMEN SHABAB": "🇦🇷阿根廷",
    "UTV IRAQI": "🇦🇷阿根廷",
    "AL RASHEED": "🇦🇷阿根廷",
    "AL RAFIDAIN": "🇦🇷阿根廷",
    "WATAN EGYPT": "🇦🇷阿根廷",
    "QAF": "🇦🇷阿根廷",
    "SSAD TV": "🇦🇷阿根廷",
    "ISHTAR TV": "🇦🇷阿根廷",
    "LANA TV (backup)": "🇦🇷阿根廷",
    "AL ALARABY 2 (backup)": "🇦🇷阿根廷",
    "ROYA TV (backup)": "🇦🇷阿根廷",
    "ROYA TV [geoblocked]": "🇦🇷阿根廷",
    "LBC LBN [geoblocked]": "🇦🇷阿根廷",
    "OTV LBN [brokenlink]": "🇦🇷阿根廷",
    "DUBAI TV": "🇦🇷阿根廷",
    "DUBAI ONE": "🇦🇷阿根廷",
    "DUBAI NOOR": "🇦🇷阿根廷",
    "DUBAI SAMA": "🇦🇷阿根廷",
    "DUBAI ZAMAN": "🇦🇷阿根廷",
    "DUBAI SPORTS 1": "🇦🇷阿根廷",
    "DUBAI SPORTS 2": "🇦🇷阿根廷",
    "DUBAI SPORTS 3": "🇦🇷阿根廷",
    "DUBAI RACING 1": "🇦🇷阿根廷",
    "DUBAI RACING 2": "🇦🇷阿根廷",
    "DUBAI RACING 3": "🇦🇷阿根廷",
    "KAS QATAR 1": "🇦🇷阿根廷",
    "KAS QATAR 2": "🇦🇷阿根廷",
    "KAS QATAR 3": "🇦🇷阿根廷",
    "KAS QATAR 4": "🇦🇷阿根廷",
    "KAS QATAR 5": "🇦🇷阿根廷",
    "KAS QATAR 6": "🇦🇷阿根廷",
    "SAUDI SBC CH": "🇦🇷阿根廷",
    "SAUDIA TV CH 1": "🇦🇷阿根廷",
    "SAUDIA THIKRAYAT": "🇦🇷阿根廷",
    "SAUDI ACTION WALEED": "🇦🇷阿根廷",
    "OMAN 1": "🇦🇷阿根廷",
    "OMAN MUNASHER": "🇦🇷阿根廷",
    "OMAN CULTURE": "🇦🇷阿根廷",
    "OMAN SPORT": "🇦🇷阿根廷",
    "JORDAN TV": "🇦🇷阿根廷",
    "JORDAN TOURISM": "🇦🇷阿根廷",
    "JORDAN DRAMA": "🇦🇷阿根廷",
    "JORDAN COMEDY": "🇦🇷阿根廷",
    "KUWAIT TV 1": "🇦🇷阿根廷",
    "KUWAIT TV 2": "🇦🇷阿根廷",
    "KUWAIT TV ARAB": "🇦🇷阿根廷",
    "KUWAIT TV ETHRAA": "🇦🇷阿根廷",
    "KUWAIT TV KHALLIK": "🇦🇷阿根廷",
    "KUWAIT TV PLUS": "🇦🇷阿根廷",
    "KUWAIT TV SPORTS": "🇦🇷阿根廷",
    "KUWAIT TV SPORT PLUS": "🇦🇷阿根廷",
    "KUWAIT TV SPORT EXTRA": "🇦🇷阿根廷",
    "SAUDI CH 1": "🇦🇷阿根廷",
    "SAUDI CH 2": "🇦🇷阿根廷",
    "SAUDI CH 3": "🇦🇷阿根廷",
    "SAUDI CH 4": "🇦🇷阿根廷",
    "SAUDI CH 6 SUNNAH": "🇦🇷阿根廷",
    "SAUDI CH 7 KABE": "🇦🇷阿根廷",
    "SAUDI CH 9": "🇦🇷阿根廷",
    "SAUDI CH 10": "🇦🇷阿根廷",
    "SAUDI CH 17": "🇦🇷阿根廷",
    "AL JAZEERA": "🇦🇷阿根廷",
    "AL ARABIYA": "🇦🇷阿根廷",
    "AL ALARABY": "🇦🇷阿根廷",
    "AL ARABIYA HADATH": "🇦🇷阿根廷",
    "AL ARABIYA BUSINESS": "🇦🇷阿根廷",
    "AL JAZEERA MUBASHER": "🇦🇷阿根廷",
    "AL JAZEERA MUBASHER 2": "🇦🇷阿根廷",
    "AL HURRA": "🇦🇷阿根廷",
    "AL QAHERA NEWS": "🇦🇷阿根廷",
    "ASHARQ NEWS": "🇦🇷阿根廷",
    "ROYA NEWS": "🇦🇷阿根廷",
    "INEWS IQ": "🇦🇷阿根廷",
    "BBC NEWS ARABIA": "🇦🇷阿根廷",
    "SKY NEWS ARABIA": "🇦🇷阿根廷",
    "CNBC ARABIA": "🇦🇷阿根廷",
    "DW ARABIC": "🇦🇷阿根廷",
    "CGTN ARABIC": "🇦🇷阿根廷",
    "FRANCE 24 AR": "🇦🇷阿根廷",
    "TRT ARABIYA": "🇦🇷阿根廷",
    "AL ALAM IR [censure-ifany]": "🇦🇷阿根廷",
    "RT ARABIC [censure-blocked]": "🇦🇷阿根廷",
    "ASHARQ DOCS": "🇦🇷阿根廷",
    "ASHARQ DOCS 2": "🇦🇷阿根廷",
    "AL HIWAR": "🇦🇷阿根廷",
    "AL SHARQIYA": "🇦🇷阿根廷",
    "PANORAMA FM TV": "🇦🇷阿根廷",
    "EL SHARQ": "🇦🇷阿根廷",
    "WANASAH": "🇦🇷阿根廷",
    "MAJID": "🇦🇷阿根廷",
    "SPACE TOON": "🇦🇷阿根廷",
    "SAT7 KIDS": "🇦🇷阿根廷",
    "AL SHALLAL": "🇦🇷阿根廷",
    "TEN WEYYAK  [geoblocked]": "🇦🇷阿根廷",
    "IQRAA": "🇦🇷阿根廷",
    "IQRAA EUR": "🇦🇷阿根廷",
    "IQRAA 2": "🇦🇷阿根廷",
    "QURAN": "🇦🇷阿根廷",
    "BAHRAIN QURAN": "🇦🇷阿根廷",
    "SHARJAH QURAN": "🇦🇷阿根廷",
    "SALAM": "🇦🇷阿根廷",
    "AL QAMAR": "🇦🇷阿根廷",
    "ALMASIRA MUBASHER": "🇦🇷阿根廷",
    "AL EKHBARIA": "🇦🇷阿根廷",
    "AL SUNNAH TV": "🇦🇷阿根廷",
    "QURAN KAREEM TV": "🇦🇷阿根廷",
    "AL ISTIQAMA": "🇦🇷阿根廷",
    "SAT7 ARABIC": "🇦🇷阿根廷",
    "NOURSAT": "🇦🇷阿根廷",
    "NOURSAT AL SHARQ": "🇦🇷阿根廷",
    "NOURSAT AL KODDASS": "🇦🇷阿根廷",
    "NOURSAT EL SHABEB": "🇦🇷阿根廷",
    "NOURSAT MARIAM": "🇦🇷阿根廷",
    "NOURSAT ENG": "🇦🇷阿根廷",
    "CTV COPTIC": "🇦🇷阿根廷",
    "ASHARQ NEWS (backup)": "🇦🇷阿根廷",
    "ASHARQ NEWS (portrait mode)": "🇦🇷阿根廷",
    "AL ARABY (backup)": "🇦🇷阿根廷",
    "AL ARABY 2 (part-time)": "🇦🇷阿根廷",
    "BBC NEWS ARABIA (backup)": "🇦🇷阿根廷",
    "MAAN NEWS [issue]": "🇦🇷阿根廷",
    "CARTOON NETWORK AR [down]": "🇦🇷阿根廷",
    "GULLI ARABI [down]": "🇦🇷阿根廷",
    "MBC 1": "🇦🇷阿根廷",
    "MBC 3": "🇦🇷阿根廷",
    "MBC 4": "🇦🇷阿根廷",
    "MBC 5": "🇦🇷阿根廷",
    "MBC DRAMA": "🇦🇷阿根廷",
    "MBC DRAMA PLUS": "🇦🇷阿根廷",
    "MBC MASR 1": "🇦🇷阿根廷",
    "MBC MASR 2": "🇦🇷阿根廷",
    "MBC IRAQ": "🇦🇷阿根廷",
    "MBC BOLLYWOOD": "🇦🇷阿根廷",
    "MBC AFLAM": "🇦🇷阿根廷",
    "MBC MOVIES": "🇦🇷阿根廷",
    "MBC MOVIES ACTION": "🇦🇷阿根廷",
    "MBC MOVIES THRILLER": "🇦🇷阿根廷",
    "MBC FM LIVE TV": "🇦🇷阿根廷",
    "ROTANA CINEMA KSA": "🇦🇷阿根廷",
    "ROTANA KHALIJA": "🇦🇷阿根廷",
    "ROTANA CLIP": "🇦🇷阿根廷",
    "ROTANA COMEDY": "🇦🇷阿根廷",
    "CBC LIVE": "🇦🇷阿根廷",
    "CBC SOFRA": "🇦🇷阿根廷",
    "CBC NEWS": "🇦🇷阿根廷",
    "ROTANA CINEMA MASR": "🇦🇷阿根廷",
    "ROTANA PLUS": "🇦🇷阿根廷",
    "ROTANA KIDS": "🇦🇷阿根廷",
    "ROTANA CLASSIC": "🇦🇷阿根廷",
    "ROTANA DRAMA": "🇦🇷阿根廷",
    "ROTANA DUHK WABASS": "🇦🇷阿根廷",
    "SHAHID AL ZAEEM": "🇦🇷阿根廷",
    "SHAHID AL MASRAH": "🇦🇷阿根廷",
    "SHAHID AL USTURA": "🇦🇷阿根廷",
    "SHAHID COMEDY": "🇦🇷阿根廷",
    "SHAHID 1": "🇦🇷阿根廷",
    "SHAHID SHAM": "🇦🇷阿根廷",
    "SHAHID MAQALEB": "🇦🇷阿根廷",
    "SHAHID AL ZARAQ": "🇦🇷阿根廷",
    "ZEE AFLAM [geoblocked]": "🇦🇷阿根廷",
    "ZEE ALWAN [geoblocked]": "🇦🇷阿根廷",
    "WEYYAK DRAMA [geoblocked]": "🇦🇷阿根廷",
    "WEYYAK MIX [geoblocked]": "🇦🇷阿根廷",
    "WEYYAK ACTION [geoblocked]": "🇦🇷阿根廷",
    "WEYYAK NAWAEM [geoblocked]": "🇦🇷阿根廷",
    "MBC 1 [offlink]": "🇦🇷阿根廷",
    "MBC MASR 1 [offlink]": "🇦🇷阿根廷",
    "RAI NEWS 24 (sometimes)": "🇮🇹意大利",
    "RAI 3": "🇮🇹意大利",
    "CLASS CNBC": "🇮🇹意大利",
    "LA C NEWS 24": "🇮🇹意大利",
    "TELETICINO": "🇮🇹意大利",
    "LA 7": "🇮🇹意大利",
    "LA 7D": "🇮🇹意大利",
    "ITALIA 2 TV": "🇮🇹意大利",
    "RETE TV": "🇮🇹意大利",
    "RETE 55": "🇮🇹意大利",
    "CANALE 7": "🇮🇹意大利",
    "CAFE TV 24": "🇮🇹意大利",
    "RADIO 105 TV": "🇮🇹意大利",
    "DEEJAY TV": "🇮🇹意大利",
    "RADIO ITALIA TV": "🇮🇹意大利",
    "RADIO KISS KISS TV": "🇮🇹意大利",
    "R101 TV": "🇮🇹意大利",
    "RTL 102.5": "🇮🇹意大利",
    "SUPER!": "🇮🇹意大利",
    "EXTRA TV": "🇮🇹意大利",
    "SPORT ITALIA": "🇮🇹意大利",
    "SPORT ITALIA LIVE": "🇮🇹意大利",
    "RTV S.MARINO": "🇮🇹意大利",
    "GO-TV": "🇮🇹意大利",
    "SUPER TENNIS": "🇮🇹意大利",
    "RADIO MONTECARLO TV": "🇮🇹意大利",
    "VIRGIN RADIO TV": "🇮🇹意大利",
    "ALTO ADIGE TV": "🇮🇹意大利",
    "ANRENNA 2 BERGAMO": "🇮🇹意大利",
    "ANTENNA 3 VENETO": "🇮🇹意大利",
    "ANTENNA SUD": "🇮🇹意大利",
    "ANTENNA SUD EXTRA": "🇮🇹意大利",
    "ARISTANIS TV": "🇮🇹意大利",
    "ARTE NETWORK": "🇮🇹意大利",
    "AURORA ARTE": "🇮🇹意大利",
    "AZZURRA TV": "🇮🇹意大利",
    "EURONEWS IT": "🇮🇹意大利",
    "TAGESSCHAU 24": "🇩🇪德意志",
    "DAS ERSTE INTL": "🇩🇪德意志",
    "DAS ERSTE DE": "🇩🇪德意志",
    "RTL DE": "🇩🇪德意志",
    "ALPHA ARD": "🇩🇪德意志",
    "BR DE": "🇩🇪德意志",
    "HR DE": "🇩🇪德意志",
    "SR DE": "🇩🇪德意志",
    "WDR DE": "🇩🇪德意志",
    "ARTE DE": "🇩🇪德意志",
    "EURONEWS DE": "🇩🇪德意志",
    "RT DEUTSCH [censure-blocked]": "🇩🇪德意志",
    "RTL LUX": "🇱🇺卢森堡",
    "RTL HR": "🇭🇷克罗地亚",
    "HRT 1": "🇭🇷克罗地亚",
    "HRT 2": "🇭🇷克罗地亚",
    "HRT 3": "🇭🇷克罗地亚",
    "RTS 1": "🇷🇸塞尔维亚",
    "RTS 2": "🇷🇸塞尔维亚",
    "PINK": "🇷🇸塞尔维亚",
    "TVR INT": "🇷🇴罗马尼亚",
    "ANTENA 1 RO": "🇷🇴罗马尼亚",
    "ANTENA 3 VOX": "🇷🇴罗马尼亚",
    "KANAL D RO": "🇷🇴罗马尼亚",
    "KANAL D2 RO": "🇷🇴罗马尼亚",
    "MOLDOVA 1": "🇲🇩摩尔多瓦",
    "MOLDOVA 2": "🇲🇩摩尔多瓦",
    "GPB 1TV პირველი არხი": "格鲁吉亚-亚美尼亚-捷克",
    "GPB 2TV": "格鲁吉亚-亚美尼亚-捷克",
    "IMEDI": "格鲁吉亚-亚美尼亚-捷克",
    "RUSTAVI 2": "格鲁吉亚-亚美尼亚-捷克",
    "PALITRA": "格鲁吉亚-亚美尼亚-捷克",
    "FORMULA": "格鲁吉亚-亚美尼亚-捷克",
    "ADJARA": "格鲁吉亚-亚美尼亚-捷克",
    "MTAVARI ARKHI": "格鲁吉亚-亚美尼亚-捷克",
    "H1 ARM Հանրային հեռուստաը": "格鲁吉亚-亚美尼亚-捷克",
    "H1 NEWS": "格鲁吉亚-亚美尼亚-捷克",
    "SONG ARM": "格鲁吉亚-亚美尼亚-捷克",
    "AZ TV Azərbaycan Televiziyası": "格鲁吉亚-亚美尼亚-捷克",
    "AZ NEWS": "格鲁吉亚-亚美尼亚-捷克",
    "AZ STAR": "格鲁吉亚-亚美尼亚-捷克",
    "ATV AZ": "格鲁吉亚-亚美尼亚-捷克",
    "BAKU TV": "格鲁吉亚-亚美尼亚-捷克",
    "UMİT TV": "格鲁吉亚-亚美尼亚-捷克",
    "MEDENİYYET": "格鲁吉亚-亚美尼亚-捷克",
    "IRIB 1": "🇮🇷伊朗",
    "IRIB 2": "🇮🇷伊朗",
    "IRIB 3": "🇮🇷伊朗",
    "IRIB 4": "🇮🇷伊朗",
    "IRIB 5": "🇮🇷伊朗",
    "IRIB AMOOZESH": "🇮🇷伊朗",
    "IRIB MOSTANAD": "🇮🇷伊朗",
    "IRIB NAMAYESH": "🇮🇷伊朗",
    "IRIB NASIM": "🇮🇷伊朗",
    "IRIB POOYA": "🇮🇷伊朗",
    "IRIB SALAMAT": "🇮🇷伊朗",
    "IRIB TAMASHA": "🇮🇷伊朗",
    "IRIB VARZESH": "🇮🇷伊朗",
    "IRIB MESRAFSANJAN": "🇮🇷伊朗",
    "IRIB ESHAREH": "🇮🇷伊朗",
    "IRIB IRINN": "🇮🇷伊朗",
    "IRIB AIOSPORT": "🇮🇷伊朗",
    "IRIB AIOSPORT 2": "🇮🇷伊朗",
    "IRIB IFILM FAR 1": "🇮🇷伊朗",
    "IRIB IFILM FAR 2": "🇮🇷伊朗",
    "MBC PERSIA": "🇮🇷伊朗",
    "HASTI TV": "🇮🇷伊朗",
    "ASIL TV": "🇮🇷伊朗",
    "SNN TV": "🇮🇷伊朗",
    "NEJAT TV": "🇮🇷伊朗",
    "VOX 1": "🇮🇷伊朗",
    "YOUR TIME": "🇮🇷伊朗",
    "HOD HOD": "🇮🇷伊朗",
    "24/7 BOX": "🇮🇷伊朗",
    "OX IR": "🇮🇷伊朗",
    "AVA FAMILY": "🇮🇷伊朗",
    "PARS": "🇮🇷伊朗",
    "SL ONE": "🇮🇷伊朗",
    "SL TWO": "🇮🇷伊朗",
    "P FILM": "🇮🇷伊朗",
    "ITN": "🇮🇷伊朗",
    "META FILM": "🇮🇷伊朗",
    "AVA SERIES": "🇮🇷伊朗",
    "BRAVOO": "🇮🇷伊朗",
    "FX TV": "🇮🇷伊朗",
    "OI TN": "🇮🇷伊朗",
    "TAPESH": "🇮🇷伊朗",
    "TAPESH IR": "🇮🇷伊朗",
    "MIHAN TV": "🇮🇷伊朗",
    "NEGAH TV": "🇮🇷伊朗",
    "AL WILAYAH": "🇮🇷伊朗",
    "PAYVAND": "🇮🇷伊朗",
    "PJ TV": "🇮🇷伊朗",
    "ASSIRAT": "🇮🇷伊朗",
    "PERSIANA NOSTALGIA": "🇮🇷伊朗",
    "PERSIANA MUSIC": "🇮🇷伊朗",
    "PERSIANA TURKIYE": "🇮🇷伊朗",
    "PERSIANA COMEDY": "🇮🇷伊朗",
    "PERSIANA IRANIAN": "🇮🇷伊朗",
    "PERSIANA ONE": "🇮🇷伊朗",
    "PERSIANA TWO": "🇮🇷伊朗",
    "PERSIANA KOREA": "🇮🇷伊朗",
    "PERSIANA CINEMA": "🇮🇷伊朗",
    "PERSIANA HD": "🇮🇷伊朗",
    "PERSIANA LATINO": "🇮🇷伊朗",
    "PERSIANA FAMILY": "🇮🇷伊朗",
    "PERSIANA SCIENCE": "🇮🇷伊朗",
    "PERSIANA JUNIOR": "🇮🇷伊朗",
    "IRIB 1 (backup)": "🇮🇷伊朗",
    "IRIB 2 (backup)": "🇮🇷伊朗",
    "IRIB 3 (backup)": "🇮🇷伊朗",
    "IRIB 4 (backup)": "🇮🇷伊朗",
    "IRIB 5 (backup)": "🇮🇷伊朗",
    "IRIB IRINN (backup)": "🇮🇷伊朗"
}

# 新的 M3U 播放地址内容
new_m3u_content = """
#EXTINF:-1 tvg-logo="https://i.ibb.co/kckRLh5/bfm.png" group-title="1. |FR|🇫🇷 INFORMATION",BFM TV
https://ncdn-live-bfm.pfd.sfr.net/shls/LIVE$BFM_TV/index.m3u8?start=LIVE&end=END
#EXTINF:-1 tvg-logo="https://i.ibb.co/qY6w8ds/cnews.png",CNEWS
https://hls-m015-live-aka-canalplus.akamaized.net/live/disk/cnews-clair-hd/hls-v3-hd-clair/cnews-clair-hd.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Zfcrrr1/lci.png",LCI
https://raw.githubusercontent.com/ipstreet312/freeiptv/master/ressources/btv/py/lci1.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/XkLHrbC/frinfo2bl.png",FRANCE INFO:
https://raw.githubusercontent.com/ipstreet312/freeiptv/master/ressources/ftv/py/frin.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/ZBqk6mK/lemedia.jpg",LE MÉDIA TV
https://raw.githubusercontent.com/BG47510/tube/refs/heads/main/lemedia.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/ZBqk6mK/lemedia.jpg",LE MÉDIA TV -1H
https://tvradiozap.eu/tools/mng-m3u8.php/936.1/60/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/VxLFYSj/euronews.png",EURONEWS FR
https://euronews-live-fre-fr.fast.rakuten.tv/v1/master/0547f18649bd788bec7b67b746e47670f558b6b2/production-LiveChannel-6564/bitok/e/26032/euronews-fr.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/drk4BWw/tv5inf.png",TV5MONDE INFO
https://ott.tv5monde.com/Content/HLS/Live/channel(info)/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/hKP8X8B/f24.png",FRANCE 24 FR
https://live.france24.com/hls/live/2037179/F24_FR_HI_HLS/master_5000.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/rkv3Nvq/lcpan.png",LCP-AN
https://raw.githubusercontent.com/ipstreet312/freeiptv/refs/heads/master/ressources/dmotion/py/lcpan/lcp1.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/2jG942b/publicsn.png",PUBLIC-SÉNAT
https://raw.githubusercontent.com/Paradise-91/ParaTV/main/streams/publicsenat/publicsenat-dm.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/2MhqYgg/bfm2.png",BFM 2
https://live-cdn-bfm2-euw1.bfmtv.bct.nextradiotv.com/m5/media.m3u8?bpkio_serviceid=7de32147a4f1055b8812bbac92a24d2e
#EXTINF:-1 tvg-logo="https://i.ibb.co/ChVvjpF/bfmgr.jpg",BFM GRAND REPORTAGES
https://ncdn-live-bfm.pfd.sfr.net/shls/LIVE$BFM_GRANDSREPORTAGES/index.m3u8?start=LIVE&end=END
#EXTINF:-1 tvg-logo="https://i.ibb.co/k4Bs0Cj/rmcti.jpg",RMC TALK INFO
https://dvvyqyxwlc4tn.cloudfront.net/v1/master/3722c60a815c199d9c0ef36c5b73da68a62b09d1/cc-n5yqxqrvnujl7/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/5j6DZrt/20mn.png",20 MINUTES TV IDF
https://live-20minutestv.digiteka.com/1961167769/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/hcPj99k/fgro.png",LE FIGARO IDF
https://static.lefigaro.fr/secom/tnt.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/hcPj99k/fgro.png",LE FIGARO LIVE
https://d358c6mfrono1y.cloudfront.net/v1/manifest/3722c60a815c199d9c0ef36c5b73da68a62b09d1/cc-0ppx9nh29jpk7-prod/fa5bf751-4c1a-465b-97bd-1fa62e8a7d00/2.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/j68q1Bp/i24.png",i24 NEWS FR
https://bcovlive-a.akamaihd.net/41814196d97e433fb401c5e632d985e9/eu-central-1/5377161796001/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/ZgqnqnJ/cgtnfr.png",CGTN FRANÇAIS
http://news.cgtn.com/resource/live/french/cgtn-f.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/nR2HsVr/ln24.png",LN24 BE
https://live-ln24.digiteka.com/1911668011/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/MZLCTmN/monacoinfo.png",MONACO INFO
https://webtv.monacoinfo.com/live/prod/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/sd7qf1w7/icirdiqb.png",RDI CANADA
https://rcavlive.akamaized.net/hls/live/704025/xcanrdi/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/pdnMrZn/a24.png",AFRICA 24 FR
https://africa24.vedge.infomaniak.com/livecast/ik:africa24/manifest.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/XSYtYHZ/africanews.png",AFRICANEWS FR
https://cdn-euronews.akamaized.net/live/eds/africanews-fr/25050/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/HDB0sdh/bfmbusiness.png",BFM BUSINESS
https://ncdn-live-bfm.pfd.sfr.net/shls/LIVE$BFM_BUSINESS/index.m3u8?start=LIVE&end=END
#EXTINF:-1 tvg-logo="https://i.ibb.co/Tm8bZHc/bsmart.png",B SMART
https://raw.githubusercontent.com/Sibprod/streams/main/ressources/dm/py/hls/bsmart.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Nn5x9Hq/bloom.jpg",BLOOMBERG FR
https://bloomberg-bloombergtv-1-fr.samsung.wurl.tv/manifest/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/cCXgWWw/tvfinance.jpg",TV FINANCE
https://strhlslb01.streamakaci.tv/str_tvfinance_tvfinance/str_tvfinance_multi/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/rwbrckj/pressir.png",PRESS IR FRENCH [temp barker]
https://live4.presstv.ir/live/smil:presstvfr.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/D7w9h7Q/rt.png",RT FRANÇAIS [censure-blocked]
https://rt-fra.rttv.com/live/rtfrance/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/D7w9h7Q/rt.png",RT FRANÇAIS [censure-blocked]
https://rt-fra.rttv.com/dvr/rtfrance/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/D7w9h7Q/rt.png",RT FRANÇAIS [censure-blocked]
http://69.64.57.208:8080/rtfrance/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/D7w9h7Q/rt.png",RT FRANÇAIS [censure-blocked]
https://librarian.pussthecat.org/live/content/a6a125c99ba2a6c068a8b502fb08dda603f6f03a/live.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/kckRLh5/bfm.png",BFM TV (backup)
https://live-cdn-stream-euw1.bfmtv.bct.nextradiotv.com/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/kckRLh5/bfm.png",BFM TV (backup)
https://live-cdn-stream-euw1.bfmtv.bct.nextradiotv.com/master.m3u8?bpkio_serviceid=7de32147a4f1055b7ea82c2886420955
#EXTINF:-1 tvg-logo="https://i.ibb.co/kckRLh5/bfm.png",BFM TV (backup)
https://live-cdn-stream-euw1.bfmtv.bct.nextradiotv.com/m1/media.m3u8?bpkio_serviceid=7de32147a4f1055b7ea82c2886420955
#EXTINF:-1 tvg-logo="https://i.ibb.co/kckRLh5/bfm.png",BFM TV (backup)
https://mit2-cdn-edge-live06.pfd.sfr.net/bfm-ncdn-live-premium-pal1.pfd.sfr.net/sid=054akapminjaseksmkrg/shls/LIVE$BFM_TV/index.m3u8?start=LIVE&end=END
#EXTINF:-1 tvg-logo="https://i.ibb.co/kckRLh5/bfm.png",BFM TV (backup)
https://d133u1kwyeqhav.cloudfront.net/v1/master/3722c60a815c199d9c0ef36c5b73da68a62b09d1/cc-cfh0ys5588w7f/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/kckRLh5/bfm.png",BFM TV (backup)
https://d2me2cx8crwpp6.cloudfront.net/v1/master/3722c60a815c199d9c0ef36c5b73da68a62b09d1/cc-456wmaba0e7dw/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/2MhqYgg/bfm2.png",BFM 2 (backup)
https://ncdn-live-bfm.pfd.sfr.net/shls/LIVE$BFM2/index.m3u8?start=LIVE&end=END
#EXTINF:-1 tvg-logo="https://i.ibb.co/2MhqYgg/bfm2.png",BFM 2 (backup)
https://live-cdn-bfm2-euw1.bfmtv.bct.nextradiotv.com/m1/media.m3u8?bpkio_serviceid=7de32147a4f1055b8812bbac92a24d2e
#EXTINF:-1 tvg-logo="https://i.ibb.co/2MhqYgg/bfm2.png",BFM 2 (backup)
https://d1ib1gsg71oarf.cloudfront.net/v1/master/3722c60a815c199d9c0ef36c5b73da68a62b09d1/cc-scp7wda722jph/BFM2_FR.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/HDB0sdh/bfmbusiness.png",BFM BUSINESS (backup)
https://d3sp7wui50dz5c.cloudfront.net/v1/master/3722c60a815c199d9c0ef36c5b73da68a62b09d1/cc-dxxit4lrci140/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/HDB0sdh/bfmbusiness.png",BFM BUSINESS (backup)
https://live-cdn-stream-euw1.bfmb.bct.nextradiotv.com/m1/media.m3u8?bpkio_serviceid=7de32147a4f1055b7de133c00ff64f92
#EXTINF:-1 tvg-logo="https://i.ibb.co/ZBqk6mK/lemedia.jpg",LE MÉDIA TV (backup ko)
https://tvradiozap.eu/936
#EXTINF:-1 tvg-logo="https://i.ibb.co/ZBqk6mK/lemedia.jpg",LE MÉDIA TV (backup ko)
https://livestream.zazerconer.workers.dev/channel/UCT67YOMntJxfRnO_9bXDpvw.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/drk4BWw/tv5inf.png",TV5MONDE INFO (backup)
https://stream.ads.ottera.tv/playlist.m3u8?network_id=7433
#EXTINF:-1 tvg-logo="https://i.ibb.co/VxLFYSj/euronews.png",EURONEWS FR (backup)
https://shls-live-ak.akamaized.net/out/v1/302a3ad418214d3f94460738a805b930/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/VxLFYSj/euronews.png",EURONEWS FR (backup)
https://7c8b7dbf12d64234a983336fdddb88c2.mediatailor.us-east-1.amazonaws.com/v1/master/44f73ba4d03e9607dcd9bebdcb8494d86964f1d8/Samsung-fr_EuroNewsLive/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/VxLFYSj/euronews.png",EURONEWS FR (backup)
https://rakuten-euronews-2-fr.lg.wurl.tv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/VxLFYSj/euronews.png",EURONEWS FR (backup)
https://jmp2.uk/sam-FR2600004SS.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/VxLFYSj/euronews.png",EURONEWS FR (backup)
https://rakuten-euronews-2-fr.samsung.wurl.tv/manifest/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/VxLFYSj/euronews.png",EURONEWS FR (backup)
http://stitcher-ipv4.pluto.tv/v1/stitch/embed/hls/channel/60d35bcaf1ff4a00078af0a6livestitch/master.m3u8?deviceDNT=%7BTARGETOPT%7D&deviceModel=samsung&deviceVersion=unknown&appVersion=unknown&deviceType=samsung-tvplus&deviceMake=samsung
#EXTINF:-1 tvg-logo="https://i.ibb.co/XkLHrbC/frinfo2bl.png",FRANCE INFO: (backup)
https://raw.githubusercontent.com/ipstreet312/freeiptv/master/ressources/ftv/py2/frinnv.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/XkLHrbC/frinfo2bl.png",FRANCE INFO: (backup)
https://livestream.zazerconer.workers.dev/channel/UCO6K_kkdP-lnSCiO3tPx7WA/live.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/XkLHrbC/frinfo2bl.png",FRANCE INFO: (backup)
https://new.cache-stream.workers.dev/channel/UCO6K_kkdP-lnSCiO3tPx7WA/live.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/XkLHrbC/frinfo2bl.png",FRANCE INFO: (backup)
https://ythls.armelin.one/channel/UCO6K_kkdP-lnSCiO3tPx7WA.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/XkLHrbC/frinfo2bl.png",FRANCE INFO: (backup-off)
https://raw.githubusercontent.com/ipstreet312/freeiptv/master/ressources/dmotion/py/frinfo/frinfo.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/XkLHrbC/frinfo2bl.png",FRANCE INFO: [find-host]
https://PuthereYourserverHostaddress/frijsoncurl.php?m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/hKP8X8B/f24.png",FRANCE 24 FR (backup)
https://live.france24.com/hls/live/2037179/F24_FR_HI_HLS/master_2300.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/hKP8X8B/f24.png",FRANCE 24 FR (backup)
https://ythls-v3.onrender.com/video/l8PMl7tUDIE.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/hKP8X8B/f24.png",FRANCE 24 FR (backup)
https://new.cache-stream.workers.dev/channel/UCCCPCZNChQdGa9EkATeye4g/live.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/hKP8X8B/f24.png",FRANCE 24 FR (backup-off)
https://d4de59d01af447a498cb0565ad005588.mediatailor.us-east-1.amazonaws.com/v1/master/82ded7a88773aef3d6dd1fedce15ba2d57eb6bca/viewmedia-7/live_092/HD/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/drk4BWw/tv5inf.png",TV5MONDE INFO (backup)
https://d161b1o6wfc5a3.cloudfront.net/v1/master/3722c60a815c199d9c0ef36c5b73da68a62b09d1/cc-3u7sgewc3l8ri/tvfm.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Zfcrrr1/lci.png",LCI (backup)
https://raw.githubusercontent.com/schumijo/iptv/main/playlists/mytf1/lci.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Zfcrrr1/lci.png",LCI (backup)
https://raw.githubusercontent.com/Paradise-91/ParaTV/main/streams/tf1plus/lci.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/qY6w8ds/cnews.png",CNEWS (backup)
https://hls-m015-live-aka-canalplus.akamaized.net/live/disk/cnews-clair-hd/hls-ios-fhd-clair/cnews-clair-hd.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/qY6w8ds/cnews.png",CNEWS (backup)
https://hls-m015-live-aka-canalplus.akamaized.net/live/disk/cnews-clair-ad-hd/hls-ios-fhd-clair/cnews-clair-ad-hd.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/qY6w8ds/cnews.png",CNEWS (backup)
https://hls-m015-live-aka-canalplus.akamaized.net/live/disk/cnews-clair-ad-hd/hls-v3-hd-clair/cnews-clair-ad-hd.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/qY6w8ds/cnews.png",CNEWS (backup)
https://hls-m015.p-cdnlive-edge020311-dual.scy.canalplus-cdn.net/__token__id%3D1a569a48e47690c700c0f71662c87679~hmac%3D6d2114baa9bb694f530073a9f707530612577a89d4d0a36aaa72374fa9e12049/live/disk/cnews-clair-ad-hd/hls-ios-fhd-clair/cnews-clair-ad-hd.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/qY6w8ds/cnews.png",CNEWS (backup)
https://hls-m015.p-cdnlive-edge020411-dual.scy.canalplus-cdn.net/__token__id%3D30d0283c7e891418deaddd2079712aaa~hmac%3Db2612e5607aecd3745717271a89b4c9f30d655071475de4667bf4819c57cd756/live/disk/cnews-clair-hd/hls-v3-hd-clair/cnews-clair-hd.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/qY6w8ds/cnews.png",CNEWS (backup)
https://raw.githubusercontent.com/Paradise-91/ParaTV/refs/heads/main/streams/canalplus/cnews-dm.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/ZBqk6mK/lemedia.jpg",LE MÉDIA TV (backup)
https://raw.githubusercontent.com/Sibprod/streams/main/ressources/dm/py/hls/lemedia.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/ZBqk6mK/lemedia.jpg",LE MÉDIA TV (backup)
https://new.cache-stream.workers.dev/stream/UCT67YOMntJxfRnO_9bXDpvw/live.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/ZBqk6mK/lemedia.jpg",LE MÉDIA TV (backup)
https://raw.githubusercontent.com/BG47510/tube/main/lemedia.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/hKP8X8B/f24.png",FRANCE 24 FR (backup)
https://new.cache-stream.workers.dev/channel/UCCCPCZNChQdGa9EkATeye4g/live.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/rkv3Nvq/lcpan.png",LCP-AN (backup)
https://raw.githubusercontent.com/Sibprod/streams/main/ressources/dm/py/hls/LCP.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/hcPj99k/fgro.png",LE FIGARO IDF (backup)
https://figarotv-live.freecaster.com/live/freecaster/figarotv.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/ZgqnqnJ/cgtnfr.png",CGTN FRANÇAIS (backup)
https://livefr.cgtn.com/1000f/prog_index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/ZgqnqnJ/cgtnfr.png",CGTN FRANÇAIS (backup)
https://amg01314-cgtn-amg01314c2-rakuten-us-1319.playouts.now.amagi.tv/cgtn-fr-rakuten/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/sq11nQ1/rdicanada.png",RDI CANADA (backup)
https://d352zobhe5lhe6.cloudfront.net/v1/master/3722c60a815c199d9c0ef36c5b73da68a62b09d1/cc-j7m6inrqe6jat/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/XSYtYHZ/africanews.png",AFRICANEWS FR (backup)
https://stream.ads.ottera.tv/playlist.m3u8?network_id=10951
#EXTINF:-1 tvg-logo="https://i.ibb.co/XSYtYHZ/africanews.png",AFRICANEWS FR (backup)
https://fd455e302ce44beb82997b99d4d215fc.mediatailor.us-east-1.amazonaws.com/v1/master/04fd913bb278d8775298c26fdca9d9841f37601f/RakutenTV-fr_AfricaNews/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Zfcrrr1/lci.png",LCI [tkn-blocked]
https://live-lci-hls.cdn-0.diff.tf1.fr/out/v1/917aad4fa72f42f7ba7f486226f54bc4/lci-cmaf/index.m3u8


#EXTINF:-1 tvg-logo="https://i.ibb.co/pQ7kLNY/tv5fbs.png" group-title="2. |FR|🇫🇷 GÉNÉRALISTE",TV5MONDE FBSM
https://ott.tv5monde.com/Content/HLS/Live/channel(fbs)/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/BBpR1Wx/tf1.png",TF1
https://raw.githubusercontent.com/Paradise-91/ParaTV/main/streams/tf1plus/tf1.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/GxWtcTm/fr2bl.png",FRANCE 2
https://raw.githubusercontent.com/ipstreet312/freeiptv/master/ressources/ftv/py/fr2.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/y8PjbJ4/fr3bl.png",FRANCE 3
https://raw.githubusercontent.com/ipstreet312/freeiptv/master/ressources/ftv/py/fr3.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/VgcrtZ5/fr4blok.png",FRANCE 4
https://raw.githubusercontent.com/ipstreet312/freeiptv/master/ressources/ftv/py/fr4.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/N9d4yXt/fr5bl.png",FRANCE 5
https://raw.githubusercontent.com/ipstreet312/freeiptv/master/ressources/ftv/py/fr5.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/9rmSGqP/frsr.png",FRANCE TV SÉRIES
https://raw.githubusercontent.com/ipstreet312/freeiptv/master/ressources/ftv/py/frserv2.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/kJjHW61/frdocs.png",FRANCE TV DOCUMENTAIRES
https://raw.githubusercontent.com/ipstreet312/freeiptv/master/ressources/ftv/py/frdocv2.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/BPpZPBn/arte.png",ARTE
https://artesimulcast.akamaized.net/hls/live/2031003/artelive_fr/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/BPpZPBn/arte.png",ARTE -0,5H
https://tvradiozap.eu/tools/mng-m3u8.php/640.2/30/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/R3KG4L9/cherie25.png",CHÉRIE 25
https://cherie25.nrjaudio.fm/hls/live/2038375/c25/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/ftYS2bk/CANAL-logo.png",CANAL+ EN CLAIR
https://hls-m005.p-cdnlive-edge020311-dual.scy.canalplus-cdn.net/__token__id%3D1a569a48e47690c700c0f71662c87679~hmac%3D6d2114baa9bb694f530073a9f707530612577a89d4d0a36aaa72374fa9e12049/live/disk/canalplusclair-hd/hls-v3-hd-clair/canalplusclair-hd.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/fdYg3Lz/rmcstory.png",RMC STORY
https://d36bxc1bknkxrk.cloudfront.net/v1/master/3722c60a815c199d9c0ef36c5b73da68a62b09d1/cc-3ewcp19zjaxpt/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/VS4xR2g/rmcdecou.png",RMC DÉCOUVERTE
https://d2mt8for1pddy4.cloudfront.net/v1/master/3722c60a815c199d9c0ef36c5b73da68a62b09d1/cc-6uronj7gzvy4j/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Sm9PtLR/cstar.png",CSTAR
https://raw.githubusercontent.com/Paradise-91/ParaTV/refs/heads/main/streams/canalplus/cstar-dm.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/hKVyKj4/tmc.png",TMC
https://github.com/Paradise-91/ParaTV/raw/main/streams/tf1plus/tmc.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/420Bjqt/tv5europe.png",TV5MONDE EUROPE [geo-area]
https://ott.tv5monde.com/Content/HLS/Live/channel(europe)/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/x8YnkQ2/tv5.png",TV5MONDE MOYEN-ORIENT [geo-area]
https://ott.tv5monde.com/Content/HLS/Live/channel(orient)/variant.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/x8YnkQ2/tv5.png",TV5MONDE ASIE SUD-EST [geo-area]
https://ott.tv5monde.com/Content/HLS/Live/channel(seasie)/variant.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/x8YnkQ2/tv5.png",TV5MONDE PACIFIQUE [geo-area]
https://ott.tv5monde.com/Content/HLS/Live/channel(pacifique)/variant.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/ftYS2bk/CANAL-logo.png",CANAL+ EN CLAIR (backup)
https://hls-m005.p-cdnlive-edge020311-dual.scy.canalplus-cdn.net/__token__id%3D30d0283c7e891418deaddd2079712aaa~hmac%3Db2612e5607aecd3745717271a89b4c9f30d655071475de4667bf4819c57cd756/live/disk/canalplusclair-hd/hls-ios-fhd-clair/canalplusclair-hd.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/R3KG4L9/cherie25.png" user-agent="SmartOs Tv",CHÉRIE 25 (backup)
https://raw.githubusercontent.com/ipstreet312/freeiptv/master/ressources/rtlm6/cherie25.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/wgJTdGY/m6.png",M6 [drm-keycrypted]
https://origin-18cd60dea8190528.live.6cloud.fr/out/v1/6bb64f06f28a4bfb8779bc1a386f7f0b/dash_short_cenc10_m6_hd_index.mpd
#EXTINF:-1 tvg-logo="https://i.ibb.co/wgJTdGY/m6.png",M6 [drm-keycrypted]
https://origin-18cd60dea8190528.live.6cloud.fr/out/v1/72072059b9d541feac3c9328728d8304/cmaf/hlsfmp4_short_fp00_m6_hd_index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/wgJTdGY/m6.png",M6 [drm-keycrypted]
https://origin-18cd60dea8190528.live.6cloud.fr/out/v1/25e13477c7c54bbe8f93e828f2234fca/cmaf/hlsfmp4_short_fp00_m6_sd_index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/LNRd253/w9.png",W9 [drm-keycrypted]
https://origin-18cd60dea8190528.live.6cloud.fr/out/v1/82a128a679444d3c9b4d68c1616e239a/hls_short_fp00_w9_hdeindex.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/LNRd253/w9.png",W9 [drm-keycrypted]
https://origin-18cd60dea8190528.live.6cloud.fr/out/v1/2babf2563b5b420caa743430699c096b/dash_short_cenc10_scte_w9_hdeindex.mpd
#EXTINF:-1 tvg-logo="https://i.ibb.co/nzh88j8/6ter.png",6TER [drm-keycrypted]
https://origin-caf900c010ea8046.live.6cloud.fr/out/v1/597b48a710164c0da9a4386bf9f7bef2/dash_short_cenc10_6ter_hdeindex.mpd
#EXTINF:-1 tvg-logo="https://i.ibb.co/6spXX2y/nrj12.png",NRJ 12 [OUT]
https://nrj12.nrjaudio.fm/hls/live/2038374/nrj_12/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/6spXX2y/nrj12.png" user-agent="SmartOs Tv",NRJ 12 [OUT]
https://raw.githubusercontent.com/ipstreet312/freeiptv/master/ressources/rtlm6/nrj12.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/cQbcrGZ/c8.png",C8 [OUT]
https://tvradiozap.eu/tools/dm-m3u8.php/x5gv5rr.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/cQbcrGZ/c8.png",C8 [OUT]
https://raw.githubusercontent.com/LeBazarDeBryan/XTVZ_/refs/heads/main/Stream/Live/C8.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Sm9PtLR/cstar.png",CSTAR (backup)
https://raw.githubusercontent.com/schumijo/iptv/main/playlists/canalplus/cstar.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/BBpR1Wx/tf1.png",TF1 (backup)
https://raw.githubusercontent.com/schumijo/iptv/main/playlists/mytf1/tf1.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/BBpR1Wx/tf1.png",TF1 (backup)
https://raw.githubusercontent.com/mikekaprielian/rtnaodhor93n398/main/fr/videotf1.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/BBpR1Wx/tf1.png",TF1 (backup)
http://live.tntdirect.tv/9CM2pADCxF/w5BA32MP6P/1.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/BBpR1Wx/tf1.png",TF1 (backup)
https://raw.githubusercontent.com/LeBazarDeBryan/XTVZ_/refs/heads/main/Stream/Live/TF1.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/GxWtcTm/fr2bl.png",FRANCE 2 (backup)
https://raw.githubusercontent.com/mikekaprielian/rtnaodhor93n398/refs/heads/main/fr/videof2.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/GxWtcTm/fr2bl.png",FRANCE 2 (backup)
https://raw.githubusercontent.com/ipstreet312/freeiptv/master/ressources/ftv/py2/fr2nv.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/y8PjbJ4/fr3bl.png",FRANCE 3 (backup)
https://raw.githubusercontent.com/ipstreet312/freeiptv/master/ressources/ftv/py2/fr3nv.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/VgcrtZ5/fr4blok.png",FRANCE 4 (backup)
https://raw.githubusercontent.com/ipstreet312/freeiptv/master/ressources/ftv/py2/fr4nv.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/N9d4yXt/fr5bl.png",FRANCE 5 (backup)
https://raw.githubusercontent.com/ipstreet312/freeiptv/master/ressources/ftv/py2/fr5nv.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/BPpZPBn/arte.png",ARTE (backup)
https://raw.githubusercontent.com/ipstreet312/freeiptv/refs/heads/master/ressources/ftv/py/frarte.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/LNRd253/w9.png" user-agent="VAVOO/1.0" referer="https://vavoo.to/",W9 (test)
https://joaquinito02.es/vavoo/128046615.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/wgJTdGY/m6.png",M6 (backup)
http://live.tntdirect.tv/9CM2pADCxF/w5BA32MP6P/6.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/wgJTdGY/m6.png",M6 (backup)
https://live.tntdirect.tv/9CM2pADCxF/w5BA32MP6P/6.ts
#EXTINF:-1 tvg-logo="https://i.ibb.co/wgJTdGY/m6.png",M6 (backup)
https://live.tntdirect.tv/9CM2pADCxF/w5BA32MP6P/6.ts?extension=m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/wgJTdGY/m6.png",M6 (test)
http://gratuittv.free.fr/Files/m6/live/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/LNRd253/w9.png",W9 (check)
http://gratuittv.free.fr/Files/w9/live/playlist.m3u8


#EXTINF:-1 tvg-logo="https://i.ibb.co/ByN83p3/funradtv.png" group-title="3. |FR|🇫🇷 SOCIÉTÉ",FUN RADIO TV BE
https://funradiovisionhd.vedge.infomaniak.com/livecast/ik:funradiovisionhd/manifest.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/ByN83p3/funradtv.png",FUN RADIO TV FR
https://raw.githubusercontent.com/Sibprod/streams/main/ressources/dm/py/hls/funradiofr.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/g3YTn6c/geneok.png",GÉNÉRATIONS TV
https://edge11.vedge.infomaniak.com/livecast/ik:generation-tv/manifest.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/BPzb19X/melody.png",MÉLODY
https://live.creacast.com/telemelody/smil:telemelody-yjvCxE7x.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/svWdczbW/ina.png",INA 70s
https://raw.githubusercontent.com/ipstreet312/freeiptv/master/ressources/ftv/py2/frina.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/svWdczbW/ina.png",INA 70s
https://fast-rakuten.okast.tv/channels/34d82f76-b51f-4bf5-9b35-769fb5904e79/96f96405-90e7-489a-a1e6-8ede5d2b4933/media_.m3u8?bpkio_serviceid=fa2e8c4385712f9af3e719ec904b3543
#EXTINF:-1 tvg-logo="https://i.ibb.co/B2Z50vtt/qwest.png",QWEST JAZZ
https://qwestjazz-rakuten.amagi.tv/hls/amagi_hls_data_rakutenAA-qwestjazz-rakuten/CDN/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/M5P1TMG/clubbing.png",CLUBBING TV
https://clubbingtv-rakuten.amagi.tv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/M5P1TMG/clubbing.png",CLUBBING TV
https://d1j2csarxnwazk.cloudfront.net/v1/master/3722c60a815c199d9c0ef36c5b73da68a62b09d1/cc-uze1m6xh4fiyr-ssai-prd/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/2hgmDs6/traceurb.png",TRACE URBAN
https://lightning-traceurban-samsungau.amagi.tv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/2hgmDs6/traceurb.png",TRACE URBAN
https://amg01131-tracetv-traceurbanuk-samsunguk-6r213.amagi.tv/playlist/amg01131-tracetv-traceurbanuk-samsunguk/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/sWxH6cv/tracesports.png",TRACE SPORTS
https://lightning-tracesport-samsungau.amagi.tv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/sWxH6cv/tracesports.png",TRACE SPORTS
https://trace-sportstars-samsungnz.amagi.tv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/p1stMyz/sportenfr.webp",SPORT EN FRANCE
https://sp1564435593.mytvchain.info/live/sp1564435593/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/cXRbJz4/eqps.png",L'ÉQUIPE LIVE 1
https://d3awaj0f2u3w26.cloudfront.net/3/media.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/cXRbJz4/eqps.png",L'ÉQUIPE LIVE 2
https://d2l55nvfkhk4sg.cloudfront.net/3/media.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/KXhYwm0/lequipe.png",L'ÉQUIPE TV
https://raw.githubusercontent.com/ipstreet312/freeiptv/master/ressources/dmotion/py/eqpe/ekip.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/KXhYwm0/lequipe.png",L'ÉQUIPE TV
https://raw.githubusercontent.com/Paradise-91/ParaTV/main/streams/lequipe/la-chaine-l-equipe-en-direct-dm.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/cXRbJz4/eqps.png",L'ÉQUIPE LIVE 3 EVENTS
https://raw.githubusercontent.com/schumijo/iptv/refs/heads/main/playlists/lequipe/lequipelive3.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/cXRbJz4/eqps.png",L'ÉQUIPE LIVE 4 EVENTS
https://raw.githubusercontent.com/schumijo/iptv/refs/heads/main/playlists/lequipe/lequipelive4.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/cXRbJz4/eqps.png",L'ÉQUIPE LIVE FOOT
https://raw.githubusercontent.com/Paradise-91/ParaTV/main/streams/lequipe/l-equipe-live-foot-dm.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/cXRbJz4/eqps.png",L'ÉQUIPE LIVE FOOT
https://raw.githubusercontent.com/schumijo/iptv/refs/heads/main/playlists/lequipe/lequipelive5.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/gTxbf2C/rmcts.jpg",RMC TALK SPORT
https://d21wdmv2hqydbt.cloudfront.net/v1/master/3722c60a815c199d9c0ef36c5b73da68a62b09d1/cc-n239v7ne7hack/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/p0CLPqT/equidia.png" user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0" referer="https://www.equidia.fr/",ÉQUIDIA
https://raw.githubusercontent.com/ipstreet312/freeiptv/master/ressources/extr/py/equidi.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/p0CLPqT/equidia.png" user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0" referer="https://www.equidia.fr/",ÉQUIDIA
https://raw.githubusercontent.com/schumijo/iptv/main/playlists/equidia/equidia-live.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/p0CLPqT/equidia.png" user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64)" referer="https://www.equidia.fr/",ÉQUIDIA RACING GALOP
https://raw.githubusercontent.com/Paradise-91/ParaTV/main/streams/equidia/racinggalop.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/p0CLPqT/equidia.png" user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64)" referer="https://www.equidia.fr/",ÉQUIDIA RACING MAG
https://raw.githubusercontent.com/Paradise-91/ParaTV/main/streams/equidia/racingmag.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/p0CLPqT/equidia.png" user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64)" referer="https://www.equidia.fr/",ÉQUIDIA RACING TROT
https://raw.githubusercontent.com/Paradise-91/ParaTV/main/streams/equidia/racingtrot.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/p0CLPqT/equidia.png" user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64)" referer="https://www.equidia.fr/",ÉQUIDIA RACING 1
https://raw.githubusercontent.com/Paradise-91/ParaTV/main/streams/equidia/racing1.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/p0CLPqT/equidia.png" user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64)" referer="https://www.equidia.fr/",ÉQUIDIA RÉGION 1
https://raw.githubusercontent.com/Paradise-91/ParaTV/main/streams/equidia/region01.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Xt5YPJY/jdgolf.png",JOURNAL DU GOLF
https://raw.githubusercontent.com/schumijo/iptv/main/playlists/jdg-tv/jdg-tv.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/yPsXSFf/esprsorc.png",L'ÉSPRIT SORCIER TV
https://194270.global.ssl.fastly.net/63b43410861d94a9eee067fb/live_947330308dd911edb85c8181cb9b11a8/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/yPsXSFf/esprsorc.png" referer="https://player.castr.com/",L'ÉSPRIT SORCIER TV
https://stream.castr.com/63b43410861d94a9eee067fb/live_947330308dd911edb85c8181cb9b11a8/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/HnSphLp/sqool.jpg",SQOOL TV
https://new.cache-stream.workers.dev/stream/UCaEqMbRYYOmI3WrALMhxuIg/live.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/HnSphLp/sqool.jpg",SQOOL TV
https://ythls.armelin.one/channel/UCaEqMbRYYOmI3WrALMhxuIg.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/LQXjFc3/gulli.png",GULLI
https://origin-caf900c010ea8046.live.6cloud.fr/out/v1/c65696b42ca34e97a9b5f54758d6dd50/cmaf/hlsfmp4_short_q2hyb21h_gulli_sd_index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/LQXjFc3/gulli.png",GULLI
https://lbcdn.6cloud.fr/resource/m6web/l/gulli_hls_sd_short_q2hyb21h.m3u8?groups[]=m6web-live-gulli_ext
#EXTINF:-1 tvg-logo="https://i.ibb.co/MMpFXQL/gong.jpg",GONG
https://cdn-uw2-prod.tsv2.amagi.tv/linear/amg01596-gongnetworks-gong-samsungfr/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/MMpFXQL/gong.jpg",GONG
https://amg01596-gongnetworks-gong-samsungfr-2q4y3.amagi.tv/playlist/amg01596-gongnetworks-gong-samsungfr/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/m4qxfcH/supertoons.jpg",SUPERTOONS FR
https://jmp2.uk/sam-FRBD5100002NL.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/92Q9cRS/plutokids.jpg",PLUTO KIDS
https://jmp2.uk/sam-FRAJ38000035M.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/brFBnw8/vevopop.png",VEVO POP
https://d3vxz540ozij3t.cloudfront.net/v1/master/3722c60a815c199d9c0ef36c5b73da68a62b09d1/cc-lv1qzgyv0ee39/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/WFQ0NCF/vevohprb.png",VEVO HP RB
https://d3mzlmrngyf08j.cloudfront.net/v1/master/3722c60a815c199d9c0ef36c5b73da68a62b09d1/cc-55k4m9whplndi/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/3CtD77v/vevo90.png",VEVO 90 00
https://d2q982f39qtdzh.cloudfront.net/v1/master/3722c60a815c199d9c0ef36c5b73da68a62b09d1/cc-np9jnkbfjxrog/Vevo90and2000_FR.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/kDmhscZ/mgg.png",MGG E-SPORT
https://d1mdvi698umja9.cloudfront.net/v1/master/3722c60a815c199d9c0ef36c5b73da68a62b09d1/cc-kuib43fy5umqi-ssai-prd/mgg.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/hFf6hc4T/fifaplus.jpg",FIFA+ FR
https://37b4c228.wurl.com/master/f36d25e7e52f1ba8d7e56eb859c636563214f541/UmFrdXRlblRWLWZyX0ZJRkFQbHVzRnJlbmNoX0hMUw/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Xs1PxZs/driveauto.png",DRIVE AUTO
https://amg01796-amg01796c2-rakuten-uk-3887.playouts.now.amagi.tv/playlist/amg01796-fastmediafast-drivetv-rakutenuk/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/0YKFn02/motorvisionfrs.png",MOTORSPORT FR
https://9e2ee5d5.wurl.com/master/f36d25e7e52f1ba8d7e56eb859c636563214f541/UmFrdXRlblRWLWV1X01vdG9yc3BvcnR0dl9ITFM/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/0YKFn02/motorvisionfrs.png",MOTORVISION FR
https://d1qswsont218xa.cloudfront.net/v1/master/3722c60a815c199d9c0ef36c5b73da68a62b09d1/cc-im2kwho8ev6jk/mv_fr.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/0sdMx5Z/mtrvsn.png",MOTORVISION TV
https://d39g1vxj2ef6in.cloudfront.net/v1/master/3fec3e5cac39a52b2132f9c66c83dae043dc17d4/prod-rakuten-stitched/master.m3u8?ads.xumo_channelId=88883047
#EXTINF:-1 tvg-logo="https://i.ibb.co/0sdMx5Z/mtrvsn.png",MOTORVISION TV-2
http://stitcher-ipv4.pluto.tv/v1/stitch/embed/hls/channel/60817e1aa6997500072d0d6d/master.m3u8?deviceDNT=%7BTARGETOPT%7D&deviceModel=samsung&deviceVersion=unknown&appVersion=unknown&deviceType=samsung-tvplus&deviceMake=samsung
#EXTINF:-1 tvg-logo="https://i.ibb.co/443jKxq/techco.png",TECH&CO
https://live-cdn-technco-euw1.bfmb.bct.nextradiotv.com/m1/media.m3u8?bpkio_serviceid=7de32147a4f1055bd2f1574d94862544
#EXTINF:-1 tvg-logo="https://i.ibb.co/443jKxq/techco.png",TECH&CO
https://ncdn-live-bfm.pfd.sfr.net/shls/LIVE$BFM_TECHANDCO/index.m3u8?start=LIVE&end=END
#EXTINF:-1 tvg-logo="https://i.ibb.co/443jKxq/techco.png",TECH&CO
https://d2py8vfwz3u72y.cloudfront.net/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tcYgz6h/mensup.png",MEN'S UP TV
https://raw.githubusercontent.com/ipstreet312/freeiptv/master/ressources/dmotion/py/dmdirect/mensup.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tcYgz6h/mensup.png",MEN'S UP TV
https://tvradiozap.eu/tools/dm-m3u8.php/x2kr3hs.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/TLPBT2L/topsante.png",TOP SANTÉ
https://d3tuo4zu8l334y.cloudfront.net/v1/manifest/3722c60a815c199d9c0ef36c5b73da68a62b09d1/cc-x8ri0qojo9mfh/e5997ac8-9e9c-42cc-a2ef-633dc0a4f5a3/2.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/TLPBT2L/topsante.png",TOP SANTÉ
https://tvradiozap.eu/tools/dm-m3u8.php/720/x89yjnn.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/d66k2fw/maisontrvx.png",MAISON & TRAVAUX
https://d387lnkgycbwl.cloudfront.net/v1/manifest/3722c60a815c199d9c0ef36c5b73da68a62b09d1/cc-sdi2aweg8u1y4/761cde02-1df4-4a1a-ad50-7033ede188ef/2.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/d66k2fw/maisontrvx.png",MAISON & TRAVAUX
https://d387lnkgycbwl.cloudfront.net/v1/master/3722c60a815c199d9c0ef36c5b73da68a62b09d1/cc-sdi2aweg8u1y4/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/HzXTSvk/naturetime.jpg",NATURE TIME
https://amg00090-blueantmedia-naturetime-samsungfr-yakbf.amagi.tv/playlist/amg00090-blueantmedia-naturetime-samsungfr/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/HzXTSvk/naturetime.jpg",NATURE TIME
https://bamusa-naturetime-emea-fra-rakuten.amagi.tv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tYqGGQp/travelxp.jpg",TRAVEL XP
https://0b0a5371d15f48128cf69b029230eac6.mediatailor.us-east-1.amazonaws.com/v1/master/04fd913bb278d8775298c26fdca9d9841f37601f/Samsung-fr_TravelXP/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/vxqS6F0/tv5voyage.png",TV5MONDE VOYAGE
https://d1qvkge2x4ev90.cloudfront.net/v1/master/3722c60a815c199d9c0ef36c5b73da68a62b09d1/cc-8q6p9i1t9dw2k/tvfvo.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/vxqS6F0/tv5voyage.png",TV5MONDE VOYAGE
https://stream.ads.ottera.tv/playlist.m3u8?network_id=11074
#EXTINF:-1 tvg-logo="https://i.ibb.co/2F8Cqdn/voyagessaveurs.png",VOYAGES ET SAVEURS
https://amg01821-amg01821c24-samsung-fr-5157.playouts.now.amagi.tv/playlist/amg01821-lovetvfast-voyagesandsaveurs-samsungfr/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/JRX9cpG/voyagesplus.jpg",VOYAGES+
https://streams2.sofast.tv/ptnr-limex/title-VOYAGES-FRE_LIMEX/v1/master/611d79b11b77e2f571934fd80ca1413453772ac7/c30aa0d0-fb77-4f9b-8acf-b156ab5b969b/manifest.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/vH6Q8Qx/plutocuisine.jpg",PLUTO CUISINE
https://jmp2.uk/sam-FRBA3300044VR.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/d6JJHZR/rmcwow.jpg",RMC WOW
https://d18uxd7zigjv4y.cloudfront.net/v1/master/3722c60a815c199d9c0ef36c5b73da68a62b09d1/cc-hynzl7bz38ht6/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/VpvbTn4/rmcmyst.jpg",RMC MYSTÈRE
https://d3w0weunrynif9.cloudfront.net/v1/master/3722c60a815c199d9c0ef36c5b73da68a62b09d1/cc-30cqeaahzofvb/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/c3ZRH8G/rmcmeca.jpg",RMC MECANIC
https://d3bb0xy15a32jc.cloudfront.net/v1/master/3722c60a815c199d9c0ef36c5b73da68a62b09d1/cc-3gcgvdj5b4sla/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tpy1mKV/rmcalertes.jpg",RMC ALERTE SECOURS
https://ddt6vdovkiskj.cloudfront.net/v1/master/3722c60a815c199d9c0ef36c5b73da68a62b09d1/cc-jompzy8pen6vl/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/2SHJGsj/allocine.png",ALLO CINÉ
https://d1yl6bf4hrzbr0.cloudfront.net/v1/master/3722c60a815c199d9c0ef36c5b73da68a62b09d1/cc-5km3zs4zs9sp0/allo.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/2SHJGsj/allocine.png",ALLO CINÉ
https://stream.ads.ottera.tv/playlist.m3u8?network_id=10840
#EXTINF:-1 tvg-logo="https://i.ibb.co/3v8W06Q/rakutenfilms.png",RAKUTEN TOP FILMS TV
https://01ac9352fbfa4204998783d41f9b1a2e.mediatailor.eu-west-1.amazonaws.com/v1/master/0547f18649bd788bec7b67b746e47670f558b6b2/production-LiveChannel-6068/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/yhRGCbH/Brefcin.png",BREF CINÉ
https://c3776ebb1c7742cb9c0191b41b8b2432.mediatailor.us-east-1.amazonaws.com/v1/master/04fd913bb278d8775298c26fdca9d9841f37601f/Samsung-fr_Brefcinema/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Hpqbt3q/cineprime.png",CINÉ PRIME
https://d1epkvgkeqefgi.cloudfront.net/v1/manifest/3722c60a815c199d9c0ef36c5b73da68a62b09d1/cc-myfiyxckorqab/257aeb10-abc9-4b30-952c-2c6775eb768d/2.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/xqMPP7j/famclub.png",FAMILY CLUB
https://d3kwy5wwq7dpr1.cloudfront.net/v1/master/3722c60a815c199d9c0ef36c5b73da68a62b09d1/cc-5ty5rugo8lr9f/famcl.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/M9XhS35/filmsfr.jpg",FILMS FRANÇAIS
https://rakuten-films-francais-1-eu.rakuten.wurl.tv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/VvMKr5V/wildside.jpg",WILD SIDE TV
https://versatile-wildsidetv-1-fr.samsung.wurl.tv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/grBSqt4/novela.png",TELE NOVELA TV
https://stormcast-telenovelatv-1-fr.samsung.wurl.tv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/JB18vMW/bblack.png",BBLACK! AFRICA
https://livevideo.vedge.infomaniak.com/livecast/ik:bblackafrica/manifest.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/JB18vMW/bblack.png",BBLACK! CARIBBEAN
https://livevideo.vedge.infomaniak.com/livecast/ik:bblackcaribbean/manifest.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/JB18vMW/bblack.png",BBLACK! CLASSIK
https://livevideo.vedge.infomaniak.com/livecast/ik:bblackclassik/manifest.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/VvMKr5V/wildside.jpg",WILD SIDE TV
https://versatile-wildsidetv-1-fr.samsung.wurl.tv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/f1FyTkt/universcine.jpg",UNIVERS CINÉ
https://samsunguk-universcine-samsung-fre-xxgab.amagi.tv/playlist/samsunguk-universcine-samsung-fre/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/px6TJjx/plutocine.jpg",PLUTO CINÉ
https://jmp2.uk/sam-FRAJ3800002W5.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/h1M7Xrt/plutopolar.jpg",PLUTO POLAR
https://jmp2.uk/sam-FRAJ38000089S.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/02pwsTj/cinenanar.png",CINÉ NANAR
https://d2o63bkh2qz410.cloudfront.net/v1/manifest/3722c60a815c199d9c0ef36c5b73da68a62b09d1/CineNanar-FR-prod/64953490-a5a5-4f44-a4fb-7bf3638dd24c/2.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/QbDCvVf/cinewestern.png",CINÉ WESTERN
https://d1rmn2456fdhrx.cloudfront.net/v1/manifest/3722c60a815c199d9c0ef36c5b73da68a62b09d1/cc-cj5v6orcb1e6m/e6540a94-93a6-4b38-bb2d-eafe9fa047e2/2.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/883phd1/ktook.png",KTO
https://live-kto.akamaized.net/hls/live/2033284/KTO/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/xJyNqdg/dieutv.png",DIEU TV
https://cdn.katapy.io/cache/stream/katapytv/dieu/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/KhXn6GB/evevangile.png" user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0" referer="https://evangile.tv/",EV TV ÉVANGILE
https://raw.githubusercontent.com/ipstreet312/freeiptv/master/ressources/extr/py/evtv.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/0FM2MbV/emci.png",EMCI TV
https://raw.githubusercontent.com/ipstreet312/freeiptv/master/ressources/dmotion/py/dmdirect/emcieu.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/LgSzMCy/museum.webp",MUSEUM
https://live2.creacast.com/museum-france/smil:museum-france.smil/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/LgSzMCy/museum.webp",MUSEUM
https://amg01492-secomsasmediart-museumtv-fr-rakuten-5ofja.amagi.tv/hls/amagi_hls_data_rakutenAA-museumtv-fr-rakuten/CDN/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/LgSzMCy/museum.webp",MUSEUM
https://cdn-ue1-prod.tsv2.amagi.tv/linear/amg01492-secomsasmediart-museumtven-xiaomi/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/VvRpRty/myzen.png",MY ZEN
https://cdn-ue1-prod.tsv2.amagi.tv/linear/amg01255-secomcofites-my-myzen-en-plex/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/VvRpRty/myzen.png",MY ZEN
https://amg01255-secomcofites-my-myzen-samsungfr-samsungfr-36vwz.amagi.tv/playlist/amg01255-secomcofites-my-myzen-samsungfr-samsungfr/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/VvRpRty/myzen.png",MY ZEN
https://live.creacast.com/myzentv-france/myzentv-france.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/VvRpRty/myzen.png",MY ZEN WELLBEING
https://amg01492-secomsasmediart-myzen-fr-rakuten-spvgz.amagi.tv/hls/amagi_hls_data_rakutenAA-myzen-fr-rakuten/CDN/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/LYbF1Wt/fashionok.png",FASHION TV
https://fashiontv-fashiontv-1-eu.rakuten.wurl.tv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/LYbF1Wt/fashionok.png",FASHION TV
https://fash1043.cloudycdn.services/slive/ftv_paris_adaptive.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/LYbF1Wt/fashionok.png",FASHION TV
https://34963c1506c8467bb8132d8a9ae4fedc.mediatailor.us-east-1.amazonaws.com/v1/master/44f73ba4d03e9607dcd9bebdcb8494d86964f1d8/Samsung-fr_FashionTV/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/LYbF1Wt/fashionok.png",FASHION TV
https://cdn-ue1-prod.tsv2.amagi.tv/linear/amg01546-ftv-fashiontv-xiaomi/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/LYbF1Wt/fashionok.png",FASHION TV
https://fashiontv-fashiontv-loriginal-fr.samsung.wurl.tv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/LYbF1Wt/fashionok.png",FASHION TV
https://stream-us-east-1.getpublica.com/playlist.m3u8?network_id=5457
#EXTINF:-1 tvg-logo="https://i.ibb.co/LYbF1Wt/fashionok.png",FASHION TV
https://fashiontv-fashiontv-5-nl.samsung.wurl.tv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/LYbF1Wt/fashionok.png",FASHION TV
https://68f1accef2154d2195cae87dec183843.mediatailor.us-east-1.amazonaws.com/v1/master/44f73ba4d03e9607dcd9bebdcb8494d86964f1d8/RakutenTV-eu_FashionTV/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/2hgmDs6/traceurb.png",TRACE URBAN (backup)
https://cdn-apse1-prod.tsv2.amagi.tv/linear/amg01076-lightningintern-traceurban-samsungnz/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/2hgmDs6/traceurb.png",TRACE URBAN (backup)
https://d35j504z0x2vu2.cloudfront.net/v1/master/0bc8e8376bd8417a1b6761138aa41c26c7309312/trace-urban/encrypted.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/2hgmDs6/traceurb.png",TRACE URBAN (backup)
https://amg01131-tracetv-amg01131c1-rakuten-us-1081.playouts.now.amagi.tv/playlist/amg01131-tracetvfast-traceurban-rakutenus/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/WPbxmgn/tv5style.png",TV5MONDE STYLE [geo-area]
https://ott.tv5monde.com/Content/HLS/Live/channel(style1)/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Jpk0d48/tv5tivi.png",TV5MONDE TiVi [geo-area]
https://ott.tv5monde.com/Content/HLS/Live/channel(tivi5)/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/LQXjFc3/gulli.png",GULLI (backup)
https://raw.githubusercontent.com/ipstreet312/freeiptv/master/ressources/rtlm6/directmaster/gullisd.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/ByN83p3/funradtv.png",FUN RADIO TV BE [died-link]
https://livevideo.infomaniak.com/streaming/livecast/funradiovisionhd/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/ByN83p3/funradtv.png",FUN RADIO TV BE (backup)
https://raw.githubusercontent.com/Sibprod/streams/main/ressources/dm/py/hls/funradiobe.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/ByN83p3/funradtv.png",FUN RADIO TV BE (backup)
https://edge11.vedge.infomaniak.com/livecast/ik:funradiovisionhd/manifest.m3u8


#EXTINF:-1 group-title="4. |FR|🇫🇷 RÉGIONS & LOCALES",--- |FR:🇫🇷 FRANCE MÉTROPOLITAINE| ---
https://section
#EXTINF:-1 tvg-logo="https://i.ibb.co/mzhSFNV/bfmregions.png",BFM ALPES
https://ncdn-live-bfm.pfd.sfr.net/shls/LIVE$BFM_DICI_ALPESDUSUD/index.m3u8?start=LIVE&end=END
#EXTINF:-1 tvg-logo="https://i.ibb.co/mzhSFNV/bfmregions.png",BFM ALSACE
https://ncdn-live-bfm.pfd.sfr.net/shls/LIVE$BFM_ALSACE/index.m3u8?start=LIVE&end=END
#EXTINF:-1 tvg-logo="https://i.ibb.co/mzhSFNV/bfmregions.png",BFM H.PROVENCE
https://ncdn-live-bfm.pfd.sfr.net/shls/LIVE$BFM_DICI_HAUTEPROVENCE/index.m3u8?start=LIVE&end=END
#EXTINF:-1 tvg-logo="https://i.ibb.co/mzhSFNV/bfmregions.png",BFM LILLE
https://ncdn-live-bfm.pfd.sfr.net/shls/LIVE$BFMGRANDLILLE/index.m3u8?start=LIVE&end=END
#EXTINF:-1 tvg-logo="https://i.ibb.co/mzhSFNV/bfmregions.png",BFM LITTORAL
https://ncdn-live-bfm.pfd.sfr.net/shls/LIVE$BFMGRANDLITTORAL/index.m3u8?start=LIVE&end=END
#EXTINF:-1 tvg-logo="https://i.ibb.co/mzhSFNV/bfmregions.png",BFM LYON
https://ncdn-live-bfm.pfd.sfr.net/shls/LIVE$BFM_LYON/index.m3u8?start=LIVE&end=END
#EXTINF:-1 tvg-logo="https://i.ibb.co/mzhSFNV/bfmregions.png",BFM MARSEILLE
https://ncdn-live-bfm.pfd.sfr.net/shls/LIVE$BFM_MARSEILLEPROV/index.m3u8?start=LIVE&end=END
#EXTINF:-1 tvg-logo="https://i.ibb.co/mzhSFNV/bfmregions.png",BFM NICE
https://ncdn-live-bfm.pfd.sfr.net/shls/LIVE$BFM_NICECOTEDAZUR/index.m3u8?start=LIVE&end=END
#EXTINF:-1 tvg-logo="https://i.ibb.co/mzhSFNV/bfmregions.png",BFM NORMANDIE
https://ncdn-live-bfm.pfd.sfr.net/shls/LIVE$BFM_NORMANDIE/index.m3u8?start=LIVE&end=END
#EXTINF:-1 tvg-logo="https://i.ibb.co/mzhSFNV/bfmregions.png",BFM PARIS
https://ncdn-live-bfm.pfd.sfr.net/shls/LIVE$BFM_PARIS/index.m3u8?start=LIVE&end=END
#EXTINF:-1 tvg-logo="https://i.ibb.co/mzhSFNV/bfmregions.png",BFM TOULON
https://ncdn-live-bfm.pfd.sfr.net/shls/LIVE$BFM_TOULONVAR/index.m3u8?start=LIVE&end=END
#EXTINF:-1 tvg-logo="https://i.ibb.co/z8SYHqs/f3ici.png",F3/ICI PARIS IDF
https://raw.githubusercontent.com/ipstreet312/freeiptv/master/ressources/ftv/py/fidf.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/z8SYHqs/f3ici.png",F3/ICI PROVENCE ALPES
https://raw.githubusercontent.com/ipstreet312/freeiptv/master/ressources/ftv/py/fpra.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/z8SYHqs/f3ici.png",F3/ICI CÔTE D'AZUR
https://raw.githubusercontent.com/ipstreet312/freeiptv/master/ressources/ftv/py/fpca.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/z8SYHqs/f3ici.png",F3/ICI RHÔNE ALPES
https://raw.githubusercontent.com/ipstreet312/freeiptv/master/ressources/ftv/py/frha.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/z8SYHqs/f3ici.png",F3/ICI ALPES
https://raw.githubusercontent.com/ipstreet312/freeiptv/master/ressources/ftv/py/falp.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/z8SYHqs/f3ici.png",F3/ICI AUVERGNE
https://raw.githubusercontent.com/ipstreet312/freeiptv/master/ressources/ftv/py/fauv.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/z8SYHqs/f3ici.png",F3/ICI BOURGOGNE
https://raw.githubusercontent.com/ipstreet312/freeiptv/master/ressources/ftv/py/fbog.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/z8SYHqs/f3ici.png",F3/ICI FRANCHE COMPTÉ
https://raw.githubusercontent.com/ipstreet312/freeiptv/master/ressources/ftv/py/ffrc.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/z8SYHqs/f3ici.png",F3/ICI CENTRE
https://raw.githubusercontent.com/ipstreet312/freeiptv/master/ressources/ftv/py/fctr.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/z8SYHqs/f3ici.png",F3/ICI CORSE VÍA STELLA
https://raw.githubusercontent.com/ipstreet312/freeiptv/master/ressources/ftv/py/fcrs.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/z8SYHqs/f3ici.png",F3/ICI ALSACE
https://raw.githubusercontent.com/ipstreet312/freeiptv/master/ressources/ftv/py/fals.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/z8SYHqs/f3ici.png",F3/ICI CHAMPAGNE
https://raw.githubusercontent.com/ipstreet312/freeiptv/master/ressources/ftv/py/fchg.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/z8SYHqs/f3ici.png",F3/ICI LORRAINE
https://raw.githubusercontent.com/ipstreet312/freeiptv/master/ressources/ftv/py/flor.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/z8SYHqs/f3ici.png",F3/ICI NORD PDC
https://raw.githubusercontent.com/ipstreet312/freeiptv/master/ressources/ftv/py/fpdc.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/z8SYHqs/f3ici.png",F3/ICI PICARDIE
https://raw.githubusercontent.com/ipstreet312/freeiptv/master/ressources/ftv/py/fpcd.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/z8SYHqs/f3ici.png",F3/ICI B.NORMANDIE
https://raw.githubusercontent.com/ipstreet312/freeiptv/master/ressources/ftv/py/fbnr.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/z8SYHqs/f3ici.png",F3/ICI H.NORMANDIE
https://raw.githubusercontent.com/ipstreet312/freeiptv/master/ressources/ftv/py/fhnr.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/z8SYHqs/f3ici.png",F3/ICI AQUITAINE
https://raw.githubusercontent.com/ipstreet312/freeiptv/master/ressources/ftv/py/faqt.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/z8SYHqs/f3ici.png",F3/ICI NOA
https://raw.githubusercontent.com/ipstreet312/freeiptv/master/ressources/ftv/py/fnoa.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/z8SYHqs/f3ici.png",F3/ICI LIMOUSIN
https://raw.githubusercontent.com/ipstreet312/freeiptv/master/ressources/ftv/py/flms.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/z8SYHqs/f3ici.png",F3/ICI POITOU CHARENTES
https://raw.githubusercontent.com/ipstreet312/freeiptv/master/ressources/ftv/py/fpch.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/z8SYHqs/f3ici.png",F3/ICI MIDI PYRÉNÉES
https://raw.githubusercontent.com/ipstreet312/freeiptv/master/ressources/ftv/py/fmpr.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/z8SYHqs/f3ici.png",F3/ICI LANGUEDOC
https://raw.githubusercontent.com/ipstreet312/freeiptv/master/ressources/ftv/py/fldr.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/z8SYHqs/f3ici.png",F3/ICI PAYS LOIRE
https://raw.githubusercontent.com/ipstreet312/freeiptv/master/ressources/ftv/py/fpdl.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/z8SYHqs/f3ici.png",F3/ICI BRETAGNE
https://raw.githubusercontent.com/ipstreet312/freeiptv/master/ressources/ftv/py/fbre.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/xmhMMDN/tebeo.png",TÉBÉO TV
https://lives.digiteka.com/stream/e0fe6433-554e-4568-9a7e-31969136d8ff/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/3k4Lv34/tvrennes.png",TVR RENNES
https://streamtv.cdn.dvmr.fr/TVR/ngrp:tvr.stream_all/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/C5mwn8j2/bordotv.png",BORDO TV
https://srv.webtvmanager.fr:3463/stream/play.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/vCB3X1Hm/bordosport.png",BORDO SPORT
https://srv.webtvmanager.fr:3225/stream/play.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/PGX8qp8n/c11media.png",C11 MÉDIA
https://srv.webtvmanager.fr:3508/stream/play.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/3y88kpg/telenantes.jpg",TÉLÉ NANTES
https://raw.githubusercontent.com/azgaresncf/strm2hls/main/streams/Telenantes.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/3y88kpg/telenantes.jpg",TÉLÉ NANTES
https://github.com/Sibprod/streams/raw/main/ressources/dm/py/hls/telenantes.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/xS8B1qS/tvvendee.png",TV VENDÉE
https://streamer01.myvideoplace.tv/streamer02/hls/VDE_EVEN_PAD_130923.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/fdcDJWF/tv78.png",TV 78
https://streamtv.cdn.dvmr.fr/TV78/ngrp:tv78.stream_all/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/WpSPwkN/7alim.png",7A LIMOGES
https://new.cache-stream.workers.dev/stream/UCdFv_ZWQ3Xk_NfRiaK-ryGg/live.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/zRLKgFS/alpehuez.png",ALPE D'HUEZ TV
https://edge14.vedge.infomaniak.com/livecast/ik:adhtv/manifest.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/61mqv2h/biptv.png",BIP TV
https://biptv.tv/live/biptvstream_orig/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Dpsn6ZV/c32.png",CANAL 32
https://edge17.vedge.infomaniak.com/livecast/ik:canal32_4/manifest.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Dpsn6ZV/c32.png",CANAL 32
https://video.vedge.infomaniak.com/livecast/canal32_4/manifest.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/YLL42C6/iltv.png",IL TV
https://live.creacast.com/iltv/smil:iltv.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/vmqkmDB/moselle.jpg",MOSELLE TV
https://live.creacast.com/mirabelletv/smil:mirabelletv.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/9VrjLFT/tv7b.png",TV7 BORDEAUX
https://lives.digiteka.com/stream/17c6dea8-fb3f-46fe-b170-2ac88cd5667b/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/d6x3fxq/tv7colm.png",TV7 COLMAR
http://tv7.hdr-tv.com/live/tv7/livestream/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/2nG96GF/tv3v.png",TV 3V
https://tv3v.live-kd.com/live/tv3v/livestream/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/4ZfHZhf/viamatele.png",VIA MATÉLÉ
https://5dd226f8f01e8.streamlock.net/via-matele-live/matelelive_1080/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/3My0NGd/viaocc.png",VIA OCCITANIE
https://streamer01.myvideoplace.tv/streamer02/hls/MDS_VIA_PAD_301117.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/3My0NGd/viaocc.png",VIA OCCITANIE
https://lives.digiteka.com/stream/9c424a1c-d202-465c-84e1-3efb89a43fee/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/nQP8st8/telepaese.png",VIA TELEPAESE
https://srv.webtvmanager.fr:3970/live/viatelepaeselive.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/qkkHNPR/vosges.png",VOSGES TV
https://vosgestv.live-kd.com/live/vosgestv/vosgestv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/nMkybxK/weo1.png",WÉO NORD PICARDIE
https://live-weo.digiteka.com/1189023466/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/KGNTppx/nancyweb.jpg",NANCY WEB TV
https://edge12.vedge.infomaniak.com/livecast/ik:nancy-webtv/manifest.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/MMDSDQ9/maurienne.png",MAURIENNE TV
https://raw.githubusercontent.com/SebTV-prod/streams/refs/heads/main/ressources/twitch/hls/MaurienneTV.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/dDbcFbF/lch32.png",LA CHAÎNE 32
https://new.cache-stream.workers.dev/stream/UChl0zP89T7yZyEwQkCfmmnQ/live.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/VNDPTDY/tgohelle.png",TÉLÉ GOHELLE
https://videas.agglo-lenslievin.fr/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/6W98gzZ/tvpi.png",TVPI BAYONNE
https://ythls-v3.onrender.com/video/yTOjGPiFseY.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/6W98gzZ/tvpi.png",TVPI BAYONNE
https://new.cache-stream.workers.dev/stream/UCwVQAPo6tjC5w5yBBh0WEdA/live.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/6W98gzZ/tvpi.png",TVPI BAYONNE
https://ythls.armelin.one/channel/UCwVQAPo6tjC5w5yBBh0WEdA.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/1rDLsMp/puisstv.png",PUISSANCE TÉLÉVISION
https://edge13.vedge.infomaniak.com/livecast/ik:puissancetelevision/manifest.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Tr2b0gV/natv.png",NA TV
https://edge11.vedge.infomaniak.com/livecast/ik:naradio/manifest.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/2Zb8Gmb/kdude.png",KANAL DUDE
https://5aa375514fbab.streamlock.net:8090/tbzain/smil:kanaldude.smil/manifest.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/0q3DHhF/cannesler.png",CANNES LÉRINS TV
https://vdo2.pro-fhi.net:3628/live/uppodsfqlive.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tLPxcFn/littoral.png",LITTORAL TV
https://live.creacast.com/littoralfm-ch1/stream/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/QYJL1N7/tarn.png",TV TARN
https://live.creacast.com/albi-tv-ch1/stream/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Jk1ND0P/mosaik.png",MOSAIK CRISTAL TV
https://new.cache-stream.workers.dev/stream/UCQC0xLG_W0QpqAXQ4-yhwBA/live.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/74fJt5v/8mblanc.png",TV8 MONTBLANC
https://raw.githubusercontent.com/azgaresncf/strm2hls/main/streams/8_Mont-Blanc.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/74fJt5v/8mblanc.png",TV8 MONTBLANC
https://tvradiozap.eu/tools/dm-m3u8.php/x3wqv8b.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/vDRB1fK/tvtloire.png",TVT TOURS
https://live-tvtours.digiteka.com/1982825398/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/vDRB1fK/tvtloire.png",TVT TOURS
https://lives.digiteka.com/stream/920f083a-9e61-4c09-9bc2-bdb664063aa9/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/QM2Y7TV/angtl.jpg",ANGERS TÉLÉ
https://github.com/Sibprod/streams/raw/main/ressources/dm/py/hls/angerstele.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/3NX9rPp/lyoncap.png",LYON CAPITALE TV
https://github.com/Sibprod/streams/raw/main/ressources/dm/py/hls/lyoncapitale.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/h2VX7Wj/tlcholt.png",TL CHOLETAIS
https://github.com/Sibprod/streams/raw/main/ressources/twitch/hls/TLC.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/S0X9VM8/brion.jpg",BRIONNAIS TV
https://stream2.mandarine.media/brionnaistv/brionnaistv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/S0X9VM8/brion.jpg",BRIONNAIS TV
https://stream2.mandarine.media/brionnais_tv/brionnais_tv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/c2MfMVN/valloire.jpg",VALLOIRE TV 
https://github.com/Sibprod/streams/raw/main/ressources/twitch/hls/ValloireTV.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/gj4ZGdY/n31.jpg",N31
https://github.com/Sibprod/streams/raw/main/ressources/dm/py/hls/n31.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/c2CBDqt/grenoble.png",TÉLÉ GRENOBLE
https://github.com/Sibprod/streams/raw/main/ressources/twitch/hls/Telegrenoble.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/nccDkr5/lmtv.png",LM TV SARTHE
https://github.com/Sibprod/streams/raw/main/ressources/twitch/hls/LMTVSarthe.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/2qs2HxR/astv.png",ASTV
https://raw.githubusercontent.com/SebTV-prod/streams/refs/heads/main/ressources/twitch/hls/ASTV.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/yRLR4Ny/tl7l.png",TL7 LOIRE
https://raw.githubusercontent.com/SebTV-prod/streams/refs/heads/main/ressources/twitch/hls/TL7.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/C99d8Z7/maritima.jpg",MARITIMA TV
https://indisponible
#EXTINF:-1 tvg-logo="https://i.ibb.co/1RVPRkx/bocal.png",TÉLÉ BOCAL
https://indisponible
#EXTINF:-1 group-title="4. |FR|🇫🇷 RÉGIONS & LOCALES",--- |FR:🇫🇷 OUTRE-MER DOM/TOM| ---
https://section
#EXTINF:-1 tvg-logo="https://i.ibb.co/3pbTbdG/ubizom.jpg",UBIZNEWS OM5TV
https://tvradiozap.eu/tools/dm-m3u8.php/x8dicii.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/3pbTbdG/ubizom.jpg",UBIZNEWS OM5TV
https://github.com/Sibprod/streams/raw/main/ressources/dm/py/hls/ubiznews.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/BwD72ps/madras.png",MADRAS FM TV
https://edge17.vedge.infomaniak.com/livecast/ik:madrasfmtv/manifest.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/PxqLyjh/antreu.png",ANTENNE RÉUNION
https://raw.githubusercontent.com/ipstreet312/freeiptv/master/ressources/infos/barkers/antreu.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/PxqLyjh/antreu.png",ANTENNE RÉUNION
https://live-antenne-reunion.zeop.tv/live/c3eds/antreunihd/hls_fta/antreunihd.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/CPZ00LY/labrise.jpg",LA BRISE HAÏTI
http://lakay.online/public/telelabrise/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/kcPbyTD/tntv.png",TNTV
https://tntv-samsung-fr.amagi.tv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/CB78JpG/etvgp.png",ETV GUADELOUPE
https://edge15.vedge.infomaniak.com/livecast/ik:etvgp/manifest.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Psz0Q4Zm/fusiontv.jpg",FUSION TV
https://edge21.vedge.infomaniak.com/livecast/fusiontv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/GkjLyFv/la1ereom.png",LA 1ÈRE MARTINIQUE [geo-area]
https://raw.githubusercontent.com/ipstreet312/freeiptv/master/ressources/ftv/py/fr1mar.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/GkjLyFv/la1ereom.png",LA 1ÈRE GUADELOUPE [geo-area]
https://raw.githubusercontent.com/ipstreet312/freeiptv/master/ressources/ftv/py/fr1gua.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/GkjLyFv/la1ereom.png",LA 1ÈRE GUYANE [geo-area]
https://raw.githubusercontent.com/ipstreet312/freeiptv/master/ressources/ftv/py/fr1guy.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/GkjLyFv/la1ereom.png",LA 1ÈRE MAYOTTE [geo-area]
https://raw.githubusercontent.com/ipstreet312/freeiptv/master/ressources/ftv/py/fr1may.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/GkjLyFv/la1ereom.png",LA 1ÈRE RÉUNION [geo-area]
https://raw.githubusercontent.com/ipstreet312/freeiptv/master/ressources/ftv/py/fr1reu.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/GkjLyFv/la1ereom.png",LA 1ÈRE N.CALÉDONIE [geo-area]
https://raw.githubusercontent.com/ipstreet312/freeiptv/master/ressources/ftv/py/fr1nc.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/GkjLyFv/la1ereom.png",LA 1ÈRE POLYNÉSIE [geo-area]
https://raw.githubusercontent.com/ipstreet312/freeiptv/master/ressources/ftv/py/fr1pol.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/GkjLyFv/la1ereom.png",LA 1ÈRE WALLIS FUTUNA [geo-area]
https://raw.githubusercontent.com/ipstreet312/freeiptv/master/ressources/ftv/py/fr1wf.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/GkjLyFv/la1ereom.png",LA 1ÈRE SAINT-PIERRE MIQUELON [geo-area]
https://raw.githubusercontent.com/ipstreet312/freeiptv/master/ressources/ftv/py/fr1spm.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/GkjLyFv/la1ereom.png",LA 1ÈRE MARTINIQUE (news only)
https://raw.githubusercontent.com/ipstreet312/freeiptv/master/ressources/ftv/py/fr1marm.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/GkjLyFv/la1ereom.png",LA 1ÈRE GUADELOUPE (news only)
https://raw.githubusercontent.com/ipstreet312/freeiptv/master/ressources/ftv/py/fr1guam.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/GkjLyFv/la1ereom.png",LA 1ÈRE GUYANE (news only)
https://raw.githubusercontent.com/ipstreet312/freeiptv/master/ressources/ftv/py/fr1guym.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/GkjLyFv/la1ereom.png",LA 1ÈRE MAYOTTE (news only)
https://raw.githubusercontent.com/ipstreet312/freeiptv/master/ressources/ftv/py/fr1maym.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/GkjLyFv/la1ereom.png",LA 1ÈRE RÉUNION (news only)
https://raw.githubusercontent.com/ipstreet312/freeiptv/master/ressources/ftv/py/fr1reum.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/GkjLyFv/la1ereom.png",LA 1ÈRE N.CALÉDONIE (news only)
https://raw.githubusercontent.com/ipstreet312/freeiptv/master/ressources/ftv/py/fr1ncm.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/GkjLyFv/la1ereom.png",LA 1ÈRE POLYNÉSIE (news only)
https://raw.githubusercontent.com/ipstreet312/freeiptv/master/ressources/ftv/py/fr1polm.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/GkjLyFv/la1ereom.png",LA 1ÈRE WALLIS FUTUNA (news only)
https://raw.githubusercontent.com/ipstreet312/freeiptv/master/ressources/ftv/py/fr1wfm.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/GkjLyFv/la1ereom.png",LA 1ÈRE SAINT-PIERRE MIQUELON (news only)
https://raw.githubusercontent.com/ipstreet312/freeiptv/master/ressources/ftv/py/fr1spmm.m3u8
#EXTINF:-1 group-title="4. |FR|🇫🇷 RÉGIONS & LOCALES",--- |MC:🇲🇨 MONACO PRINCIPAUTÉ| ---
https://section
#EXTINF:-1 tvg-logo="https://i.ibb.co/XjzvmqL/tvmonaco.jpg",TV MONACO
https://production-fast-mcrtv.content.okast.tv/channels/2116dc08-1959-465d-857f-3619daefb66b/b702b2b9-aebd-436c-be69-2118f56f3d86/master.m3u8
#EXTINF:-1 group-title="4. |FR|🇫🇷 RÉGIONS & LOCALES",--- |BE:🇧🇪 BELGIQUE WALLONIE| ---
https://section
#EXTINF:-1 tvg-logo="https://i.ibb.co/NyHqX5R/belrtl.png",BEL RTL
https://bel-live-hls.akamaized.net/hls/live/2038650/BEL-Live-HLS/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/WGHbhfh/latelebe.png",LA TÉLÉ
https://latele2.vedge.infomaniak.com/livecast/latele2/manifest.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/WGHbhfh/latelebe.png",LA TÉLÉ
https://edge14.vedge.infomaniak.com/livecast/latele2/manifest.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/RCY8bJZ/notele.png",NO TÉLÉ
https://streaming01.divercom.be/notele_live/_definst_/direct.stream/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/4dTPMzK/tlbrux.png",TÉLÉ BRUXELLES
https://59959724487e3.streamlock.net/stream/live/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/cbbQ0hK/vedia.png",VEDIA
https://tvlocales-live.freecaster.com/95d2f480-3c9f-48ba-ba4e-af64b58431ef/95d2f480-3c9f-48ba-ba4e-af64b58431ef.isml/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/4YZfGGL/rtcliege.png",RTC TÉLÉ LIÈGE
https://tvlocales-live.freecaster.com/95d2f6eb-6f01-4d1d-8543-d14966de7b04/95d2f6eb-6f01-4d1d-8543-d14966de7b04.isml/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/ZphSkW0n/qu4trebe.jpg",QUATRE LIÈGE
https://tvlocales-live.freecaster.com/95d2f6eb-6f01-4d1d-8543-d14966de7b04/95d2f6eb-6f01-4d1d-8543-d14966de7b04.isml/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/5TyhqWc/telemb.jpg",TÉLÉ MB
https://tvlocales-live.freecaster.com/95d2f6c9-e85f-4388-8e9c-596260a4206f/95d2f6c9-e85f-4388-8e9c-596260a4206f.isml/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/y0jz90j/bouke.jpg",BOUKÈ
https://tvlocales-live.freecaster.com/95d2f70d-9229-478b-9aed-bc4fa220316d/95d2f70d-9229-478b-9aed-bc4fa220316d.isml/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/2F48hsL/actv.png",ANTENNE CENTRE
https://tvlocales-live.freecaster.com/95d2f733-1bc2-4bd5-9b96-c53ed3fc450f/95d2f733-1bc2-4bd5-9b96-c53ed3fc450f.isml/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/0VSd8bM/zoombe.png",CANAL ZOOM
https://tvlocales-live.freecaster.com/95d2e3af-5ab8-45a9-9dc9-f544d006b5d5/95d2e3af-5ab8-45a9-9dc9-f544d006b5d5.isml/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/8gczbQk/sambre.png",SAMBRE CHARLEROI
https://tvlocales-live.freecaster.com/95d2f67c-de80-486b-9e60-9c72cb2782e2/95d2f67c-de80-486b-9e60-9c72cb2782e2.isml/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/NSZgQQG/Brabant.png",BRABANT WALLON
https://tvlocales-live.freecaster.com/95d2f656-50f1-432b-84a6-ce11c6cdb482/95d2f656-50f1-432b-84a6-ce11c6cdb482.isml/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/MCtzw8h/tvlux.png",TV LUX
https://tvlocales-live.freecaster.com/95d2f631-8941-4efd-b223-0ebd56a033c4/95d2f631-8941-4efd-b223-0ebd56a033c4.isml/master.m3u8
#EXTINF:-1 group-title="4. |FR|🇫🇷 RÉGIONS & LOCALES",--- |CH:🇨🇭 BASSIN SUISSE ROMANDE| ---
https://section
#EXTINF:-1 tvg-logo="https://i.ibb.co/fqq90Z2/noovo.png",NOOVO
https://pe-fa-lp03a.9c9media.com/live/NOOVO/p/hls/00000201/716cf4c845225692/index/de22f34f/live/stream/h264/v1/2048000/manifest.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/CQb8zFT/lemanbleu.jpg",LÉMAN BLEU
https://livevideo.vedge.infomaniak.com/livecast/naxoo/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Y8QFgbN/carac.png",CARAC 1
https://rougetv.vedge.infomaniak.com/livecast/rougetv/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Y8QFgbN/carac.png",CARAC 1
http://event.vedge.infomaniak.com/livecast/event/manifest.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Y8QFgbN/carac.png",CARAC 2
https://onefmhd.vedge.infomaniak.com/livecast/onefmhd/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Y8QFgbN/carac.png",CARAC 3
https://lfmhd.vedge.infomaniak.com/livecast/lfmhd/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Y8QFgbN/carac.png",CARAC 4
https://compack_media_1.vedge.infomaniak.com/livecast/compack_media_1/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/gz2wbkL/tvm3.png",TVM 3
https://edge11.vedge.infomaniak.com/livecast/ik:tvm3/manifest.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/1XYdy6j/canal9.png",CANAL 9
https://edge12.vedge.infomaniak.com/livecast/ik:livehd/manifest.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/st6cDg1/calpha.png",CANAL ALPHA
https://livevideo.vedge.infomaniak.com/livecast/ik:canalalpha/manifest.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/st6cDg1/calpha.png",CANAL ALPHA
https://canalalphaju.vedge.infomaniak.com/livecast/canalalphaju/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/FzJtxkx/mmediach.png",M LE MÉDIA
https://raw.githubusercontent.com/BG47510/tube/refs/heads/main/mlemedia.m3u8
#EXTINF:-1 group-title="4. |FR|🇫🇷 RÉGIONS & LOCALES",--- |CA-QC:🇨🇦 ZONE CANADA\QUÉBEC| ---
https://section
#EXTINF:-1 tvg-logo="https://i.ibb.co/LzWqD0s/savoirmedia.png",SAVOIR.MÉDIA
https://hls.savoir.media/live/stream.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/hFr5pYb/telequebec.png",TÉLÉ QUÉBEC
https://bcovlive-a.akamaihd.net/575d86160eb143458d51f7ab187a4e68/us-east-1/6101674910001/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/HqLCHkz/cpac.png",CPAC TV
https://d7z3qjdsxbwoq.cloudfront.net/groupa/live/f9809cea-1e07-47cd-a94d-2ddd3e1351db/live.isml/.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/whkNzKNr/iciteleqb.png",ICI QUÉBEC
https://rcavlive.akamaized.net/hls/live/696615/xcancbft/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/whkNzKNr/iciteleqb.png",ICI QUÉBEC
https://rcavlive.akamaized.net/hls/live/664045/cancbvt/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tHBB7zv/icimontreal.png",ICI MONTRÉAL
https://amdici.akamaized.net/hls/live/873426/ICI-Live-Stream/master.m3u8


#EXTINF:-1 tvg-logo="https://i.ibb.co/Bt6frts/trthaber.png" group-title="5. |TR|🇹🇷 HABER",TRT HABER
https://tv-trthaber.medya.trt.com.tr/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/B40rjP3/szc1.png" referer="https://turkcanli.tv",SÖZCÜ TV
https://helga.iptv2022.com/szc_tv/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/B40rjP3/szc1.png",SÖZCÜ TV
http://176.65.146.123:6004/play/a019/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/wdwm0fn/haberturk.png",HABER TÜRK
https://ciner-live.daioncdn.net/haberturktv/haberturktv.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/k58p7P2/hglobal.png",HABER GLOBAL
https://ensonhaber-live.ercdn.net/haberglobal/haberglobal.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/BtYMK4q/halk21a.png",HALK TV
https://halktv-live.daioncdn.net/halktv/halktv.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/bLpTdYZ/tv100.png",TV 100
https://tv100-live.daioncdn.net/tv100/tv100.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/4Mhmggc/tele1.png",TELE 1
https://tele1-live.ercdn.net/tele1/tele1.m3u8
#EXTINF:-1 tvg-logo=" https://i.ibb.co/wrMn5rgQ/mktv.png",MK TV
https://live.artidijitalmedya.com/artidijital_mavikaradeniz/mavikaradeniz/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Ln92Dj2/Ekoltv.png",EKOL TV
https://ekoltv-live.ercdn.net/ekoltv/ekoltv.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tXdf2YF/ulusal22.png",ULUSAL KANAL
https://trn03.tulix.tv/gt-ulusaltv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/9c7MvWX/ntv.png",NTV
http://dygvideo.dygdigital.com/live/hls/ntv4puhu?m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/6m9Pb3t/tv5tr1.png",TV 5
https://tv5-live.ercdn.net/tv5/tv5.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/HXKrJRC/blght22.png",BLOOMBERG HT
https://bloomberght-live.daioncdn.net/bloomberght/bloomberght.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/xS3zLQr/ekoturk.png",EKO TÜRK
http://koprulu2.global.ssl.fastly.net/yt.m3u8/?id=7cItyPb6-p0.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/JqWCczW/cnnturk1.png",CNN TÜRK
http://116.202.238.88/CNNTURK_TR/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/JqWCczW/cnnturk1.png",CNN TÜRK
https://b.fulltvizle.com/cnn/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/jZShqBM/Krt24v2.png",KRT
https://trn03.tulix.tv/gt-krt/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/9s9YKYT/gzt.png",GZT
https://mn-nl.mncdn.com/gzttv/gzttv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/0MHPk8y/benguturk.png",BENGÜ TÜRK
https://tv.ensonhaber.com/benguturk/benguturk.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/vJJzR8G/tgrthab22.png",TGRT HABER
https://tgrthaber-live.daioncdn.net/tgrthaber/tgrthaber.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/1RWhvy4/tvnet.png",TV NET
https://mn-nl.mncdn.com/tvnet/tvnet/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/PhwYjQ7/24tv.png",24
https://turkmedya-live.ercdn.net/tv24/tv24.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/F5FcvbZ/flash4ok.png",FLASH HABER
https://flashhaber-live.ercdn.net/flashhaber/flashhaber.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/ZXts607/ulketv.png",ÜLKE
https://livetv.radyotvonline.net/kanal7live/ulketv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/B4XX5Vx/akittv.png",AKIT TV
http://akittv-live.ercdn.net/akittv/akittv.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/1X8nWHc/ahaber.png",A HABER
https://trkvz-live.ercdn.net/ahaberhd/ahaberhd.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/1X8nWHc/ahaber.png",A HABER
https://b.fulltvizle.com/ahaber/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",LİDER HABER TV
http://nrttn172.kesintisizyayin.com:29010/lidertv/lidertv/sec-f5-v1-a1.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/j9Pmc2qN/thhaber.jpg",TÜRK HABER
https://edge1.socialsmart.tv/turkhaber/bant1/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/b2b6Zn0/businesschtr.jpg",BUSINESS CHANNEL TÜRK
https://new.cache-stream.workers.dev/stream/UCLPc5pYOl2clEkCA82Sfb0Q/live.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/GQdBjZfW/finansturk.png",FİNANS TÜRK
https://yayin30.haber100.com/live/finansturk/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/KwXzY6B/apara.png",A PARA
https://trkvz-live.ercdn.net/aparahd/aparahd.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/kcpSwmK/cnbce.png",CNBC-E
https://uzunmuhalefet.serv00.net/canlitv2.php?id=13406&.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/BN9tk1q/tbmm22.png",TBMM TV
https://meclistv-live.ercdn.net/meclistv/meclistv.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/K6BKFqY/dha.png",DHA (feed 1)
https://603c568fccdf5.streamlock.net/live/dhaweb1/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/K6BKFqY/dha.png",DHA (feed 2)
https://603c568fccdf5.streamlock.net/live2/dhaweb2/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/jLd8Fcb/aa.png",AA (feed)
http://mtulqxgomrllive.mediatriple.net/mtulqxgomrllive/broadcast_59f9c0c785b88.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Bt6frts/trthaber.png",TRT HABER
https://ensonhaber-live.ercdn.net/trthaber/trthaber.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Bt6frts/trthaber.png",TRT HABER (backup)
https://tv.ensonhaber.com/trthaber/trthaber.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/B40rjP3/szc1.png",SÖZCÜ TV (backup)
https://b.fulltvizle.com/sozcu/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/B40rjP3/szc1.png",SÖZCÜ TV (backup)
http://185.234.111.229:8000/play/a00y
#EXTINF:-1 tvg-logo="https://i.ibb.co/B40rjP3/szc1.png",SÖZCÜ TV (backup)
http://13.60.64.58/stream/yt/sozcu.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/B40rjP3/szc1.png",SÖZCÜ TV (backup)
https://trn03.tulix.tv/gt-sozcu-tv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/B40rjP3/szc1.png",SÖZCÜ TV (backup)
http://koprulu2.global.ssl.fastly.net/yt.m3u8/?id=ztmY_cCtUl0.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/wdwm0fn/haberturk.png",HABER TÜRK (backup)
https://tv.ensonhaber.com/haberturk/haberturk.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/wdwm0fn/haberturk.png",HABER TÜRK (backup)
https://ciner.daioncdn.net/haberturktv/haberturktv.m3u8?app=c98ab0b0-50cc-495b-bb37-778e91f5ff5b
#EXTINF:-1 tvg-logo="https://i.ibb.co/wdwm0fn/haberturk.png",HABER TÜRK (backup)
https://haberturk.blutv.com/blutv_haberturk_live/live.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/wdwm0fn/haberturk.png",HABER TÜRK (backup)
https://tv.ensonhaber.com/haberturk/haberturk.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/wdwm0fn/haberturk.png",HABER TÜRK (backup)
https://ensonhaber-live.ercdn.net/haberturk/haberturk.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/k58p7P2/hglobal.png",HABER GLOBAL (backup)
https://tv.ensonhaber.com/haberglobal/haberglobal.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/bLpTdYZ/tv100.png",TV 100 (backup)
https://ensonhaber-live.ercdn.net/tv100/tv100.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/bLpTdYZ/tv100.png",TV 100 (backup)
https://tv100.blutv.com/blutv_tv100_live/live.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/bLpTdYZ/tv100.png",TV 100 (backup)
https://tv100.daioncdn.net/tv100/tv100.m3u8?app=web
#EXTINF:-1 tvg-logo="https://i.ibb.co/bLpTdYZ/tv100.png",TV 100 (backup)
https://tv.ensonhaber.com/tv100/tv100.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/JqWCczW/cnnturk1.png",CNN TÜRK (backup)
http://trn03.tulix.tv/gt-cnn-turk/tracks-v1a1/mono.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/JqWCczW/cnnturk1.png",CNN TÜRK (backup)
https://live.duhnet.tv/S2/HLS_LIVE/cnnturknp/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/JqWCczW/cnnturk1.png",CNN TÜRK (backup)
https://yayin2.canlitv.fun/livetv/cnnturk.stream/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tXdf2YF/ulusal22.png",ULUSAL KANAL (backup)
https://canlitvulusal.xyz/live/ulusalkanal/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tXdf2YF/ulusal22.png",ULUSAL KANAL (backup)
https://internettv.guventechnology.com:19360/ulusaltv/ulusaltv.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/9c7MvWX/ntv.png",NTV (backup)
https://dogus-live.daioncdn.net/ntv/ntv.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/9c7MvWX/ntv.png",NTV (backup)
http://dogus.daioncdn.net/ntv/ntv.m3u8?ce=3&&app=7c4bb802-0c41-409e-8cd2-799984995694
#EXTINF:-1 tvg-logo="https://i.ibb.co/9c7MvWX/ntv.png",NTV (backup)
http://dygvideo.dygdigital.com/live/hls/puhuntvdai?m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/9c7MvWX/ntv.png",NTV (backup)
https://raw.githubusercontent.com/ipstreet312/freeiptv/master/ressources/tur/ntv.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/F5FcvbZ/flash4ok.png",FLASH HABER (backup)
https://b01c02nl.mediatriple.net/videoonlylive/mtyycglqauzjhlive/broadcast_67c053c48829f.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/F5FcvbZ/flash4ok.png",FLASH HABER (backup)
https://flashtv.blutv.com/blutv_flashtv/live.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/F5FcvbZ/flash4ok.png",FLASH HABER (backup)
https://internettv.guventechnology.com:19360/flashhabertv/flashhabertv.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Ln92Dj2/Ekoltv.png",EKOL TV (backup)
https://helga.iptv2022.com/sh/ekol_tv/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/4Mhmggc/tele1.png",TELE 1 (backup)
https://tele1.blutv.com/blutv_tele1_live/live.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/0MHPk8y/benguturk.png",BENGÜ TÜRK (backup)
https://ensonhaber-live.ercdn.net/benguturk/benguturk.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/ZXts607/ulketv.png",ÜLKE (backup)
https://ulketv.blutv.com/blutv_ulketv2/live.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/1X8nWHc/ahaber.png",A HABER (backup)
https://c.fulltvizle.com/ahaber/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/1X8nWHc/ahaber.png",A HABER
https://canlitvulusal.xyz/live/ahaber/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/jZShqBM/Krt24v2.png",KRT (backup)
https://trn03.tulix.tv/gt-krttv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/jZShqBM/Krt24v2.png",KRT (backup)
https://krt.blutv.com/blutv_krt_live/live.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/BtYMK4q/halk21a.png",HALK TV (backup)
https://halktvdvr.blutv.com/blutv_halktv2_dvr/live.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/BtYMK4q/halk21a.png",HALK TV (backup)
https://halktv.daioncdn.net/halktv/halktv.m3u8?app=c86957d3-74a7-44da-9ad2-dc358c769609
#EXTINF:-1 tvg-logo="https://i.ibb.co/PhwYjQ7/24tv.png",24 (backup)
https://tv.ensonhaber.com/tv24/tv24.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/PhwYjQ7/24tv.png",24 (backup)
https://mn-nl.mncdn.com/kanal24/smil:kanal24.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/PhwYjQ7/24tv.png",24 (backup)
https://ensonhaber-live.ercdn.net/tv24/tv24.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/HXKrJRC/blght22.png",BLOOMBERG HT (backup)
https://ciner-live.daioncdn.net/bloomberght/bloomberght.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/HXKrJRC/blght22.png",BLOOMBERG HT (backup)
https://ciner.daioncdn.net/bloomberght/bloomberght.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/HXKrJRC/blght22.png",BLOOMBERG HT (backup)
https://ensonhaber-live.ercdn.net/bloomberght/bloomberght.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/HXKrJRC/blght22.png",BLOOMBERG HT (backup)
https://bloomberght2.blutv.com/blutv_bloomberght2/live.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/HXKrJRC/blght22.png",BLOOMBERG HT (backup)
https://tv.ensonhaber.com/bloomberght/bloomberght.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/kcpSwmK/cnbce.png",CNBC-E (backup)
http://stream.tvcdn.net/ekonomi/cnbc-e.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/vJJzR8G/tgrthab22.png",TGRT HABER (backup)
https://canli.tgrthaber.com/tgrt.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/vJJzR8G/tgrthab22.png",TGRT HABER (backup)
https://b01c02nl.mediatriple.net/videoonlylive/mtsxxkzwwuqtglive/broadcast_5fe4598be8e5d.smil/playlist.m3u8


#EXTINF:-1 tvg-logo="https://i.ibb.co/d6c87Km/trt122.png" group-title="6. |TR|🇹🇷 ULUSAL GENEL",TRT 1
https://tv-trt1.medya.trt.com.tr/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/d6c87Km/trt122.png",TRT 1
https://trt.daioncdn.net/trt-1/master.m3u8?app=web
#EXTINF:-1 tvg-logo="https://i.ibb.co/s9mVqWH/kanald.png",KANAL D
https://demiroren-live.daioncdn.net/kanald/kanald.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/s9mVqWH/kanald.png",KANAL D
https://live.duhnet.tv/S2/HLS_LIVE/kanalddainp/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/DYyDzGV/star22tv.png",STAR
https://dogus-live.daioncdn.net/startv/startv.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/DYyDzGV/star22tv.png",STAR
http://dygvideo.dygdigital.com/live/hls/startv4puhu?m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/BrGNZJ4/showtv.png",SHOW
https://ciner-live.daioncdn.net/showtv/showtv.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/BrGNZJ4/showtv.png",SHOW
https://bloomberght-live.daioncdn.net/showtv/showtv.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/0DpKtzT/nowtvturk.png" tvg-id="Fox.tr",NOW
https://nowtv-live-ad.ercdn.net/nowtv/playlist.m3u8?st=taZpj3W7ALa4ubJIyjIvbw&e=1747142182
#EXTINF:-1 tvg-logo="https://i.ibb.co/0DpKtzT/nowtvturk.png" tvg-id="Fox.tr",NOW
https://nowtv.daioncdn.net/nowtv/nowtv.m3u8?st=taZpj3W7ALa4ubJIyjIvbw&e=1747142182
#EXTINF:-1 tvg-logo="https://i.ibb.co/tXKXNDz/tv8.png",TV8
https://tv8.daioncdn.net/tv8/tv8.m3u8?app=7ddc255a-ef47-4e81-ab14-c0e5f2949788
#EXTINF:-1 tvg-logo="https://i.ibb.co/tXKXNDz/tv8.png",TV8
https://bcovlive-a.akamaihd.net/ccee7091e86040d18e14cd0efef2a51b/eu-central-1/6415845530001/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/n1SCYqN/atv.png",ATV
https://rnttwmjcin.turknet.ercdn.net/lcpmvefbyo/atv/atv_480p.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/n1SCYqN/atv.png",ATV
https://trkvz.daioncdn.net/atv/atv_720p.m3u8?app=web
#EXTINF:-1 tvg-logo="https://i.ibb.co/1s3fHfm/k7tr1.png",KANAL 7
https://kanal7-live.daioncdn.net/kanal7/kanal7.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/1s3fHfm/k7tr1.png",KANAL 7
https://kanal7.daioncdn.net/kanal7/kanal7.m3u8?app=f99587ad-1637-494d-8255-da35b09d17a1
#EXTINF:-1 tvg-logo="https://i.ibb.co/0tc3PYz/beyaz22b.png",BEYAZ TV
https://beyaztv-live.daioncdn.net/beyaztv/beyaztv.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/0tc3PYz/beyaz22b.png",BEYAZ TV
https://beyaztv.daioncdn.net/beyaztv/beyaztv.m3u8?app=fcd5c66b-da9d-44ba-a410-4f34805c397d
#EXTINF:-1 tvg-logo="https://i.ibb.co/d6c87Km/trt122.png",TRT 1 (backup)
https://tv-trt1-esdai.medya.trt.com.tr/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/d6c87Km/trt122.png",TRT 1 (backup)
https://trt.daioncdn.net/trt-1/master.m3u8?app=ed3904e8-737b-4a5e-856a-1b0d7a0a94e2
#EXTINF:-1 tvg-logo="https://i.ibb.co/d6c87Km/trt122.png",TRT 1 (backup)
https://trt.daioncdn.net/trt-1/master.m3u8?app=e435840d-2653-45a3-afef-082d4ea998f3
#EXTINF:-1 tvg-logo="https://i.ibb.co/d6c87Km/trt122.png",TRT 1 (backup)
https://d1u68oyra9spme.cloudfront.net/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/d6c87Km/trt122.png",TRT 1 (backup)
https://ddc75c8a6akqr.cloudfront.net/v1/master/80dbfc318ab6b980679b32095ba497236de6d2f9/TRT-1/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/d6c87Km/trt122.png",TRT 1 (backup)
https://helga.iptv2022.com/sh/trt_1/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/d6c87Km/trt122.png",TRT 1 (backup)
https://c.fulltvizle.com/trt1/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/d6c87Km/trt122.png",TRT 1 (backup)
https://rpn3.bozztv.com/dvrfl05/gin-trt1tv/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/d6c87Km/trt122.png",TRT 1 (backup)
https://yayin2.canlitv.fun/livetv/trt1.stream/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/d6c87Km/trt122.png",TRT 1 (backup)
https://dvrfl05.tulix.tv/gin-trt1eu/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/d6c87Km/trt122.png",TRT 1 (backup)
https://tgn.bozztv.com/dvrfl05/gin-trt1eu/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/s9mVqWH/kanald.png",KANAL D (backup)
https://demiroren.daioncdn.net/kanald/kanald.m3u8?app=da2109ea-5dfe-4107-89ab-23593336ed61
#EXTINF:-1 tvg-logo="https://i.ibb.co/s9mVqWH/kanald.png",KANAL D (backup)
https://trn03.tulix.tv/gt-kanald/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/s9mVqWH/kanald.png",KANAL D (backup)
http://trn09.tulix.tv/gt-kanald/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/DYyDzGV/star22tv.png",STAR (backup)
https://dogus.daioncdn.net/startv/startv.m3u8?app=a20ac41e-bdc3-4aa1-934d-26b484480ac9
#EXTINF:-1 tvg-logo="https://i.ibb.co/DYyDzGV/star22tv.png",STAR (backup)
https://raw.githubusercontent.com/ipstreet312/freeiptv/refs/heads/master/ressources/tur/star.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/DYyDzGV/star22tv.png",STAR (backup)
http://dygvideo.dygdigital.com/live/hls/stardai?m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/DYyDzGV/star22tv.png",STAR (backup)
http://trn03.tulix.tv/gt-star-tv/tracks-v1a1/mono.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/DYyDzGV/star22tv.png",STAR (backup)
https://trn03.tulix.tv/gt-startv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/BrGNZJ4/showtv.png",SHOW (backup)
https://canlitvulusal.xyz/live/showtv/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/BrGNZJ4/showtv.png",SHOW (backup)
http://canli.haber365.com.tr/tr/showtv/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/0DpKtzT/nowtvturk.png" tvg-id="Fox.tr",NOW (backup)
https://uycyyuuzyh.turknet.ercdn.net/nphindgytw/nowtv/nowtv.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/0DpKtzT/nowtvturk.png",NOW (backup)
https://nowtv.blutv.com/blutv_nowtv/live.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/0DpKtzT/nowtvturk.png",NOW (backup)
https://new.cache-stream.workers.dev/stream/UCJe13zu6MyE6Oueac41KAqg/live.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/0DpKtzT/nowtvturk.png",NOW (backup)
https://ythls.armelin.one/channel/UCJe13zu6MyE6Oueac41KAqg.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/0DpKtzT/nowtvturk.png",NOW (backup)
http://hw1.jemtv.com/app/FoxTurkey/chunks.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/0DpKtzT/nowtvturk.png",NOW (backup)
https://bozztv.com/inim03/live1/turkfoxtv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/0DpKtzT/nowtvturk.png",NOW (backup)
https://mnorigin-ank-1.mncdn.com/test/live_720p.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/0DpKtzT/nowtvturk.png",NOW (backup)
https://c.fulltvizle.com/fox/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/n1SCYqN/atv.png",ATV (backup)
https://tgn.bozztv.com/trn03/gt-atv-tv/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/n1SCYqN/atv.png",ATV (backup)
https://trkvz.daioncdn.net/atv/atv.m3u8?app=d5eb593f-39d9-4b01-9cfd-4748e8332cf0
#EXTINF:-1 tvg-logo="https://i.ibb.co/n1SCYqN/atv.png",ATV (backup)
https://ythls-v3.onrender.com/channel/UCUVZ7T_kwkxDOGFcDlFI-hg.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/n1SCYqN/atv.png",ATV (backup)
https://koprulu.global.ssl.fastly.net/ythls?kanal_id=UCUVZ7T_kwkxDOGFcDlFI-hg&m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/n1SCYqN/atv.png",ATV (backup)
https://koprulu.serv00.net/ythls/?kanal_id=UCUVZ7T_kwkxDOGFcDlFI-hg.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/n1SCYqN/atv.png",ATV (backup)
https://livestream.zazerconer.workers.dev/channel/UCUVZ7T_kwkxDOGFcDlFI-hg.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/n1SCYqN/atv.png",ATV (backup)
https://ythlsgo.onrender.com/channel/UCUVZ7T_kwkxDOGFcDlFI-hg.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/n1SCYqN/atv.png",ATV (backup)
https://deathlesstg.serv00.net/Youtube-Live/index.php?id=gIdaTOTzZuw&m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/n1SCYqN/atv.png",ATV (backup)
https://new.cache-stream.workers.dev/stream/UCUVZ7T_kwkxDOGFcDlFI-hg/live.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/n1SCYqN/atv.png",ATV (backup)
https://ythls.armelin.one/channel/UCUVZ7T_kwkxDOGFcDlFI-hg.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/n1SCYqN/atv.png",ATV (backup)
https://trkvz-beta.daioncdn.net/atv/atv.m3u8?app=d1ce2d40-5256-4550-b02e-e73c185a314e
#EXTINF:-1 tvg-logo="https://i.ibb.co/n1SCYqN/atv.png",ATV (backup)
https://yayin2.canlitv.fun/livetv/atv.stream/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/n1SCYqN/atv.png",ATV (backup)
https://c.fulltvizle.com/aytv/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/n1SCYqN/atv.png",ATV (backup)
https://bozztv.com/gin-36bay4/gt-atv-tv3/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/n1SCYqN/atv.png",ATV (backup)
https://rnttwmjcin.turknet.ercdn.net/lcpmvefbyo/atv/atv_480p.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/n1SCYqN/atv.png",ATV (backup)
https://rnttwmjcin.turknet.ercdn.net/lcpmvefbyo/atv/atv_720p.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/n1SCYqN/atv.png",ATV [youtube-src]
https://youtu.be/1KXZDgP9W5E
#EXTINF:-1 tvg-logo="https://i.ibb.co/n1SCYqN/atv.png",ATV [tkn-blocked]
https://trkvz-live.daioncdn.net/atv/atv.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/n1SCYqN/atv.png",ATV [tkn-blocked]
https://trkvz.daioncdn.net/atv/atv.m3u8?app=d1ce2d40-5256-4550-b02e-e73c185a314e
#EXTINF:-1 tvg-logo="https://i.ibb.co/n1SCYqN/atv.png",ATV [tkn-blocked]
https://trkvz-dev.daioncdn.net/atv/atv.m3u8?app=8672c3cb-70f1-4686-9158-cc03a23c6b0f
#EXTINF:-1 tvg-logo="https://i.ibb.co/n1SCYqN/atv.png",ATV [tkn-blocked]
https://trkvz-beta.daioncdn.net/atv/atv.m3u8?app=d1ce2d40-5256-4550-b02e-e73c185a314e
#EXTINF:-1 tvg-logo="https://i.ibb.co/tXKXNDz/tv8.png",TV8 (backup)
https://rkhubpaomb.turknet.ercdn.net/fwjkgpasof/tv8/tv8.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tXKXNDz/tv8.png",TV8 (backup)
https://tv8-live.daioncdn.net/tv8/tv8.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tXKXNDz/tv8.png",TV8 (backup)
http://trn03.tulix.tv/gt-tv8-tv/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tXKXNDz/tv8.png",TV8 (backup)
http://tgn.bozztv.com/trn03/gt-tv8-tv/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tXKXNDz/tv8.png",TV8 (backup)
https://x.canlitvapp.com/kanal8/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/1s3fHfm/k7tr1.png",KANAL 7 (backup)
https://kanal7.blutv.com/blutv_kanal7_live/live.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/0tc3PYz/beyaz22b.png",BEYAZ TV [diedlink]
https://beyaztv.blutv.com/blutv_beyaztv_live/live.m3u8


#EXTINF:-1 tvg-logo="https://i.ibb.co/N1h8m96/trtbelgesel.png" group-title="7. |TR|🇹🇷 BELGESEL & YAŞAM",TRT BELGESEL
https://tv-trtbelgesel-dai.medya.trt.com.tr/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/TB5N8cN/trt2.png",TRT 2
https://tv-trt2.medya.trt.com.tr/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Fq0ZvYG/meltemtvt.png",MELTEM TV
https://vhxyrsly.rocketcdn.com/meltemtv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/sRNHKjS/tivi622.png",TİVİ 6
https://live.artidijitalmedya.com/artidijital_tivi6/tivi6/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/SnPFhXS/cnee12.png",CİNE 1
https://live.artidijitalmedya.com/artidijital_cine1/cine1/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/8dQdNrv/akilli22.png",AKILLI TV
https://yayin.santraltr.com/hls/akillitv.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/QQQR6VK/dmax.png",DMAX
https://dogus-live.daioncdn.net/dmax/dmax.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/QQQR6VK/dmax.png",DMAX
https://dmax.blutv.com/blutv_dmax2/live.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Z1vHy41/tlc.png",TLC TR
https://dogus-live.daioncdn.net/tlc/tlc.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Z1vHy41/tlc.png",TLC TR
https://tlc.blutv.com/blutv_tlc_live/live.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/FVnG3Zr/360tv.png",360
https://turkmedya-live.ercdn.net/tv360/tv360.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/FVnG3Zr/360tv.png",360
https://tv.ensonhaber.com/tv360/tv360.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/pXncfpb/tv422.png",TV 4
https://turkmedya-live.ercdn.net/tv4/tv4.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/pXncfpb/tv422.png",TV 4
https://tv4.blutv.com/blutv_tv4/live.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/N2n2tqMz/tyt.png",TYT TÜRK
https://cdn-tytturk.yayin.com.tr/tytturk/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/VWRBg1M/trklinik.png",TÜRKİYE KLİNİKLERİ TV
http://mn-nl.mncdn.com/turkiyeklinikleri/smil:turkiyeklinikleri/chunklist_b3128000.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/s9gLmqv/cgtnch.png",CGTN BELGESEL
https://mn-nl.mncdn.com/dogusdyg_drone/cgtn/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/TTwc1rR/saglikch.png",SAĞLIK CHANNEL
https://live.euromediacenter.com/saglikchannel/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/DKHDfbr/wmtv.png",WOMAN KADIN TV
https://embedlp.b-cdn.net/womantv.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/YQtd480/wlife.jpg",WOMAN LIFE TV
https://yayin30.haber100.com/live/womanlifetv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/qRsfyb2/tvmor.png",MOR TV
https://live.euromediacenter.com/tvmor/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/SBhSXwk/Cine5tv.jpg",CINE5 TV
https://cdn-cine5tv.yayin.com.tr/cine5tv/cine5tv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/PZW37ch0/onstv.jpg",ONS TV
https://cdn-onstv.yayin.com.tr/onstv/tracks-v1a1/mono.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/PZW37ch0/onstv.jpg",ONS TV
https://live.artidijitalmedya.com/artidijital_onstv/onstv/artidijital_onstv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/1Z22dCY/teve2.png",TEVE 2
https://live.duhnet.tv/S2/HLS_LIVE/teve2np/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/1Z22dCY/teve2.png",TEVE 2
https://demiroren-live.daioncdn.net/teve2/teve2.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/dgj3MTh/tv85.png",TV8 BUÇUK
https://tv8.daioncdn.net/tv8bucuk/tv8bucuk.m3u8?app=tv8bucuk_web
#EXTINF:-1 tvg-logo="https://i.ibb.co/dgj3MTh/tv85.png",TV8 BUÇUK
https://bcovlive-a.akamaihd.net/8fe5dabcdbcd4af0ace7b991a12a6a4c/eu-central-1/6415845530001/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/1Ty8Z3X/bizimev.png",BİZİM EV TV
https://ythls-v3.onrender.com/channel/UCIHMK8qtjB_GNuXmeex6i8g.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/kxjKk89/showmax.png",SHOW MAX
https://raw.githubusercontent.com/ipstreet312/freeiptv/master/ressources/tur/shmax.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/kxjKk89/showmax.png",SHOW MAX
https://ythls.armelin.one/video/Y3vGHFrsqrs.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/2qrg9QF/a2022.png",A2
https://trkvz-live.ercdn.net/a2tv/a2tv.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/2qrg9QF/a2022.png",A2
https://trkvz-live.daioncdn.net/a2tv/a2tv.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Zd6fMvZ/filtr.png",FİL TV
https://live.filbox.com.tr/filtv/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/rynNr53/yabantv.png",YABAN TV
https://asds.tech/ch/yaban.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/kxjKk89/showmax.png",SHOW MAX (backup)
https://ythlsgo.onrender.com/video/Y3vGHFrsqrs.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/kxjKk89/showmax.png",SHOW MAX (backup)
https://livestream.zazerconer.workers.dev/stream/Y3vGHFrsqrs.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/kxjKk89/showmax.png",SHOW MAX (backup)
https://new.cache-stream.workers.dev/stream/Y3vGHFrsqrs/live.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/kxjKk89/showmax.png",SHOW MAX [tkn-blocked]
https://ciner-live.ercdn.net/showmax/showmax.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/2qrg9QF/a2022.png",A2 (backup)
https://new.cache-stream.workers.dev/stream/UCHqu50_C2U2h_rpzhygs4aA/live.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/2qrg9QF/a2022.png",A2 (backup)
https://ythls.armelin.one/channel/UCHqu50_C2U2h_rpzhygs4aA.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/2qrg9QF/a2022.png",A2 (backup)
http://stream.tvcdn.net/eglence/a2.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/2qrg9QF/a2022.png",A2 (backup)
https://trkvz.daioncdn.net/a2tv/a2tv.m3u8?ce=3&app=59363a60-be96-4f73-9eff-355d0ff2c758
#EXTINF:-1 tvg-logo="https://i.ibb.co/2qrg9QF/a2022.png",A2 [tkn-blocked]
https://trkvz-live.daioncdn.net/a2tv/a2tv.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/1Z22dCY/teve2.png",TEVE 2 (backup)
https://demiroren.daioncdn.net/teve2/teve2.m3u8?app=6aab838a-437e-4a1b-bbd0-e30f79cdbbbd
#EXTINF:-1 tvg-logo="https://i.ibb.co/dgj3MTh/tv85.png",TV8 BUÇUK (backup)
https://rkhubpaomb.turknet.ercdn.net/fwjkgpasof/tv8bucuk/tv8bucuk.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/dgj3MTh/tv85.png",TV8 BUÇUK (backup)
https://tv8-live.daioncdn.net/tv8bucuk/tv8bucuk.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/dgj3MTh/tv85.png",TV8 BUÇUK (backup)
https://tv8.daioncdn.net/tv8bucuk/tv8bucuk.m3u8?app=bf58ab52-4865-4c81-b223-26b41009801e
#EXTINF:-1 tvg-logo="https://i.ibb.co/dgj3MTh/tv85.png",TV8 BUÇUK [tkn-blocked]
https://tv8-tb-live.ercdn.net/tv8bucuk/tv8bucuk.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/N1h8m96/trtbelgesel.png",TRT BELGESEL (backup)
https://tv-trtbelgesel.medya.trt.com.tr/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/N1h8m96/trtbelgesel.png",TRT BELGESEL (backup)
https://d2xwn494f2lep.cloudfront.net/v1/master/80dbfc318ab6b980679b32095ba497236de6d2f9/TRT-Belgesel/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/N1h8m96/trtbelgesel.png",TRT BELGESEL (backup)
http://tv-trtbelgesel.live.trt.com.tr/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/QQQR6VK/dmax.png",DMAX (backup)
http://dygvideo.dygdigital.com/live/hls/dmaxdai?m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/QQQR6VK/dmax.png",DMAX [downline]
http://canli.haber365.com.tr/tr/dmax/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Z1vHy41/tlc.png",TLC TR [downline]
http://canli.haber365.com.tr/tr/tlc/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Z1vHy41/tlc.png",TLC TR (backup)
http://dygvideo.dygdigital.com/live/hls/tlctvdai?m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Z1vHy41/tlc.png",TLC TR (backup)
https://dogus.daioncdn.net/tlc/tlc.m3u8?app=1aca0aa1-06e3-41ff-a8e5-38d7df475469
#EXTINF:-1 tvg-logo="https://i.ibb.co/FVnG3Zr/360tv.png",360 [tkn-blocked]
https://mn-nl.mncdn.com/360tv_live/360tv.smil/chunklist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/FVnG3Zr/360tv.png",360 (backup)
https://360tv.blutv.com/blutv_360tv_live/live.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/FVnG3Zr/360tv.png",360 (backup)
http://canli.haber365.com.tr/tr/360tv/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/DKHDfbr/wmtv.png",WOMAN KADIN TV (backup)
https://s01.webcaster.cloud/wmtv/live_1080p.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/DKHDfbr/wmtv.png",WOMAN KADIN TV (backup)
https://s01.vpis.io/wmtv/wmtv.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/DKHDfbr/wmtv.png",WOMAN KADIN TV (backup)
https://womantv.blutv.com/blutv_womantv/blutv_womantv/index.m3u8


#EXTINF:-1 tvg-logo="https://i.ibb.co/YjkMYbF/trtcocuk21a.png" group-title="8. |TR|🇹🇷 ÇOCUK / SPOR",TRT ÇOCUK
https://tv-trtcocuk.medya.trt.com.tr/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/qDF8pHQ/tdcc.png",TRT DİYANET ÇOCUK
https://tv-trtdiyanetcocuk.medya.trt.com.tr/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/R2Zgy7F/minikago.png",MİNİKA GO (sometimes)
https://trkvz-live.daioncdn.net/minikago/minikago.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/L8ftBdN/minikacocuk.png",MİNİKA ÇOCUK (sometimes)
https://trkvz-live.daioncdn.net/minikago_cocuk/minikago_cocuk.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Zxd0j45/cartoonnetwork.png",CARTOON NETWORK TR
http://51.20.137.71/stream/yt/cartoonnetwork.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/SwwjnF5/gstv.png",GALATASARAY TV
https://owifavo5.rocketcdn.com/gstv/gstv.smil/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/867fC4z/fbtv22a.png",FENERBAHÇE TV
https://1hskrdto.rocketcdn.com/fenerbahcetv.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/F0Tsz1v/htsportr.png",HT SPOR
https://ciner-live.ercdn.net/htspor/htspor.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/F0Tsz1v/htsportr.png",HT SPOR
https://ciner-live.daioncdn.net/ht-spor/ht-spor.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/xSjB51j/aspor.png",A SPOR
https://rnttwmjcin.turknet.ercdn.net/lcpmvefbyo/aspor/aspor_480p.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/xSjB51j/aspor.png",A SPOR
https://rnttwmjcin.turknet.ercdn.net/lcpmvefbyo/aspor/aspor.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/BfM21nC/beinhaber.png",BIS HABER
https://ythls-v3.onrender.com/channel/UCPe9vNjHF1kEExT5kHwc7aw.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/BfM21nC/beinhaber.png",BIS HABER
https://tgn.bozztv.com/dvrfl05/gin-beinsportshaber/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/4Rm7Z6Z/sports22.png",SPORTS TV
https://sportstv.blutv.com/blutv_sportstv2/live.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/4Rm7Z6Z/sports22.png",SPORTS TV
https://live.sportstv.com.tr/hls/low/sportstv_hd/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/3WmLjwG/trtspor22c.png",TRT SPOR [geo-blocked]
https://tv-trtspor1.medya.trt.com.tr/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/3WmLjwG/trtspor22c.png",TRT SPOR [geo-blocked]
https://trt.daioncdn.net/trtspor/master.m3u8?app=9b65474e-8197-4899-aabb-321fcf6dd9eb
#EXTINF:-1 tvg-logo="https://i.ibb.co/ky3qVPc/trtspory2.png",TRT SPOR2 YILDIZ [geo-blocked]
https://tv-trtspor2.medya.trt.com.tr/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/YBDCT7q/tabii.png",TABİİ SPOR 1 [geoblocked]
https://tabii-spor.medya.trt.com.tr/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/YBDCT7q/tabii.png",TABİİ SPOR 2 [geoblocked]
https://tabii-spor2.medya.trt.com.tr/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/YBDCT7q/tabii.png",TABİİ SPOR 3 [geoblocked]
https://tabii-spor3.medya.trt.com.tr/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/YBDCT7q/tabii.png",TABİİ SPOR 4 [geoblocked]
https://tabii-spor4.medya.trt.com.tr/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/YBDCT7q/tabii.png",TABİİ SPOR 5 [geoblocked]
https://tabii-spor5.medya.trt.com.tr/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/YBDCT7q/tabii.png",TABİİ SPOR 6 [geoblocked]
https://tabii-spor6.medya.trt.com.tr/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/0Yt6jbg/tjk.png",TJK TV [geo-blocked]
http://tjktv.ercdn.net/tjktv.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/0Yt6jbg/tjk.png",TJK TV [geo-blocked]
http://tjktv-live.tjk.org/tjktv.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/0Yt6jbg/tjk.png",TJK TV
https://new.cache-stream.workers.dev/stream/kDvc4MSsnyI/live.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/dgpChqK/horses.png",BY HORSES TV
https://byhorses.blutv.com/blutv_byhorses/blutv_byhorses/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/dgpChqK/horses.png",BY HORSES TV
https://new.cache-stream.workers.dev/stream/UCQgq6bnp3N_ZlyNq5dHmkNw/live.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/J5QjKLt/tay22.png",TAY TV
https://duhnet.hipodrom.com/S2/HLS_LIVE/mislitaynp/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/J5QjKLt/tay22.png",TAY TV
https://ythlsgo.onrender.com/channel/UCjkRA7KEdp7PDKDUs396XHg.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/8g20RBH/ebatek.png",TRT EBA TV
https://tv-e-okul01.medya.trt.com.tr/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/8g20RBH/ebatek.png",TRT EBA TV
https://ebao.blutv.com/blutv_ebao2/live.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/L8ftBdN/minikacocuk.png",MİNİKA ÇOCUK (offline)
http://trn10.tulix.tv/gt-minikacocuk/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/R2Zgy7F/minikago.png",MİNİKA GO (offline)
http://trn10.tulix.tv/gt-minikago/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/R2Zgy7F/minikago.png",MİNİKA GO (backup)
http://tgn.bozztv.com/dvrfl05/gin-minikago/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Zxd0j45/cartoonnetwork.png",CARTOON NETWORK TR (offline)
https://cartoonnetwork.blutv.com/blutv_cartoonnetwork/live.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/R2Zgy7F/minikago.png",MİNİKA GO (backoff)
https://trkvz-live.daioncdn.net/minikago/minikago.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/R2Zgy7F/minikago.png",MİNİKA GO (backoff)
https://trkvz.daioncdn.net/minikago/minikago.m3u8?app=web&ce=3
#EXTINF:-1 tvg-logo="https://i.ibb.co/L8ftBdN/minikacocuk.png",MİNİKA ÇOCUK (backoff)
https://trkvz-live.daioncdn.net/minikago_cocuk/minikago_cocuk.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/L8ftBdN/minikacocuk.png",MİNİKA ÇOCUK (backoff)
https://trkvz.daioncdn.net/minikago_cocuk/minikago_cocuk.m3u8?app=web&ce=3
#EXTINF:-1 tvg-logo="https://i.ibb.co/F0Tsz1v/htsportr.png",HT SPOR (backup)
https://ciner.daioncdn.net/ht-spor/ht-spor.m3u8?app=web
#EXTINF:-1 tvg-logo="https://i.ibb.co/F0Tsz1v/htsportr.png",HT SPOR (backup)
https://ythls.armelin.one/channel/UCK3mI2lsk3LSo8PBUc8JTSw.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/F0Tsz1v/htsportr.png",HT SPOR (backup)
https://deathlesstg.serv00.net/Youtube-Live/index.php?id=Eg7c3jB39Hc&m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/BfM21nC/beinhaber.png",BIS HABER (backup)
https://raw.githubusercontent.com/rideordie16/YouTube/main/spor/beinsportshaber.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/BfM21nC/beinhaber.png",BIS HABER (backup)
https://deathlesstg.serv00.net/Youtube-Live/index.php?id=OypUpUTYAHI&m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/BfM21nC/beinhaber.png",BIS HABER (backup)
https://koprulu1.global.ssl.fastly.net/ythls?kanal_id=UCPe9vNjHF1kEExT5kHwc7aw.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/BfM21nC/beinhaber.png",BIS HABER (backup)
https://livestream.zazerconer.workers.dev/channel/UCPe9vNjHF1kEExT5kHwc7aw.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/BfM21nC/beinhaber.png",BIS HABER (backup)
https://ythls.armelin.one/channel/UCPe9vNjHF1kEExT5kHwc7aw.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/BfM21nC/beinhaber.png",BIS HABER (backup)
https://new.cache-stream.workers.dev/stream/UCPe9vNjHF1kEExT5kHwc7aw/live.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/3WmLjwG/trtspor22c.png",TRT SPOR (backup)
https://trt.daioncdn.net/trtspor/master.m3u8?app=web
#EXTINF:-1 tvg-logo="https://i.ibb.co/ky3qVPc/trtspory2.png",TRT SPOR2 YILDIZ (backup)
https://trt.daioncdn.net/trtspor-yildiz/master.m3u8?&app=2c6690bb-4021-4292-8ddc-c93a3cf04a3a
#EXTINF:-1 tvg-logo="https://i.ibb.co/M9kWXzt/trt3spor22c.png",TRT3 SPOR [offline]
https://tv-trt3.live.trt.com.tr/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/M9kWXzt/trt3spor22c.png",TRT3 SPOR [offline]
https://bozztv.com/inim03/live1/trtspor3/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/YjkMYbF/trtcocuk21a.png",TRT ÇOCUK (backup)
https://tv-trtcocuk.live.trt.com.tr/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/4Rm7Z6Z/sports22.png",SPORTS TV (backup)
https://live.sportstv.com.tr/hls/low/sportstv.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/xSjB51j/aspor.png",A SPOR (backup)
https://x.canlitvapp.com/aspor/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/xSjB51j/aspor.png",A SPOR (backup)
https://trkvz-live.daioncdn.net/aspor/aspor.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/xSjB51j/aspor.png",A SPOR (backup)
https://rnttwmjcin.turknet.ercdn.net/lcpmvefbyo/aspor/aspor_720p.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/xSjB51j/aspor.png",A SPOR (backup)
https://trkvz.daioncdn.net/aspor/aspor.m3u8?ce=3&app=45f847c4-04e8-419a-a561-2ebf87084765
#EXTINF:-1 tvg-logo="https://i.ibb.co/xSjB51j/aspor.png",A SPOR (backup)
https://ythlsgo.onrender.com/video/SzLuO_PW43A.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/xSjB51j/aspor.png",A SPOR (backup)
https://new.cache-stream.workers.dev/stream/UCJElRTCNEmLemgirqvsW63Q/live.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/xSjB51j/aspor.png",A SPOR (backup)
https://raw.githubusercontent.com/rideordie16/YouTube/main/spor/aspor.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/xSjB51j/aspor.png",A SPOR (backup)
https://ythls.armelin.one/channel/UCJElRTCNEmLemgirqvsW63Q.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/xSjB51j/aspor.png",A SPOR [tkn-blocked]
https://trkvz-live.daioncdn.net/aspor/aspor.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/xSjB51j/aspor.png",A SPOR [tkn-blocked]
https://trkvz-beta.daioncdn.net/aspor/aspor.m3u8?app=45f847c4-04e8-419a-a561-2ebf87084765
#EXTINF:-1 tvg-logo="https://i.ibb.co/F0Tsz1v/htsportr.png",HT SPOR (backup)
https://new.cache-stream.workers.dev/stream/UCK3mI2lsk3LSo8PBUc8JTSw/live.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/F0Tsz1v/htsportr.png",HT SPOR (backup)
https://livestream.zazerconer.workers.dev/channel/UCK3mI2lsk3LSo8PBUc8JTSw.m3u8


#EXTINF:-1 tvg-logo="https://i.ibb.co/gdbyhx2/spotify.png" group-title="9. |TR|🇹🇷 MÜZİK",SPOTIFY TURKEY • TRLIST 👤🎧🎤📻💯
https://github.com/ipstreet312/freeiptv/raw/master/ressources/infos/barkers/sptr.ts
#EXTINF:-1 tvg-logo="https://i.ibb.co/gdbyhx2/spotify.png",SPOTIFY TURKEY • 2025 🎶🎵🎼🎹🪗
https://github.com/ipstreet312/freeiptv/raw/master/ressources/infos/barkers/sptr25.ts
#EXTINF:-1 tvg-logo="https://i.ibb.co/gdbyhx2/spotify.png",SPOTIFY TURKEY • 2024 🎸🎷🎺🎻🪕
https://github.com/ipstreet312/freeiptv/raw/master/ressources/infos/barkers/spb24.ts
#EXTINF:-1 tvg-logo="https://i.ibb.co/d6Zfm2P/trtmuzik21c.png",TRT MÜZİK
https://tv-trtmuzik.medya.trt.com.tr/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/6401NQw/kraltv.png",KRAL - KRAL POP
http://dygvideo.dygdigital.com/live/hls/kralpop?m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/6401NQw/kraltv.png",KRAL - KRAL POP
https://dogus-live.daioncdn.net/kralpoptv/kralpoptv.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/4SsJS4R/dreamturk.png",DREAM TÜRK
https://live.duhnet.tv/S2/HLS_LIVE/dreamturknp/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/B6N9KsN/powerturk22.png",POWER TÜRK
http://livetv.powerapp.com.tr/powerturkTV/powerturkhd.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/B6N9KsN/powerturk22.png",POWER TÜRK
https://live.artidijitalmedya.com/artidijital_powerturktv/powerturktv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/wy1H8jM/pturkttaze.png",POWER TÜRK TAPTAZE
http://livetv.powerapp.com.tr/pturktaptaze/taptaze.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/rZxNWKv/pslow.png",POWER TÜRK SLOW
http://livetv.powerapp.com.tr/pturkslow/slow.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/FgCW885/pturkakustik.png",POWER TÜRK AKUSTİK
http://livetv.powerapp.com.tr/pturkakustik/akustik.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/cQfPfgR/tatlises.png",TATLISES
https://live.artidijitalmedya.com/artidijital_tatlisestv/tatlisestv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Jqzzby7/milyontv.png",MİLYON TV
https://sosyoapp-live.cdnnew.com/sosyo/buraya-bir-isim-verin.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/wSPFds2/nr1turk.png",NUMBER ONE TÜRK
https://b01c02nl.mediatriple.net/videoonlylive/mtkgeuihrlfwlive/broadcast_5c9e187770143.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/wSPFds2/nr1turk.png",NUMBER ONE TÜRK
https://nr1turk.blutv.com/blutv_n1turk/blutv_n1turk/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/jJWLsCQ/nr1ask.jpg",NUMBER ONE TÜRK ASK
https://b01c02nl.mediatriple.net/videoonlylive/mtkgeuihrlfwlive/u_stream_5c9e18f9cea15_1/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/jJWLsCQ/nr1ask.jpg",NUMBER ONE TÜRK ASK
https://b01c02nl.mediatriple.net/videoonlylive/mtkgeuihrlfwlive/broadcast_5c9e18f9c54e6.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/824MwJ6/nr1damar.jpg",NUMBER ONE TÜRK DAMAR
https://b01c02nl.mediatriple.net/videoonlylive/mtkgeuihrlfwlive/u_stream_5c9e198784bdc_1/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/824MwJ6/nr1damar.jpg",NUMBER ONE TÜRK DAMAR
https://b01c02nl.mediatriple.net/videoonlylive/mtkgeuihrlfwlive/broadcast_5c9e19877b340.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/LR5v10B/nr1dance.jpg",NUMBER ONE TÜRK DANCE
https://b01c02nl.mediatriple.net/videoonlylive/mtkgeuihrlfwlive/u_stream_5c9e2aa8acf44_1/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/LR5v10B/nr1dance.jpg",NUMBER ONE TÜRK DANCE
https://b01c02nl.mediatriple.net/videoonlylive/mtkgeuihrlfwlive/broadcast_5c9e2aa89e721.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/bQHyST5/nr1tv.png",NUMBER ONE
https://b01c02nl.mediatriple.net/videoonlylive/mtkgeuihrlfwlive/broadcast_5c9e17cd59e8b.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/bQHyST5/nr1tv.png",NUMBER ONE
https://nr1.blutv.com/blutv_n1/blutv_n1/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/9grLJCS/fone22.png",FASHION ONE
https://b01c02nl.mediatriple.net/videoonlylive/mtkgeuihrlfwlive/u_stream_5c9e2ee6997cb_1/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/9grLJCS/fone22.png",FASHION ONE
https://b01c02nl.mediatriple.net/videoonlylive/mtkgeuihrlfwlive/broadcast_5c9e2ee690051.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/xhfcTC7/powertv.png",POWER TV
http://livetv.powerapp.com.tr/powerTV/powerhd.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/xhfcTC7/powertv.png",POWER TV
https://live.artidijitalmedya.com/artidijital_powertv/powertv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/FVNL477/pdance.png",POWER DANCE
http://livetv.powerapp.com.tr/dance/dance.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/VLQ6cmV/plove.png",POWER LOVE
http://livetv.powerapp.com.tr/plove/love.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/bQHyST5/nr1tv.png",NUMBER ONE (backup)
https://b01c02nl.mediatriple.net/videoonlylive/mtkgeuihrlfwlive/u_stream_5c9e17cd6360b_1/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/6401NQw/kraltv.png",KRAL - KRAL POP (backup)
http://dygvideo.dygdigital.com/live/hls/puhukralpopdai?m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/6401NQw/kraltv.png",KRAL - KRAL POP (backup)
https://dogus.daioncdn.net/kralpoptv/kralpoptv.m3u8?app=f38a38b4-ce55-4040-8676-9826937d6128


#EXTINF:-1 tvg-logo="https://i.ibb.co/xzZk0Yq/trtavaz.png" group-title="10. |TR|🇹🇷 AVRUPA; DİNÎ; DİĞER",TRT AVAZ
https://tv-trtavaz.medya.trt.com.tr/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/swtn1kV/trtturk.png",TRT TÜRK
https://tv-trtturk.medya.trt.com.tr/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/cDxKJy1/k7avr1.png",KANAL 7 AVRUPA
https://livetv.radyotvonline.net/kanal7live/kanal7avr/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/cDxKJy1/k7avr1.png",KANAL 7 AVRUPA
https://raw.githubusercontent.com/UzunMuhalefet/yayinlar/main/streams/kanal7avrupa.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/WvhGGP0/showturk1.png",SHOW TÜRK
https://raw.githubusercontent.com/ipstreet312/freeiptv/master/ressources/tur/shturk.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/WvhGGP0/showturk1.png",SHOW TÜRK
https://ythls.armelin.one/video/XnvS-RZa4Qw.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/THj0Jrg/eurod22.png",EURO D
https://live.duhnet.tv/S2/HLS_LIVE/eurodnp/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/THj0Jrg/eurod22.png",EURO D (geçici geçerli)
https://bozztv.com/inim03/live1/eurod/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Lg90xsB/eurostar22.png",EURO STAR
https://raw.githubusercontent.com/ipstreet312/freeiptv/master/ressources/tur/estar.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Lg90xsB/eurostar22.png",EURO STAR (geçici geçerli)
https://bozztv.com/gin-trn10/gt-eurostar/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/PtH4wGr/atvavr.png",ATV AVRUPA (geçici geçerli)
https://tgn.bozztv.com/dvrfl05/gin-atvavrupa/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/n7Jy3h5/tv8int22.png",TV8 INT (geçici geçerli)
https://tgn.bozztv.com/dvrfl05/gin-tv8int/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/MCXCRcn/tgrteu1.png",TGRT EU
https://tgrt-live.ercdn.net/tgrteu/tgrteu.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/MCXCRcn/tgrteu1.png",TGRT EU
https://canli.tgrteu.com/tgrteu.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/1RnLJpf/agro.png",AGRO TV
https://yayin30.haber100.com/live/agrotv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/1RnLJpf/agro.png",AGRO TV
https://agrotv.blutv.com/blutv_agrotv/live.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/vHwMgx0/ciftci.png",ÇİFTÇİ TV
https://live.artidijitalmedya.com/artidijital_ciftcitv/ciftcitv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tDB51ww/tarim.png",TARIM TV
https://content.tvkur.com/l/c7e1da7mm25p552d9u9g/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/hB9yNXV/yol22.png",YOL TV
https://iptv.amgsmart2home.de/YOLTVMAIN/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/X7zxL8v/knlb.png",KANAL B
https://baskentaudiovideo.xyz/LiveApp/streams/mUE22idl26lA1683879097431.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Sc4DY66/emtv.webp",EM TV
https://cdn-tvem.yayin.com.tr/TVEM/TVEM/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/k9phm3v/diyanettv.png",DİYANET TV
https://diyanet.blutv.com/blutv_diyanet2/live.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/k9phm3v/diyanettv.png",DİYANET TV
https://eustr73.mediatriple.net/videoonlylive/mtikoimxnztxlive/broadcast_5e3bf95a47e07.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/k8L3Mq1/semerkandtv.png",SEMERKAND
https://b01c02nl.mediatriple.net/videoonlylive/mtisvwurbfcyslive/broadcast_58d915bd40efc.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/k8L3Mq1/semerkandtv.png",SEMERKAND WAY
https://b01c02nl.mediatriple.net/videoonlylive/mtisvwurbfcyslive/broadcast_6409fdaa68111.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/jwgqtSB/dosttv.png",DOST TV
https://dost.stream.emsal.im/tv/live.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tHfxLTn/rehbertv.png",REHBER TV
https://cdn4.yayin.com.tr/rehbertv/tracks-v1a1/mono.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/wrL2khn/lalegul.png",LALEGÜL TV
https://lbl.netmedya.net/hls/lalegultv.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/yN9HKJ6/berrat.png",BERAT TV
https://cdn-berattv.yayin.com.tr/berattv/berattv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/bj1H8LCm/vavtv.png",VAV TV
https://trkvz-live.ercdn.net/vavtv/vavtv.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/FX1SqtR/cantv.jpg",CAN TV
http://canbroadcast.com:7000/canlican/tv.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/FX1SqtR/cantv.jpg",CAN TV
https://livetv.canbroadcast.com:7443/canlican/tv.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/6B8M20v/on422.png",ON4 TV
https://edge1.socialsmart.tv/on4/bant1/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/DMRJYJM/afroturk.png",AFRO TURK TV
https://edge1.socialsmart.tv/live/naturaltv/bant1/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/KjLpH6t/luys.png",LUYS TV
https://b01c02nl.mediatriple.net/videoonlylive/mtpayqrfkgirxelive/broadcast_5e91c5ac96898.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Cm1kp8f/sat7turk.png",SAT 7 TÜRK
https://svs.itworkscdn.net/sat7turklive/sat7turk.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Cm1kp8f/sat7turk.png",SAT 7 TÜRK
https://live.artidijitalmedya.com/artidijital_sat7turk/sat7turk/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/1qFR0jX/Kanalhayat.png",KANAL HAYAT
https://livecdn.use1-0004.jwplive.com/live/sites/WpgVdplm/media/icNwL50b/live.isml/live.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/ChhQT8b/Abn.png",ABN TURKEY
https://mediaserver.abnvideos.com/streams/turkish__discipleship.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/JHH0xcX/tgrtbel22.png",TGRT BELGESEL
https://b01c02nl.mediatriple.net/videoonlylive/mtsxxkzwwuqtglive/broadcast_5fe462afc6a0e.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/JHH0xcX/tgrtbel22.png",TGRT BELGESEL
https://tgrt-live.ercdn.net/tgrtbelgesel/tgrtbelgesel.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/MCXCRcn/tgrteu1.png",TGRT EU (backup)
https://tv.ensonhaber.com/tgrteu/tgrteu.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/MCXCRcn/tgrteu1.png",TGRT EU (backup)
https://ensonhaber-live.ercdn.net/tgrteu/tgrteu.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/MCXCRcn/tgrteu1.png",TGRT EU (backup)
https://canli.haber365.com.tr/tr/tgrteu/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/JHH0xcX/tgrtbel22.png",TGRT BELGESEL (backup)
https://canli.ihlasdigitalassets.com/tgrtbelgesel.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/JHH0xcX/tgrtbel22.png",TGRT BELGESEL (backup)
https://ensonhaber-live.ercdn.net/tgrtbelgesel/tgrtbelgesel.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/JHH0xcX/tgrtbel22.png",TGRT BELGESEL (backup)
https://tv.ensonhaber.com/tgrtbelgesel/tgrtbelgesel.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/JHH0xcX/tgrtbel22.png",TGRT BELGESEL (backup)
https://canli.haber365.com.tr/tr/tgrtbelgesel/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/JHH0xcX/tgrtbel22.png",TGRT BELGESEL (checkalt)
https://tv.ensonhaber.com/tv/tr/tgrtbelgesel/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/cDxKJy1/k7avr1.png",KANAL 7 AVRUPA [off-link]
https://live.kanal7.com/live/kanal7AvrupaLive/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/cDxKJy1/k7avr1.png",KANAL 7 AVRUPA (backup)
https://raw.githubusercontent.com/rideordie16/YouTube/main/ch/kanal7eu.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/PtH4wGr/atvavr.png",ATV AVRUPA (backoff)
https://trkvz-live.ercdn.net/atvavrupa/atvavrupa.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/WvhGGP0/showturk1.png",SHOW TÜRK (geçici geçerli)
https://bozztv.com/inim03/live1/showtvturk/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/WvhGGP0/showturk1.png",SHOW TÜRK (geçici geçerli)
http://nimplus3.bozztv.com/showtvturk/showtvturk/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/PtH4wGr/atvavr.png",ATV AVRUPA (geçici geçerli)
http://nimplus3.bozztv.com/atvavrupa/atvavrupa/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/THj0Jrg/eurod22.png",EURO D (geçici geçerli)
http://nimplus3.bozztv.com/eurod/eurod/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Lg90xsB/eurostar22.png",EURO STAR (geçici geçerli)
http://nimplus3.bozztv.com/eurostar/eurostar/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/n7Jy3h5/tv8int22.png",TV8 INT (geçici geçerli)
http://nimplus3.bozztv.com/tv8int/tv8int/playlist.m3u8


#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png" group-title="11. |TR|🇹🇷 YEREL - BÖLGESEL",ANADOLU NET TV
https://live.artidijitalmedya.com/artidijital_anadolunet/anadolunet/chunks.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",AKSU TV KAHRAMANMARAŞ
https://live.artidijitalmedya.com/artidijital_aksutv/aksutv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",ALANYA POSTA TV
https://win1.yayin.com.tr/postatv/postatv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",ALANYA TV
http://stream2.taksimbilisim.com:1935/alanyatv/smil:alanyatv.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",ALTAS TV ORDU
https://edge1.socialsmart.tv/altastv/bant1/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",ART AMASYA
http://stream.tvcdn.net/yerel/art-amasya.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",AS TV BURSA
https://waw2.artiyerelmedya.net/astv/bant1/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",AS TV BURSA
https://live.artidijitalmedya.com/artidijital_astv/astv/chunks.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",BARTIN TV
http://cdn-bartintv.yayin.com.tr/BARTINTV/BARTINTV/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",BEYKENT TV
https://yayin30.haber100.com/live/beykenttv/chunklist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",BİR TV İZMİR
https://live.artidijitalmedya.com/artidijital_birtv/birtv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",BİR TV İZMİR
https://edge1.socialsmart.tv/birtv/bant1/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",BRTV KARABÜK
https://live.artidijitalmedya.com/artidijital_brtv/brtv/chunks.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",BURSA LINE TV
https://edge1.socialsmart.tv/linetv/bant1/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",BURSA ON6 TV
https://live.artidijitalmedya.com/artidijital_kanal16/kanal16/chunks.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",BURSA ON6 TV
https://live.euromediacenter.com/on6tvyayin/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",BÜLTEN TV ANKARA
https://cdn1-bultentv.yayin.com.tr/bultentv/bultentv/chunks.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",ÇAY TV RİZE
https://edge1.socialsmart.tv/caytv/bant1/chunks.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",ÇAY TV RİZE
http://stream2.taksimbilisim.com:1935/caytv/bant1/CAYTV.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",ÇEKMEKÖY BELEDİYE TV
https://cdn-cekmekoybeltv.yayin.com.tr/cekmekoybeltv/amlst:cekmekoybeltv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",ÇORUM BLD TV
https://edge1.socialsmart.tv/corumbelediyesilive/bant1/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",DEHA TV DENİZLİ
https://live.artidijitalmedya.com/artidijital_dehatv/dehatv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",DENİZ POSTASI TV
https://live.artidijitalmedya.com/artidijital_denizpostasi/denizpostasi/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",DİM TV ALANYA
https://live.artidijitalmedya.com/artidijital_dimtv/dimtv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",DİYAR TV
https://yayin30.haber100.com/live/diyartv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",DİYAR TV
https://live.artidijitalmedya.com/artidijital_diyartv/diyartv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",DRT DENİZLİ
https://edge1.socialsmart.tv/drttv/bant1/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",DRT DENİZLİ
http://stream2.taksimbilisim.com:1935/drt/smil:drt.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",DÜĞÜN TV ÇİNE
https://cdn-duguntvmedya.yayin.com.tr/duguntvmedya/duguntvmedya/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",EDESSA TV ŞANLIURFA
https://tv170.radyotelekom.com.tr:21764/edessatv/edessatv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png" referer="https://fm.tv.tr/",EGE TV İZMİR
https://radyotelekomtv.com/player/m3u8/366fe57e47b8093df9bb22ff1e7f5bd6/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",EGE MAX İZMİR
https://customer-c7coo2iloxeojh2d.cloudflarestream.com/c61484b2af92bef0814536122d01233c/manifest/stream_t5f28a648e8b16a70a2ceec733b098bc5_r899548610.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",EGE LIVE TV
http://stream.tvcdn.net/yerel/ege-live-tv.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",ELMAS TV ZONGULDAK
https://edge1.socialsmart.tv/elmastv/bant1/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",ER TV MALATYA
https://live.artidijitalmedya.com/artidijital_ertv_new/ertv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",ERCİS TV
https://cdn1-ercistv.yayin.com.tr/ercistv/amlst:ercistv/chunklist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",ERCİYES TV
https://live.artidijitalmedya.com/artidijital_erciyestv/erciyestv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",ERT ŞAH TV ERZİNCAN
http://win20.yayin.com.tr/ertsahtv/ertsahtv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",ERZURUM WEB TV
https://win29.yayin.com.tr/erzurumwebtv/erzurumwebtv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",ES TV ESKİŞEHİR
https://live.artidijitalmedya.com/artidijital_estv/estv/chunks.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",EDİRNE TV
https://yayin.edirnetv.com:8088/hls/etvcanliyayin.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",EFES DOST TV
https://cdn-efesdosttv.yayin.com.tr/efesdosttv/efesdosttv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",ESENLER ŞEHİR TV
https://yayin30.haber100.com/live/sehirekrani/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",ETV KAYSERİ
https://live.artidijitalmedya.com/artidijital_etv/etv/chunks.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",FRT FETHİYE
https://edge1.socialsmart.tv/frttv/bant1/chunks.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",GRT GAZİANTEP TV
https://live.artidijitalmedya.com/artidijital_grt/grt/chunks.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",GÜNEY TV TARSUS
https://edge1.socialsmart.tv/guneytv/bant1/chunks.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",GÜNEYDOĞU TV
https://edge1.socialsmart.tv/gtv/bant1/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",GURBET 24 TV
http://cdn1-gurbet24.yayin.com.tr/gurbet24/ngrp:gurbet24/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",HEDEF TV KOCAELİ
https://cdn1-hedeftv.yayin.com.tr/hedeftv/hedeftv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",HABER61 TRABZON
https://cdn-haber61tv.yayin.com.tr/haber61tv/haber61tv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",HRT HATAY AKDENİZ
http://stream.tvcdn.net/yerel/hrt-akdeniz.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",HUNAT TV KAYSERİ
https://live.artidijitalmedya.com/artidijital_hunattv/hunattv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",İÇEL TV MERSİN
http://stream.taksimbilisim.com:1935/iceltv/bant1/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",İÇEL TV MERSİN
https://edge1.socialsmart.tv/iceltv/bant1/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png" referer="https://player.castr.com/",İSTANBUL TV
https://stream.castr.com/6606b96e9fa9fb790a255296/live_0303bec01eac11efa26bbdf96dc3f28e/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",İZMİR TIME 35 TV
https://cdn-time35tv.yayin.com.tr/time35tv/time35tv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",İZMİR TÜRK TV
http://stream.tvcdn.net/yerel/izmir-turk-tv.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",KANAL 15 BURDUR
https://live.artidijitalmedya.com/artidijital_kanal15/kanal15/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",KANAL 19 ÇORUM
https://live.euromediacenter.com/kanal19/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",KANAL 23 ELAZIĞ
https://live.artidijitalmedya.com/artidijital_kanal23/kanal23/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",KANAL 23 ELAZIĞ
https://cdn13-kanal23.yayin.com.tr/kanal23/kanal23/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",KANAL 26 ESKİŞEHİR
https://live.artidijitalmedya.com/artidijital_kanal26/kanal26/chunks.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",KANAL 3 AFYONKARAHİSAR
https://live.artidijitalmedya.com/artidijital_kanal3/kanal3/chunks.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",KANAL 32 ISPARTA
https://edge1.socialsmart.tv/kanal32/bant1/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",KANAL 33 MERSİN
http://stream.taksimbilisim.com:1935/kanal33/smil:kanal33.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",KANAL 33 MERSİN
https://edge1.socialsmart.tv/kanal33/bant1/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",KANAL 34 İSTANBUL
https://live.euromediacenter.com/kanal34/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",KANAL 53 RİZE
https://kanal53.ozelip.com:3448/hybrid/play.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",KANAL 56 SİİRT
https://cdn-kanal56tv.yayin.com.tr/kanal56tv/kanal56tv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",KANAL 58 SİVAS
https://edge1.socialsmart.tv/kanal58/bant1/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",KANAL 58 SİVAS
https://live.artidijitalmedya.com/artidijital_kanal58/kanal58/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",KANAL 68 AKSARAY
https://live.artidijitalmedya.com/artidijital_kanal68/kanal68/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",KANAL EGE
https://cdn-365tv.yayin.com.tr/365tv/365tv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",KANAL EGE
https://cdn-berat.yayin.com.tr/berat/berat/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",KANAL FIRAT
https://live.artidijitalmedya.com/artidijital_kanalfirat/kanalfirat/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",KANAL S SAMSUN
https://cdn-kanals.yayin.com.tr/kanals/kanals/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",KANAL URFA
https://edge1.socialsmart.tv/kanalurfa/bant1/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",KANAL V ANTALYA
https://live.artidijitalmedya.com/artidijital_kanalv/kanalv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",KANAL Z ZONGULDAK
https://live.artidijitalmedya.com/artidijital_kanalz/kanalz/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",KASTAMONU TV
http://51.91.118.139:8080/live/kastamonutv/kastamonutv/3385.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",KARABÜK DERİN TV
https://cdn1-derintv.yayin.com.tr/derintv/derintv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",KARDELEN TV
https://edge1.socialsmart.tv/kardelentv/bant1/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",KAY TV KAYSERİ
https://live.artidijitalmedya.com/artidijital_kaytv/kaytv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",K+ KAYSERİ
https://live.artidijitalmedya.com/artidijital_kanalplus/kanalplus/mpeg/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",KEÇİÖREN TV ANKARA
https://angr.radyotvonline.net/webtv/smil:kecioren.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",KENT 38 TV KAYSERİ
https://live.artidijitalmedya.com/artidijital_38kenttv/38kenttv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",KENT TV BODRUM
https://edge1.socialsmart.tv/bodrumkenttv/bant1/chunks.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png" referer="https://player.castr.com/",KOCAELİ TV
http://stream.castr.com/64c0d0ebaaa212486ecf0238/live_4faaaa102b8a11ee80f12783ea1667a8/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",KOCAELİ TV
https://edge1.socialsmart.tv/kocaelitv/bant1/chunks.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",KONYA KTV
https://cdn-ktvtv.yayin.com.tr/ktvtv/ktvtv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",KONYA OLAY TV
https://live.artidijitalmedya.com/artidijital_konyaolaytv/konyaolaytv/chunks.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",KOZA TV ADANA
https://ythls.armelin.one/channel/UC4Ohyy56H4EZAy0Pagsv3iA.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",KOZA TV ADANA
https://new.cache-stream.workers.dev/stream/UC4Ohyy56H4EZAy0Pagsv3iA/live.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",LIFE TV KAYSERİ
https://live.artidijitalmedya.com/artidijital_lifetv/lifetv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",MALATYA VUSLAT TV
https://live.artidijitalmedya.com/artidijital_vuslattv/vuslattv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",MANISA ETV
https://edge1.socialsmart.tv/manisaetv/bant1/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",MARMARİS TV
https://cdn-marmariswebtv.yayin.com.tr/marmariswebtv/marmariswebtv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",MERCAN TV ADIYAMAN
https://live.artidijitalmedya.com/artidijital_mercantv/mercantv/chunks.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",METROPOL DENİZLİ
https://edge1.socialsmart.tv/metropoltv/smil/metropoltv/bant1/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",MUĞLA MERKEZ TV
http://nrttn172.kesintisizyayin.com:29010/merkeztv/merkeztv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",MUĞLA TÜRK TV
https://edge1.socialsmart.tv/muglaturk/bant1/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",NOKTA TV KOCAELİ
https://new.cache-stream.workers.dev/stream/UCQuaIes9sMK8Z0VAZsVsvxQ/live.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",NORA TV AKSARAY
https://live.artidijitalmedya.com/artidijital_noratv/noratv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",OGUN TV
https://s01.vpis.io/ogun/ogun.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",OLAY TÜRK KAYSERİ TV
https://live.artidijitalmedya.com/artidijital_olayturk/olayturk/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",OLAY TV BURSA
http://nrttn172.kesintisizyayin.com:29010/olay/olay/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",ORDU BEL TV
https://cdn1-ordubeltv.yayin.com.tr/ordubeltv/ordubeltv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",ORT OSMANİYE TV
https://edge1.socialsmart.tv/orttv/bant1/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",PAMUKKALE TV
http://stream.tvcdn.net/yerel/pamukkale-tv.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",POSTA TV ALANYA
http://cdn-postatv.yayin.com.tr/postatv/postatv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",RADYO KARDEŞ TV FR
http://yayin25.canliyayin.org:1935/live/kardestv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",RİZE TÜRK TV
https://yayin.rizeturk.com:3777/hybrid/play.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",SARIYER TV İST
http://s01.vpis.io/sariyer/sariyer.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",SILKWAY KAZAKH (TUR)
https://raw.githubusercontent.com/ipstreet312/freeiptv/master/ressources/tur/silkway.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",SİNOP YILDIZ TV
http://s01.vpis.io/sinopyildiz/sinopyildiz.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",SKYHABER TV
https://cdn1-skyhabertv.yayin.com.tr/skyhabertv/skyhabertv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",SLOW KARADENİZ TV
https://yayin.slowkaradeniztv.com:3390/hybrid/play.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",SUN RTV MERSİN
https://live.artidijitalmedya.com/artidijital_sunrtv/sunrtv/chunks.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",RUMELİ TV
https://rumelitv-live.ercdn.net/rumelitv/rumelitv.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",TEK RUMELİ TV
https://edge1.socialsmart.tv/tekrumelitv/bant1/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",TEMPO TV
https://live.artidijitalmedya.com/artidijital_tempotv/tempotv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",TV 1 ADANA
https://live.artidijitalmedya.com/artidijital_tva/tva/chunks.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",TV 3 AFYONKARAHİSAR
https://live.artidijitalmedya.com/artidijital_tv3/tv3/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",TİVİ TURK
https://stream.tiviturk.de/live/tiviturk.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",TON TV ÇANAKKALE
https://live.artidijitalmedya.com/artidijital_tontv/tontv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",TOKAT TV
https://cdn-tokattvwebtv.yayin.com.tr/tokattvwebtv/tokattvwebtv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",TRABZON TV
https://raw.githubusercontent.com/UzunMuhalefet/yayinlar/main/streams/trabzontv.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",TRAKYA TÜRK
https://live.artidijitalmedya.com/artidijital_trakyaturk/trakyaturk/chunks.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",TURHAL WEB TV
http://cdn-turhalwebtv.yayin.com.tr/turhalwebtv/turhalwebtv/chunklist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",TV KAYSERİ
https://raw.githubusercontent.com/UzunMuhalefet/yayinlar/main/streams/tvkayseri.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",TV 1 KAYSERİ
https://edge1.socialsmart.tv/tv1/bant1/chunks.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",TV 25 DOĞU
https://cdn-tv25.yayin.com.tr/tv25/tv25/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",TV 264 SAKARYA
http://mc1.mediatriple.net/videoonlylive/mtdxkkitgbrckilive/broadcast_5ee244263fd6d.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",TV 35 İZMİR
http://stream01.tv35.com.tr/hls2/tv35izmir.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",TV 41 KOCAELİ
http://stream.taksimbilisim.com:1935/tv41/bant1/TV41.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",TV 41 KOCAELİ
https://live.artidijitalmedya.com/artidijital_tv41/tv41/chunks.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",TV 48 MİLAS
https://live.euromediacenter.com/tv48/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",TV 52 ORDU
http://stream.taksimbilisim.com:1935/tv52/smil:tv52.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",TV 52 ORDU
https://edge1.socialsmart.tv/tv52/bant1/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",TVO ANTALYA
https://cdn-kanaltvo.yayin.com.tr/kanaltvo/kanaltvo/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",TV DEN AYDIN
http://canli.tvden.com.tr/hls/live.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",TÜRKMENELİ TV
https://135962.global.ssl.fastly.net/5ff366a512987e2c0a3dabfe/live_14378e1002eb11ef9cb025207067897a/index.fmp4.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",UR FANATİK TV
https://edge1.socialsmart.tv/urfanatiktv/bant1/chunks.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",UR FANATİK TV
https://live.artidijitalmedya.com/artidijital_urfanatiktv/urfanatiktv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",ÜSKÜDAR UNİVERSİTE TV
http://uskudarunv.mediatriple.net/uskudarunv/uskudar2/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",VAN GÖLÜ TV
https://cdn1-vangolutv.yayin.com.tr/vangolutv/amlst:vangolutv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",VİYANA TV
http://nrttn172.kesintisizyayin.com:29010/nrttn/nrttn/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",YAŞAM TV
https://yayin30.haber100.com/live/yasamtv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",WORLD TÜRK TV
https://live.artidijitalmedya.com/artidijital_worldturk/worldturk/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",YOZGAT BLD TV
https://cdn1-yozgatbeltv.yayin.com.tr/yozgatbeltv/yozgatbeltv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",YILDIZ TV
https://cdn-yildiz.yayin.com.tr/yildiz/yildiz/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",BRÜKSEL TÜRK
https://live.euromediacenter.com/brukselturk/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",BALKAN TÜRK
https://live.euromediacenter.com/balkanturktv/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",KANAL AVRUPA
http://cdn-kanalavrupa.yayin.com.tr/kanalavrupa/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",GURME TV
https://live.euromediacenter.com/gurmetv/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",EZGİ TV
https://live.euromediacenter.com/ezgitv/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mHt7rQf/Tryerel.png",*ESKİ TÜRKİYE* - NOSTALJİ TV KANALLAR...
https://github.com/ipstreet312/freeiptv/raw/master/ressources/infos/barkers/eskitrnost.ts
#EXTINF:-1 group-title="11. |TR|🇹🇷 YEREL - BÖLGESEL",--- |KKTC: KUZEY KIBRIS| ---
http://blank
#EXTINF:-1 tvg-logo="https://i.ibb.co/y8p46cM/Kktc.png",BRT 1
https://sc-kuzeykibrissmarttv.ercdn.net/brt1hd/bant1/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/y8p46cM/Kktc.png",BRT 1
https://spor.kuzeykibris.tv/m3u8/tv_brt1.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/y8p46cM/Kktc.png",BRT 2
https://sc-kuzeykibrissmarttv.ercdn.net/brt2hd/bant1/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/y8p46cM/Kktc.png",BRT 2
https://spor.kuzeykibris.tv/m3u8/tv_brt2.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/y8p46cM/Kktc.png",ADA TV
https://sc-kuzeykibrissmarttv.ercdn.net/adatv/bant1/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/y8p46cM/Kktc.png",ADA TV
https://spor.kuzeykibris.tv/m3u8/tv_ada.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/y8p46cM/Kktc.png",ADA TV
https://yayin1.canlitv.fun/live/kibrisadatv.stream/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/y8p46cM/Kktc.png",KANAL T
https://sc-kuzeykibrissmarttv.ercdn.net/kanalt/bantp1/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/y8p46cM/Kktc.png",KANAL T
https://spor.kuzeykibris.tv/m3u8/tv_kanalt.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/y8p46cM/Kktc.png",GENÇ TV
https://sc-kuzeykibrissmarttv.ercdn.net/kibrisgenctv/bant1/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/y8p46cM/Kktc.png",GENÇ TV
https://spor.kuzeykibris.tv/m3u8/tv_genc.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/y8p46cM/Kktc.png",KIBRIS TV
https://sc-kuzeykibrissmarttv.ercdn.net/kibristv/bant1/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/y8p46cM/Kktc.png",KIBRIS TV
https://spor.kuzeykibris.tv/m3u8/tv_ktv.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/y8p46cM/Kktc.png",SİM TV
https://sc-kuzeykibrissmarttv.ercdn.net/simtv/bantp1/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/y8p46cM/Kktc.png",SİM TV
https://spor.kuzeykibris.tv/m3u8/tv_sim.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/y8p46cM/Kktc.png",TV 2020
https://sc-kuzeykibrissmarttv.ercdn.net/tv2020/bantp1/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/y8p46cM/Kktc.png",TV 2020
https://spor.kuzeykibris.tv/m3u8/tv_2020.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/y8p46cM/Kktc.png",KK TV
http://old.kuzeykibris.tv/m3u8/kktv.m3u8
#EXTINF:-1 group-title="11. |TR|🇹🇷 YEREL - BÖLGESEL",--- |KURDÎ: SORANİ, ZAZA| ---
http://blank
#EXTINF:-1 tvg-logo="https://i.ibb.co/cXd3MBV/symkr.png",ZAROK KURMANÎ
https://zindikurmanci.zaroktv.com.tr/hls/stream.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/cXd3MBV/symkr.png",ZAROK SORANÎ
https://zindisorani.zaroktv.com.tr/hls/stream.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/cXd3MBV/symkr.png",ZAROK
https://iko-live.akamaized.net/ZarokTV/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/cXd3MBV/symkr.png",TRT KURDÎ
https://tv-trtkurdi.medya.trt.com.tr/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/cXd3MBV/symkr.png",ZAGROS TV
https://5a3ed7a72ed4b.streamlock.net/zagrostv/SMIL:myStream.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/cXd3MBV/symkr.png",KURDMAX SHOW
https://6476e46b58f91.streamlock.net/liveTrans/SHOW2/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/cXd3MBV/symkr.png",KURDMAX SORANÎ
https://6476e46b58f91.streamlock.net/liveTrans/KurdmaxS0rani!/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/cXd3MBV/symkr.png",KURDMAX MUSIC
https://6476e46b58f91.streamlock.net/music/livestream/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/cXd3MBV/symkr.png",RÛDAW TV
https://svs.itworkscdn.net/rudawlive/rudawlive.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/cXd3MBV/symkr.png",ROJAVA TV
https://iko-streamline-live1.akamaized.net/RojavaTV/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/cXd3MBV/symkr.png",KURD CHANNEL
https://kurd-channel.ikoflix.com/hls/stream_2.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/cXd3MBV/symkr.png",KURDISTAN 24
https://d1x82nydcxndze.cloudfront.net/live/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/cXd3MBV/symkr.png",KURDISTAN TV
https://5a3ed7a72ed4b.streamlock.net/live/SMIL:myStream.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/cXd3MBV/symkr.png",KURDSAT
https://kurdsat.akamaized.net/hls/kurdsat.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/cXd3MBV/symkr.png",KURDSAT
https://iko-live.akamaized.net/KurdsatTV/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/cXd3MBV/symkr.png",KURDSAT NEWS
https://kurdsat-news.akamaized.net/hls/kurdsat-news.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/cXd3MBV/symkr.png",KURDMAX MUSIC
https://6476e46b58f91.streamlock.net/music/livestream/chunklist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/cXd3MBV/symkr.png",GELÎ KURDISTAN TV
https://live.bradosti.net/live/GaliKurdistan/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/cXd3MBV/symkr.png",KOMALA TV
https://live.tvkomala.com/live/komala/chunks.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/cXd3MBV/symkr.png",JÎN TV
https://live.jintv.org/medialive/jintv.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/cXd3MBV/symkr.png",CÎHAN TV
http://cihan.dwasat.com/upload/images/cihanhd.m3u8


#EXTINF:-1 tvg-logo="https://i.ibb.co/vQZKgNX/ertworld.png" group-title="12. |GR|🇬🇷 GREECE Ελλά",ERT WORLD
https://ertflix.akamaized.net/ertlive/ertworld/default/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/qNZ259D/ertnews.png",ERT NEWS
https://ertflix.akamaized.net/ertlive/ertnews/default/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/kc1Dy1d/ertnews2.png",ERT NEWS 2
https://ertflix.akamaized.net/ertlive/ertnews2/default/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/kx3g5tM/ertnews3.png",ERT NEWS 3
https://ertflix.akamaized.net/ertlive/ertnews3/default/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/YDX83ph/ert1.png",ERT 1
https://ertflix.akamaized.net/ertlive/ert1/clrdef24723b/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/bL4sJLW/ert2.png",ERT 2
https://ertflix.akamaized.net/ertlive/ert2/clrdef24828z/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/BjHZT7x/ert3.png",ERT 3
https://ertflix.akamaized.net/ertlive/ert3/clrdef24828n/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/PGvP32M/ertsports1.png",ERT SPORTS 1
https://ertflix.akamaized.net/ertlive/ertsports1/clrdef24724a/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/HYMZh7V/ertsports2.png",ERT SPORTS 2
https://ertflix.akamaized.net/ertlive/ertsports2/clrdef24724b/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/pPkt9Yg/ertsports3.png",ERT SPORTS 3
https://ertflix.akamaized.net/ertlive/ertsports3/clrdef24724c/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/KYrkMLk/ertsports4.png",ERT SPORTS 4
https://ertflix.akamaized.net/ertlive/ertsports4/default/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/zbvFC65/ertkids.jpg",ERT KIDS
https://ertflix.akamaized.net/ertlive/kids/default/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/zbvFC65/ertkids.jpg",ERT KIDS
http://hbbtvapp.ert.gr/stream.php/v/vid_kidstv-hbbtv_mpeg.2ts
#EXTINF:-1 tvg-logo="https://i.ibb.co/c8NJjxh/ertmusic.jpg",ERT MUSIC
https://ertflix.akamaized.net/ertlive/music/default/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/c8NJjxh/ertmusic.jpg",ERT MUSIC
http://hbbtvapp.ert.gr/stream.php/v/vid_ertplay5_mpeg.2ts
#EXTINF:-1 tvg-logo="https://i.ibb.co/480p4sv/alpha.png",ALPHA TV
https://alphatvlive2.siliconweb.com/alphatvlive/live_abr/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/480p4sv/alpha.png",ALPHA TV
http://alphatvlive.siliconweb.com/1/Y2Rsd1lUcUVoajcv/UVdCN25h/hls/live/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/qk1SMGf/ant1.jpg",ANT 1
http://l2.cloudskep.com/ant1cm2/abr/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/qk1SMGf/ant1.jpg",ANT 1
http://mcdn.antennaplus.gr/live/media0/Ant1/HLS/Ant1.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/qk1SMGf/ant1.jpg",ANT 1
https://pcdn.antennaplus.gr/live/media0/antenna-gr/HLS/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/qk1SMGf/ant1.jpg",ANT 1
https://cdn1.smart-tv-data.com/live/ant1/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/qk1SMGf/ant1.jpg",ANT 1
https://d1nfykbwa3n98t.cloudfront.net/out/v1/6e5667da5a6843899a337dea72adb61b/antenna.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/df2r3NS/skai.jpg",SKAI
https://skai-live.siliconweb.com/media/cambria4/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/df2r3NS/skai.jpg",SKAI
https://skai-live-back.siliconweb.com/media/cambria4/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/PmDyTX6/star.jpg",STAR
https://livestar.siliconweb.com/starvod/star_int/star_int.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/PmDyTX6/star.jpg",STAR
https://livestar.siliconweb.com/media/star1/star1.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/PmDyTX6/star.jpg",STAR
https://livestar.siliconweb.com/media/star4/star4.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/PmDyTX6/star.jpg",STAR
http://telmaco-cdn.akamaized.net/starcgr/default/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/y6D9CPT/megagr.png",MEGA
http://c98db5952cb54b358365984178fb898a.msvdn.net/live/S14373792/aGr5KG7RcZ9a/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/y6D9CPT/megagr.png",MEGA
https://c98db5952cb54b358365984178fb898a.msvdn.net/live/S86713049/gonOwuUacAxM/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/y6D9CPT/megagr.png",MEGA
https://streamcdng16-c98db5952cb54b358365984178fb898a.msvdn.net/live/S14373792/aGr5KG7RcZ9a/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/y6D9CPT/megagr.png",MEGA
https://github.com/ipstreet312/freeiptv/raw/master/ressources/infos/barkers/megr.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/y6D9CPT/megagr.png",MEGA PLAY
https://c422e6f66e3a41029fa6cf83cab8b1d5.msvdn.net/live/S46747281/DJSPnDk0TaKs/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/y6D9CPT/megagr.png",MEGA PLAY
http://vid1.megatv-ctv.com/mega/megasport/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/ynxKwfdR/meganews.png",MEGA NEWS
https://c98db5952cb54b358365984178fb898a.msvdn.net/live/S99841657/NU0xOarAMJ5X/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/ynxKwfdR/meganews.png",MEGA NEWS
http://vid1.megatv-ctv.com/mega/meganews/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/B2Xxhty/mak.png",MAK TV
http://mcdn.antennaplus.gr/live/media0/MAK/HLS/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/B2Xxhty/mak.png",MAK TV
http://dlm34ll53zqql.cloudfront.net/out/v1/d4177931deff4c7ba994b8126d153d9f/maktv.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/B6hwDfS/netmax.jpg",NETMAX TV
https://live.netmaxtv.com:1936/live/live/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/8bgKVyb/openbyd.png",OPEN TV
https://liveopencloud.siliconweb.com/1/ZlRza2R6L2tFRnFJ/eWVLSlQx/hls/live/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/xq8t3P5/attica.jpg",ATTICA
http://atticatv.siliconweb.com/atticatv/atticaliveabr/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/sPtkhnL/sigma.png",SIGMA TV
https://sl2.sigmatv.com/hls/live.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/sPtkhnL/sigma.png",SIGMA TV
http://l10.cloudskep.com/sigmatv/stv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/txd3r3P/magic.png",MAGIC TV
https://itv.streams.ovh/magictv/magictv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Gs4djtL/makedonia.png",MAKEDONIA TV
https://dlm34ll53zqql.cloudfront.net/out/v1/d4177931deff4c7ba994b8126d153d9f/maktv_4.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tQmhZ0K/netmax.png",NET TV TORONTO
https://eu1.vectromdigital.com:1936/netvtoronto/netvtoronto/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tQmhZ0K/netmax.png",NET TV EUROPE
https://eu1.vectromdigital.com:1936/netveurope/netveurope/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tQmhZ0K/netmax.png",NET MAX TV
http://live.netmaxtv.com:8080/live/live/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/qk1SMGf/ant1.jpg" user-agent="VLC/3.0.20 LibVLC/3.0.20",ANT 1 COMEDY
http://mcdn.antennaplus.gr/live/media0/Comedy/HLS/Comedy.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/qk1SMGf/ant1.jpg",ANT 1 COMEDY
http://d2e65zbw2lm5c4.cloudfront.net/comedy_aws/abr/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/qk1SMGf/ant1.jpg" user-agent="VLC/3.0.20 LibVLC/3.0.20",ANT 1 DRAMA
http://mcdn.antennaplus.gr/live/media0/Drama/HLS/Drama.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/qk1SMGf/ant1.jpg",ANT 1 DRAMA
http://d2e65zbw2lm5c4.cloudfront.net/drama_aws/abr/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/qk1SMGf/ant1.jpg",ANT 1 MUSIC
http://mcdn.antennaplus.gr/live/media0/Just_Music/HLS/Just_Music.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/W5DZtvt/madtv.png",MAD WORLD
https://ellastvmax.better-than.tv/freetv/madworldtv/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/W5DZtvt/madtv.png",MAD WORLD
http://ellastv.gotdns.com:88/freetv/madworldtv/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/TPGzY4C/omega.png",OMEGA
https://l1.cloudskep.com/omegatv/omcy/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/3sHp7pS/riksat.png",RIK SAT CYPRUS
http://l3.cloudskep.com/cybcsat/abr/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/3sHp7pS/riksat.png",RIK 1
http://l6.cloudskep.com/rikct/rik1/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/3sHp7pS/riksat.png",RIK 2
http://l6.cloudskep.com/rikct/rik2/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/3sHp7pS/riksat.png",RIK HD
http://l6.cloudskep.com/rikct/rikhd/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/56kWP6F/action24.png",ACTION 24
https://actionlive.siliconweb.com/actionabr/actiontv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/1qXMwq2/groovy.png",GROOVY TV
http://web.onair-radio.eu:1935/groovytv/groovytv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/3m2fYyYw/skaibb.jpg",SKAI BIG BROTHER
https://cdn1.smart-tv-data.com/skai/skaiBB/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/0DDXv93/nea.png",NEA CRETE TV
https://live.neatv.gr:8888/hls/neatv_high/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/b2mBMBk/baraza.jpg",BARAZA RELAXING TV
https://rtmp.streams.ovh:1936/barazarelax/barazarelax/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/72657Kw/xalastra.jpg",XALASTRA TV
https://live.cast-control.eu:443/xalastratv/xalastratv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/z6zPQL8/nrg.png",NRG TV
http://tv.nrg91.gr:1935/onweb/live/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/L9fj1Hj/greece.png",BOYAH TV - KANALI VOULIS
http://streamer-cache.grnet.gr/parliament/hls/webtv.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/L9fj1Hj/greece.png",BOYAH TV - KANALI VOULIS
https://streamer-cache.grnet.gr/parliament/parltv.sdp/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/L9fj1Hj/greece.png",AEOLOS
https://cdn.istoikona.com/aeolostv/live/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/L9fj1Hj/greece.png",EXPLORE
http://web.onair-radio.eu:1935/explorecy/explorecy/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/L9fj1Hj/greece.png",TOP CHANNEL
http://eu1.vectromdigital.com:1935/topchannel/topchannel/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/L9fj1Hj/greece.png",ράκη Νετ TV
https://cdn.onestreaming.com/thrakinettv/thrakinettv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/L9fj1Hj/greece.png",TELE ΚΡΗΤΗ
https://neon.streams.gr:8081/telekriti/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/L9fj1Hj/greece.png",START TV
https://live.cast-control.eu/StartMedia/StartMedia/playlist.m3u8
##EXTINF:-1 tvg-logo="https://i.ibb.co/L9fj1Hj/greece.png",PELLA TV
https://video.streams.ovh:1936/pellatv/pellatv/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/L9fj1Hj/greece.png",KONTRA TV
http://kontralive.siliconweb.com/live/kontratv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/L9fj1Hj/greece.png",HIGH TV
http://live.streams.ovh:1935/hightv/hightv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/L9fj1Hj/greece.png",HELLENIC TV
https://l5.cloudskep.com/hellenictv/htv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/L9fj1Hj/greece.png",GREEK TV LONDON
https://vdo.streams.gr:3125/live/greektvlondonlive.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/L9fj1Hj/greece.png",GRD CHANNEL
https://live.cast-control.eu:443/organismos/organismos/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/L9fj1Hj/greece.png",CRETA
http://live.streams.ovh:1935/tvcreta/tvcreta/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/L9fj1Hj/greece.png",CORFU
https://itv.streams.ovh/corfuchannel/corfuchannel/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/L9fj1Hj/greece.png",BLUE SKY
https://cdn5.smart-tv-data.com/bluesky/bluesky-live/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/L9fj1Hj/greece.png",RED MUSIC
https://fr.crystalweb.net:1936/redmusic/redmusic/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/L9fj1Hj/greece.png",BARAZA TV
https://eco.streams.ovh:8081/barazatv/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/L9fj1Hj/greece.png",10 CHANNEL
https://castor.streamthatvideo.co:8081/10channel/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/vQZKgNX/ertworld.png",ERT WORLD (backup)
https://ertflix.akamaized.net/ertlive/ertworld/default/index.mpd
#EXTINF:-1 tvg-logo="https://i.ibb.co/vQZKgNX/ertworld.png",ERT WORLD (backup)
http://hbbtvapp.ert.gr/stream.php/v/vid_ertworld_mpeg.2ts
#EXTINF:-1 tvg-logo="https://i.ibb.co/vQZKgNX/ertworld.png",ERT WORLD (backup)
http://hbbtv.ert.gr/stream.php/v/vid_ertworld_mpeg.2ts
#EXTINF:-1 tvg-logo="https://i.ibb.co/qNZ259D/ertnews.png",ERT NEWS (backup)
https://ertflix.akamaized.net/ertlive/ertnews/default/index.mpd
#EXTINF:-1 tvg-logo="https://i.ibb.co/qNZ259D/ertnews.png",ERT NEWS (backup)
http://hbbtvapp.ert.gr/stream.php/v/vid_ertnews_mpeg.2ts
#EXTINF:-1 tvg-logo="https://i.ibb.co/PGvP32M/ertsports1.png",ERT SPORTS 1 (backup)
https://ertflix.akamaized.net/ertlive/ertsports1/clrdef24724a/index.mpd
#EXTINF:-1 tvg-logo="https://i.ibb.co/PGvP32M/ertsports1.png",ERT SPORTS 1 (backup)
http://hbbtvapp.ert.gr/stream.php/v/vid_ertsports_mpeg.2ts
#EXTINF:-1 tvg-logo="https://i.ibb.co/HYMZh7V/ertsports2.png",ERT SPORTS 2 (backup)
http://hbbtvapp.ert.gr/stream.php/v/vid_ertplay2_mpeg.2ts
#EXTINF:-1 tvg-logo="https://i.ibb.co/pPkt9Yg/ertsports3.png",ERT SPORTS 3 (backup)
http://hbbtvapp.ert.gr/stream.php/v/vid_ertplay3_mpeg.2ts
#EXTINF:-1 tvg-logo="https://i.ibb.co/KYrkMLk/ertsports4.png",ERT SPORTS 4 (backup)
http://hbbtv.ert.gr/stream.php/v/vid_ertplay4_mpeg.2ts
#EXTINF:-1 tvg-logo="https://i.ibb.co/c8NJjxh/ertmusic.jpg",ERT MUSIC (backup)
http://hbbtv.ert.gr/stream.php/v/vid_ertplay5_mpeg.2ts
#EXTINF:-1 tvg-logo="https://i.ibb.co/zbvFC65/ertkids.jpg",ERT KIDS (backup)
http://hbbtv.ert.gr/stream.php/v/vid_kidstv-hbbtv_mpeg.2ts
#EXTINF:-1 tvg-logo="https://i.ibb.co/3sHp7pS/riksat.png",RIK SAT CYPRUS (backup)
https://ertflix.akamaized.net/ertlive/rik/default/playlist.m3u8

#EXTINF:-1 tvg-logo="https://i.ibb.co/pyXp0bk/tvi.png" group-title="13. |PT|🇵🇹 PORTUGAL",TVI
https://raw.githubusercontent.com/ipstreet312/freeiptv/master/ressources/tvipt/sh/tvi.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/6r1xHn6/sic.png",SIC
https://d1zx6l1dn8vaj5.cloudfront.net/out/v1/b89cc37caa6d418eb423cf092a2ef970/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/SPR2SDK/RTP.png" user-agent="VLC/3.0.20 LibVLC/3.0.20",RTP INTERNACIONAL
https://raw.githubusercontent.com/ipstreet312/freeiptv/refs/heads/master/ressources/tvipt/py/rtp_internacional.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/SPR2SDK/RTP.png",RTP INTERNACIONAL
http://78.128.125.60:9981/play/a00k/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/XbSHxd5/cnn.png",CNN PORTUGAL
https://raw.githubusercontent.com/ipstreet312/freeiptv/master/ressources/tvipt/sh/cnnpt.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/1QHfvZJ/sicnoc.png",SIC NOTÍCIAS
https://cdnapisec.kaltura.com/p/4526593/sp/4526593/playManifest/entryId/1_j8ztwihx/deliveryProfileId/672/protocol/https/format/applehttp/a.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/HnqCkQj/rtp3.jpg" user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0",RTP 3 NOTÍCIAS
https://raw.githubusercontent.com/ipstreet312/freeiptv/refs/heads/master/ressources/tvipt/py/rtp_3.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/VxLFYSj/euronews.png",EURONEWS PT
https://euronews-live-por-pt.fast.rakuten.tv/v1/master/0547f18649bd788bec7b67b746e47670f558b6b2/production-LiveChannel-6572/bitok/e/26035/euronews-pt.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/pyXp0bk/tvi.png",TVI INT
https://raw.githubusercontent.com/ipstreet312/freeiptv/master/ressources/tvipt/sh/tviint.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/gDFmb2z/vplustvi.png",TVI V+
https://video-auth2.iol.pt/live_vmais/live_vmais/edge_servers/vmais-720p/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/hg8wkqj/tvific.jpg",TVI FICCAO
https://video-auth1.iol.pt/live_tvi_ficcao/live_tvi_ficcao/edge_servers/tvificcao-720p/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/xYNTr2v/tvirea.jpg",TVI REALITY
https://video-auth4.iol.pt/live_tvi_reality/live_tvi_reality/edge_servers/tvireality-720_passthrough/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/dJZR1gD/sicnov.png",SIC NOVELAS
https://production-fast-sic.content.okast.tv/fa2e8c4385712f9ae705b449477523ec/channels/d9070446-8448-455e-8075-773b1ba12562/f083c6ea-33af-458e-82c5-f27f6b42f9ec/media_.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/W2dzvHS/sicreplay.png",SIC REPLAY
https://production-fast-sic.content.okast.tv/fa2e8c4385712f9a7dce4ff2dcebac2e/channels/d9070446-8448-455e-8075-773b1ba12562/d47eae0f-ad77-414a-9a1d-2a6628ba18c3/media_.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/M2g53rQ/sichdad.png",SIC HD ALTA DEFINIÇÃO
https://production-fast-sic.content.okast.tv/fa2e8c4385712f9aa54bbe52b1bd9b6b/channels/d9070446-8448-455e-8075-773b1ba12562/fc831b20-f252-4e7d-8cc5-2d05f4d43c1c/media_.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/WVzhVbc/portoc.png",PORTO CANAL
https://pull-live-156-1.global.ssl.fastly.net/pc5865dc25400thmb-ea6bf03b14fa318f7133/smil:pc1-jhrgyuoqe5865db-68tkgb14fa318f7133f03.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/vvRXDTV/tviafrica.jpg",TVI AFRICA
https://video-auth4.iol.pt/live_tvi_africa/live_tvi_africa/edge_servers/tviafrica-480p/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/zZwMM3d/arparl.png",AR PARLAMENTO
https://playout175.livextend.cloud/livenlin4/_definst_/2liveartvpub2/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/V3Hk3KC/adb.png",ADB TV
https://streamer-a03.videos.sapo.pt/live/sobrenaturaltv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/DCzRYjV/mca.png",MCA
https://video-auth2.iol.pt/live_hd2/live_hd2/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/RpQj4Dd/fama.png",FAMA FM TV
https://tv2.fastcast4u.com:3310/live/famatvlive.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/cX8tGgsv/Kuriakos.png",KURIAKOS TV
https://w1.manasat.com/ktv/smil:ktv.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/KxXJddKf/Kuriakosmsc.png",KURIAKOS MUSIC
https://w2.manasat.com/kmusic/smil:kmusic.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/TcpshFx/kuricine.png",KURIAKOS CINE
https://w2.manasat.com/kcine/smil:kcine.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/B2YCsC0/kurikids.png",KURIAKOS KIDS
https://w2.manasat.com/kkids/smil:kkids.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/fk0Vttj/tracebraz.png",TRACE BRAZUCA
https://d35j504z0x2vu2.cloudfront.net/v1/master/0bc8e8376bd8417a1b6761138aa41c26c7309312/trace-brazuca/encrypted.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/fk0Vttj/tracebraz.png",TRACE BRAZUCA
https://d25usgadhphvwi.cloudfront.net/v1/master/3722c60a815c199d9c0ef36c5b73da68a62b09d1/cc-ccfvktkgxl5qg/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/3YZFCjp/rtp1.jpg",RTP 1 (backup sd)
https://streaming-live.rtp.pt/liverepeater/rtp1.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tbFT1V2/rtp2.jpg",RTP 2 (backup sd)
https://streaming-live.rtp.pt/liverepeater/rtp2.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/HnqCkQj/rtp3.jpg",RTP 3 (backup sd)
https://streaming-live.rtp.pt/liverepeater/rtpn.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/HnqCkQj/rtp3.jpg",RTP 3 (tvhlsdvr)
https://streaming-live.rtp.pt/livetvhlsDVR/rtpndvr.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/HnqCkQj/rtp3.jpg",RTP 3 (tvhlsdvr_HD)
https://streaming-live.rtp.pt/livetvhlsDVR/rtpnHDdvr.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/9GMzcw7/rtpaco.jpg",RTP ACORES (backup)
https://streaming-live.rtp.pt/liverepeater/rtpacoresHD.smil/chunklist_b640000_slpor.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/SPR2SDK/RTP.png" user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0" referer="https://www.rtp.pt/play/direto/rtpinternacional",RTP I (noott)
https://streaming-live.rtp.pt/liverepeater/smil:rtpi.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/3YZFCjp/rtp1.jpg" user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0" referer="https://www.rtp.pt/play/direto/rtp1",RTP 1 (noott)
https://streaming-live.rtp.pt/liverepeater/smil:rtpClean1HD.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/3YZFCjp/rtp1.jpg" user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0" referer="https://www.rtp.pt/play/direto/rtp1",RTP 1 (noott)
https://streaming-live.rtp.pt/liverepeater/rtp1HD.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tbFT1V2/rtp2.jpg" user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0" referer="https://www.rtp.pt/play/direto/rtp2",RTP 2 (noott)
https://streaming-live.rtp.pt/liverepeater/smil:rtpClean2HD.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tbFT1V2/rtp2.jpg" user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0" referer="https://www.rtp.pt/play/direto/rtp2",RTP 2 (noott)
https://streaming-live.rtp.pt/liverepeater/rtp2HD.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/HnqCkQj/rtp3.jpg" user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0" referer="https://www.rtp.pt/play/direto/rtp3",RTP 3 (noott)
https://streaming-live.rtp.pt/liverepeater/rtpnHD.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/HnqCkQj/rtp3.jpg" user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0" referer="https://www.rtp.pt/play/direto/rtp3",RTP 3 (noott)
https://streaming-live.rtp.pt/livetvhlsDVR/rtpnHDdvr.smil/playlist.m3u8?DVR
#EXTINF:-1 tvg-logo="https://i.ibb.co/3YZFCjp/rtp1.jpg" user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0" referer="https://www.rtp.pt/play/direto/rtp1",RTP 1 (backup)
https://streaming-live.rtp.pt/liverepeater/rtpClean1HD.smil/manifest.mpd
#EXTINF:-1 tvg-logo="https://i.ibb.co/tbFT1V2/rtp2.jpg" user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0" referer="https://www.rtp.pt/play/direto/rtp2",RTP 2 (backup)
https://streaming-live.rtp.pt/liverepeater/rtpClean2HD.smil/manifest.mpd
#EXTINF:-1 tvg-logo="https://i.ibb.co/BsdgH54/rtpafr.webp" user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64)" referer="https://www.rtp.pt/play/direto",RTP AFRICA (noott)
https://streaming-live.rtp.pt/liverepeater/rtpafrica.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/9GMzcw7/rtpaco.jpg" user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64)" referer="https://www.rtp.pt/play/direto",RTP ACORES (noott)
https://streaming-live.rtp.pt/liverepeater/rtpacores.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/bvwwcB9/rtpmad.jpg" user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64)" referer="https://www.rtp.pt/play/direto",RTP MADEIRA (noott)
https://streaming-live.rtp.pt/liverepeater/rtpmadeira.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/vZ9S4rV/rtpmem.jpg" user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64)" referer="https://www.rtp.pt/play/direto",RTP MEMORIA (noott)
https://streaming-live.rtp.pt/liverepeater/rtpmem.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/VxLFYSj/euronews.png",EURONEWS PT (backup)
https://rakuten-euronews-8-pt.samsung.wurl.tv/manifest/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/VxLFYSj/euronews.png",EURONEWS PT (backup)
https://7c8b7dbf12d64234a983336fdddb88c2.mediatailor.us-east-1.amazonaws.com/v1/master/44f73ba4d03e9607dcd9bebdcb8494d86964f1d8/Samsung-pt_EuroNewsLive/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/VxLFYSj/euronews.png",EURONEWS PT (backup)
https://0ff3c09c7580460e8e018cdcaacbadee.mediatailor.us-east-1.amazonaws.com/v1/master/44f73ba4d03e9607dcd9bebdcb8494d86964f1d8/RakutenTV-pt_EuroNewsLive/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/VxLFYSj/euronews.png",EURONEWS PT (backup)
https://7c8b7dbf12d64234a983336fdddb88c2.mediatailor.us-east-1.amazonaws.com/v1/master/44f73ba4d03e9607dcd9bebdcb8494d86964f1d8/Samsung-pt_EuroNewsLive/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/VxLFYSj/euronews.png",EURONEWS PT (backup)
http://stitcher-ipv4.pluto.tv/v1/stitch/embed/hls/channel/619e6614c9d9650007a2b171livestitch/master.m3u8?deviceDNT=%7BTARGETOPT%7D&deviceModel=samsung&deviceVersion=unknown&appVersion=unknown&deviceType=samsung-tvplus&deviceMake=samsung
#EXTINF:-1 tvg-logo="https://i.ibb.co/XbSHxd5/cnn.png",CNN PORTUGAL (backup)
https://sktv-forwarders.7m.pl/get.php?x=CNN_Portugal&m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/1QHfvZJ/sicnoc.png",SIC NOTÍCIAS (backup)
https://d277k9d1h9dro4.cloudfront.net/out/v1/293e7c3464824cbd8818ab8e49dc5fe9/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/dJZR1gD/sicnov.png",SIC NOVELAS (backup)
https://fast.live.impresa.pt/out/v1/b5be42c4a68d4ee18461a7156bb8ecf2/sic-novelas.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/gDFmb2z/vplustvi.png",TVI V+ (ex-TVI FICCAO)
https://video-auth2.iol.pt/live_tvi_ficcao/live_tvi_ficcao/edge_servers/tvificcao-720p/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/1QHfvZJ/sicnoc.png" referer="https://sic.pt/",SIC NOTÍCIAS (backup)
https://sicnot.live.impresa.pt/sicnot.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/6r1xHn6/sic.png" referer="https://sic.pt/",SIC OPT. (backup)
https://eventos.live.impresa.pt/opto_in1.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/dJZR1gD/sicnov.png" referer="https://sic.pt/",SIC NOVELAS (backup)
https://eventos.live.impresa.pt/opto_in2.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/6r1xHn6/sic.png" referer="https://sic.pt/",SIC [offline]
https://sic.live.impresa.pt/sic.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/6r1xHn6/sic.png" referer="https://sic.pt/",SIC INT [offline]
https://sic.live.impresa.pt/live/sicint/sicint.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/XbSHxd5/cnn.png",CNN PORTUGAL [find-host]
https://PuthereYourserverHostaddress/cnnpcurlua.php?m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/pyXp0bk/tvi.png",TVI [find-host]
https://PuthereYourserverHostaddress/tvicurlua.php?m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/pyXp0bk/tvi.png",TVI INT [find-host]
https://PuthereYourserverHostaddress/tviintcurlua.php?m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/XbSHxd5/cnn.png",CNN PORTUGAL [tkn-blocked]
https://video-auth7.iol.pt/edge_servers/cnn-720p/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/pyXp0bk/tvi.png",TVI [tkn-blocked]
https://video-auth2.iol.pt/edge_servers/tvi-720_passthrough/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/pyXp0bk/tvi.png",TVI INT [tkn-blocked]
https://video-auth6.iol.pt/edge_servers/tviinternacional-720p/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/hg8wkqj/tvific.jpg",TVI FICCAO [tkn-blocked]
https://video-auth6.iol.pt/live_tvi_ficcao/live_tvi_ficcao/playlist.m3u8?wmsAuthSign=
#EXTINF:-1 tvg-logo="https://i.ibb.co/hg8wkqj/tvific.jpg",TVI FICCAO [tkn-blocked]
https://video-auth2.iol.pt/edge_servers/tvificcao-720p/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/xYNTr2v/tvirea.jpg",TVI REALITY [tkn-blocked]
https://video-auth6.iol.pt/live_tvi_reality/live_tvi_reality/playlist.m3u8?wmsAuthSign=
#EXTINF:-1 tvg-logo="https://i.ibb.co/xYNTr2v/tvirea.jpg",TVI REALITY [tkn-blocked]
https://video-auth4.iol.pt/live_tvi_direct/live_tvi_direct/edge_servers/tvireality-720_passthrough/playlist.m3u8?wmsAuthSign=
#EXTINF:-1 tvg-logo="https://i.ibb.co/xYNTr2v/tvirea.jpg",TVI REALITY [tkn-blocked]
https://video-auth2.iol.pt/edge_servers/tvireality-720_passthrough/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/dJZR1gD/sicnov.png",SIC NOVELAS [offline]
https://cdnapisec.kaltura.com/p/4526593/sp/4526593/playManifest/entryId/1_kfaion7y/deliveryProfileId/672/protocol/https/format/applehttp/a.m3u8


#EXTINF:-1 tvg-logo="https://i.ibb.co/ypn5DBD/tveint.png" group-title="14. |ES|🇪🇸 ESPAÑA",TVE INTERNACIONAL
https://rtvelivestream-rtveplayplus.rtve.es/rtvesec/int/tvei_eu_main_720.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/ypn5DBD/tveint.png",TVE INTERNACIONAL
https://rtvelivestream.akamaized.net/rtvesec/int/tvei_eu_main.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/VM5vGBV/la1.jpg",TVE LA 1
https://ztnr.rtve.es/ztnr/1688877.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/VM5vGBV/la1.jpg",TVE LA 1
https://dh6vo1bovy43s.cloudfront.net/La_1_ES.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/ssGmhbH/la2.jpg",TVE LA 2
https://ztnr.rtve.es/ztnr/1688885.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/ssGmhbH/la2.jpg",TVE LA 2
https://di2qeq48iv8ps.cloudfront.net/La_2_ES.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/fqg1vfr/24h.png",TVE 24 H
https://ztnr.rtve.es/ztnr/1694255.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/fqg1vfr/24h.png",TVE 24 H
https://d3pfmk89wc0vm9.cloudfront.net/24H_ES.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/3T2TS2p/tvestar.jpg",STAR TVE
https://rtvelivestream.akamaized.net/rtvesec/int/star_main.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/3T2TS2p/tvestar.jpg",STAR TVE
https://rtvelivestream-rtveplayplus.rtve.es/rtvesec/int/star_main_720.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/D1Djbfj/tdp.jpg",TVE TDP
https://d2a02gfcid1k4a.cloudfront.net/Teledeporte_ES.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/D1Djbfj/tdp.jpg",TVE TDP
https://ztnr.rtve.es/ztnr/1712295.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/BGy5vM5/clan.jpg",TVE CLAN
https://d3nnqrdb77sy13.cloudfront.net/Clan_ES.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/BGy5vM5/clan.jpg",TVE CLAN
https://ztnr.rtve.es/ztnr/5466990.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/hYTkm8L/A3es.png",ANTENA 3
https://tvnoov.com/fadoo/antena3.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/hYTkm8L/A3es.png",ANTENA 3
https://gitlab.com/movrey/movrel/-/raw/main/antena3.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/hRs6WrH/C4es.png",CUATRO
https://tvnoov.com/fadoo/cuatrohd.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/hRs6WrH/C4es.png",CUATRO
https://gitlab.com/movrey/movrel/-/raw/main/cuatro.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/7gMg1nb/t5es.png",TELECINCO
https://tvnoov.com/fadoo/telecincohd.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/7gMg1nb/t5es.png",TELECINCO
https://gitlab.com/movrey/movrel/-/raw/main/telecinco.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/6JF4BK4/l6es.png",LA SEXTA
https://tvnoov.com/fadoo/lasexta.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/6JF4BK4/l6es.png",LA SEXTA
https://gitlab.com/movrey/movrel/-/raw/main/sexta.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/99kVf9W/somoscine.png",TVE SOMOS CINE [geo-limited]
https://ztnr.rtve.es/ztnr/5836726.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/99kVf9W/somoscine.png",TVE SOMOS CINE [geo-limited]
https://ztnr.rtve.es/ztnr/6909845.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/SRbKtLk/rtve.png",RNE PARA TODOS
https://ztnr.rtve.es/ztnr/6688753.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/SRbKtLk/rtve.png",RNE PARA TODOS
https://rtvelivestream.akamaized.net/rtvesec/rne/rne_para_todos_main.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/SRbKtLk/rtve.png",RTVE PLAY CADENA 1
https://ztnr.rtve.es/ztnr/6108696.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/SRbKtLk/rtve.png",RTVE PLAY CADENA 2
https://ztnr.rtve.es/ztnr/6108703.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/SRbKtLk/rtve.png",RTVE PLAY CADENA 3
https://ztnr.rtve.es/ztnr/6108704.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/SRbKtLk/rtve.png",RTVE PLAY CADENA 4
https://ztnr.rtve.es/ztnr/6108720.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/SRbKtLk/rtve.png",RTVE
https://ztnr.rtve.es/ztnr/5562351.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/SRbKtLk/rtve.png",RTVE
https://rtvelivestream.akamaized.net/hls/nxrtgolumi/mastdp/stream1.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/VxLFYSj/euronews.png",EURONEWS ES
https://euronews-live-spa-es.fast.rakuten.tv/v1/master/0547f18649bd788bec7b67b746e47670f558b6b2/production-LiveChannel-6571/bitok/e/26034/euronews-es.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/VxLFYSj/euronews.png",EURONEWS ES
https://39997b2f529e4793961899e546833a75.mediatailor.us-east-1.amazonaws.com/v1/master/44f73ba4d03e9607dcd9bebdcb8494d86964f1d8/Samsung-es_EuroNewsLive/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/cQwqfFC/ees.jpg",EL PAIS
https://d2xqbi89ghm9hh.cloudfront.net/v1/master/3722c60a815c199d9c0ef36c5b73da68a62b09d1/cc-79fx3huimw4xc-ssai-prd/fast-channel-el-pais.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/cQwqfFC/ees.jpg",EL PAIS
https://d2uerfl96fh0y6.cloudfront.net/v1/master/3722c60a815c199d9c0ef36c5b73da68a62b09d1/cc-98b4w85lugvp4/fast-channel-el-pais/fast-channel-el-pais.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tMVTj53/elconf.jpg",EL CONFIDENCIAL TV
https://daqnsnf5phf17.cloudfront.net/v1/master/3722c60a815c199d9c0ef36c5b73da68a62b09d1/cc-sde7fypd1420w-prod/fast-channel-elconfidencial/fast-channel-elconfidencial.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/8xh76zN/parl.jpg",CANAL PARLAMENTO
https://congresodirecto.akamaized.net/hls/live/2037973/canalparlamento/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/8xh76zN/parl.jpg",CANAL DIPUTADOS
https://congresodirecto.akamaized.net/hls/live/2038274/canal1/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/TthjhJ6/solmusica.png",SOL MÙSICA
https://d2glyu450vvghm.cloudfront.net/v1/master/3722c60a815c199d9c0ef36c5b73da68a62b09d1/cc-21u4g5cjglv02/sm.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/GsLm5g5/trece.png",TRECE INT
https://5940924978228.streamlock.net/8009/ngrp:8009_all/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/GsLm5g5/trece.png",TRECE
https://play.cdn.enetres.net/091DB7AFBD77442B9BA2F141DCC182F5021/021/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/GsLm5g5/trece.png",TRECE
https://play.cdn.enetres.net/091DB7AFBD77442B9BA2F141DCC182F5021/live.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/GsLm5g5/trece.png",TRECE
https://live-edge-ff-1.cdn.enetres.net/091DB7AFBD77442B9BA2F141DCC182F5021/liveld/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/bKLFcnD/a3cine.png",ATRES SERIES
http://181.78.109.48:8000/play/a00l/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/bKLFcnD/a3cine.png",ATRES SERIES
http://nodep002.service.openstream.es/SVoriginOperatorEdge2/smil:10_HD.smil/manifest.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/h17Kt3g/fastatres.jpg",ATRES CLÁSICOS
https://fast-channels.atresmedia.com/648ef12c2bfab0e4507e0d61/648ef12c2bfab0e4507e0d61.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/h17Kt3g/fastatres.jpg",ATRES COMEDIA
https://fast-channels.atresmedia.com/648ef23d2bfab0e4557e0d61/648ef23d2bfab0e4557e0d61.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/h17Kt3g/fastatres.jpg",ATRES FLOOXER
https://fast-channels.atresmedia.com/5c1285e47ed1a861f8125285/5c1285e47ed1a861f8125285.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/h17Kt3g/fastatres.jpg",ATRES MULTICINE
https://fast-channels.atresmedia.com/648ef18c1756b0e41daf83cc/648ef18c1756b0e41daf83cc.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/h17Kt3g/fastatres.jpg",ATRES KIDZ
https://fast-channels.atresmedia.com/648c271d2bfab0e4177a0d61/648c271d2bfab0e4177a0d61.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/h17Kt3g/fastatres.jpg",ATRES INQUIETOS
https://fast-channels.atresmedia.com/648ef3162bfab0e4587e0d61/648ef3162bfab0e4587e0d61.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/GJ3Qw6b/peque.jpg",PEQUE TV
https://canadaremar2.todostreaming.es/live/peque-pequetv.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Zxd0j45/cartoonnetwork.png",CARTOON NETWORK ES
https://playout.cdn.cartoonnetwork.com.br/playout_02/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Zxd0j45/cartoonnetwork.png",CARTOON NETWORK ES
https://playout.cdn.cartoonnetwork.com.br/playout_04/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/nLcKDkX/ddrama.png",VIVE KANAL D DRAMA
https://cdn-uw2-prod.tsv2.amagi.tv/linear/amg01602-themahqfrance-vivekanald-samsungspain/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/nLcKDkX/ddrama.png",VIVE KANAL D DRAMA
https://amg01602-themahqfrance-vivekanald-samsungspain-uu2zn.amagi.tv/playlist/amg01602-themahqfrance-vivekanald-samsungspain/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/vvhRkHZ/tracelatina.png",TRACE LATINA
https://cdn-uw2-prod.tsv2.amagi.tv/linear/amg01131-tracetv-tracelatinaes-samsungspain/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/vvhRkHZ/tracelatina.png",TRACE LATINA
https://d3b13j525hja2q.cloudfront.net/23073/Latina/encrypted/4/prog_index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/vvhRkHZ/tracelatina.png",TRACE LATINA
https://d35j504z0x2vu2.cloudfront.net/v1/master/0bc8e8376bd8417a1b6761138aa41c26c7309312/trace-latina/encrypted.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/bNm7D0p/rlmdrd.png",REAL MADRID CINEVERSE
https://cdn-uw2-prod.tsv2.amagi.tv/linear/amg01201-cinedigmenterta-realmadrid-cineverse/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/bNm7D0p/rlmdrd.png",REAL MADRID TV
https://stitcher-ipv4.pluto.tv/v1/stitch/embed/hls/channel/65f96cd34e01740008ef1c97livestitch/master.m3u8?deviceDNT=%7BTARGETOPT%7D&deviceModel=samsung&deviceVersion=unknown&appVersion=unknown&deviceType=samsung-tvplus&deviceMake=samsung
#EXTINF:-1 tvg-logo="https://i.ibb.co/bNm7D0p/rlmdrd.png",REAL MADRID TV
https://stitcher-ipv4.pluto.tv/v1/stitch/embed/hls/channel/65f96c0c2873090008d356d1livestitch/master.m3u8?deviceDNT=%7BTARGETOPT%7D&deviceModel=samsung&deviceVersion=unknown&appVersion=unknown&deviceType=samsung-tvplus&deviceMake=samsung
#EXTINF:-1 tvg-logo="https://i.ibb.co/bNm7D0p/rlmdrd.png",REAL MADRID TV
https://rmtv-canela.amagi.tv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/NLVj121/eltoro.png",EL TORO TV
https://streaming-1.eltorotv.com/lb0/eltorotv-streaming-web/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Qb7LPVN/andartv.png",SUR 1 ANDALUCÍA
https://cdnlive.codev8.net/rtvalive/smil:DtRLVjt1.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Qb7LPVN/andartv.png",SUR 1 ANDALUCÍA
https://d3kph49ozqk4tr.cloudfront.net/out/v1/b9781dec66d64d5f975b398c31f371db/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Qb7LPVN/andartv.png",SUR 1 ANDALUCÍA
https://d35x6iaiw8f75z.cloudfront.net/v1/master/3722c60a815c199d9c0ef36c5b73da68a62b09d1/cc-kbwsl0jk1bvoo/canal_sur_andalucia_es.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Qb7LPVN/andartv.png",SUR 1 ANDALUCÍA
https://live-24-canalsur.interactvty.pro/9bb0f4edcb8946e79f5017ddca6c02b0/26af5488cda642ed2eddd27a6328c93b9c03e9181b9d0a825147a7d978e69202.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Pt5ThHQ/andatv.png",SUR 2 ANDALUCÍA
https://cdnlive.codev8.net/rtvalive/channel22.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/gWcDxx9/csnan.png",SUR NOTICIAS ANDALUCÍA
https://cdnlive.codev8.net/rtvalive/smil:channel42.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/0Q8h8MG/andacine.png",CINE ANDALUCÍA
https://cdnlive.codev8.net/rtvalive/smil:channel24.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/LrnwFnz/andacocina.png",COCINA ANDALUCÍA
https://cloud.fastchannel.es/mic/manifiest/hls/acocina/acocina.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/hHKKnt3/andaturismo.png",TURISMO ANDALUCÍA
https://cloud.fastchannel.es/mic/manifiest/hls/aturismo/aturismo.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/MkBCwH4/arag.png",ARAGÓN TV
https://cartv.streaming.aranova.es/hls/live/aragontv_canal1.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/B4RNJb6/aragonot.jpg",ARAGÓN NOTICIAS
https://cartv-streaming.aranova.es/hls/live/anoticias_canal3.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/VM5vGBV/la1.jpg",LA 1 CANARIAS
https://ztnr.rtve.es/ztnr/5190066.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/ssGmhbH/la2.jpg",LA 2 CANARIAS
https://ztnr.rtve.es/ztnr/5468585.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/fqg1vfr/24h.png",24 H CANARIAS
https://ztnr.rtve.es/ztnr/5473142.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/N7tznnD/cmm.jpg",CASTILLA MEDIA
https://cdnapisec.kaltura.com/p/2288691/sp/228869100/playManifest/entryId/1_sqa9madm/format/applehttp/.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/VM5vGBV/la1.jpg",LA 1 CATALUNYA
https://ztnr.rtve.es/ztnr/3293681.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/ssGmhbH/la2.jpg",LA 2 CATALUNYA
https://ztnr.rtve.es/ztnr/3987218.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/fqg1vfr/24h.png",24 H CATALUNYA
https://ztnr.rtve.es/ztnr/4952053.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/xmGNS4w/tvcata.jpg",TV3 CATALUNYA INT
https://directes3-tv-int.3catdirectes.cat/live-content/tvi-hls/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/xmGNS4w/tvcata.jpg",TV3 CATALUNYA INT
https://directes-tv-int.3catdirectes.cat/live-origin/tvi-hls/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/xmGNS4w/tvcata.jpg",TV3 CATALUNYA CAT
https://directes-tv-cat.3catdirectes.cat/live-origin/tvi-hls/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/xmGNS4w/tvcata.jpg",TV3 CATALUNYA ES
https://directes-tv-es.3catdirectes.cat/live-origin/tvi-hls/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/xmGNS4w/tvcata.jpg",TV3 CATALUNYA 24H
https://directes-tv-int.3catdirectes.cat/live-content/canal324-hls/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/xmGNS4w/tvcata.jpg",TV3 CATALUNYA 24H
https://directes-tv-int.3catdirectes.cat/live-origin/canal324-hls/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/xmGNS4w/tvcata.jpg",TV3 CATALUNYA FAST 1
https://fast-tailor.3catdirectes.cat/v1/channel/ccma-channel1/hls.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/xmGNS4w/tvcata.jpg",TV3 CATALUNYA FAST 2
https://fast-tailor.3catdirectes.cat/v1/channel/ccma-channel2/hls.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/xmGNS4w/tvcata.jpg",TV3 CATALUNYA LOC
https://directes3-tv-cat.3catdirectes.cat/live-content/tv3-hls/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/xmGNS4w/tvcata.jpg",TV3 CATALUNYA LOC
https://directes-tv-cat.3catdirectes.cat/live-origin/tv3-hls/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/xmGNS4w/tvcata.jpg",TV3 CATALUNYA C33
https://directes-tv-int.3catdirectes.cat/live-content/c33-super3-hls/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/2F2XDFd/bondia.png",CATALUNYA BON DIA TV
https://directes-tv-int.3catdirectes.cat/live-content/bondia-hls/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/2F2XDFd/bondia.png",CATALUNYA BON DIA TV
https://directes-tv-int.3catdirectes.cat/live-origin/bondia-hls/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tM7BJP1/cata4.jpg",CATALUNYA 4 TV
https://limited35.todostreaming.es/live/mitjans-livestream.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/hB1Y74S/infocat.jpg",INFOCIUDADES TV CATALUNYA
https://consultant1267.cloudhostservers.com:3150/hybrid/play.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/crzKf1n/tenerife4.jpg",TENERIFE 4
https://videoserver.tmcreativos.com:19360/ccxwhsfcnq/ccxwhsfcnq.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/zxnPhtW/melilla.png",MELILLA TV
https://tvmelilla-hls-rm-lw.flumotion.com/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/HKFVwnt/ceum.jpg",CEUTA RTV
https://cdnlive.codev8.net/rtvcelive/channel1.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/PGd1Sj9H/huelva.jpg",HUELVA TV
https://5f71743aa95e4.streamlock.net:1936/huelvatv/htvdirecto/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/QnMxFJD/madr.jpg",TELE MADRID
https://telemadrid-23-secure2.akamaized.net/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/QnMxFJD/madr.jpg",TELE MADRID INT
https://new-international-23-secure2.akamaized.net/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/QnMxFJD/madr.jpg",TELE MADRID OTRA
https://laotra-1-23-secure2.akamaized.net/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/QnMxFJD/madr.jpg",TELE ONDE MADRID
https://tvradio-1-23-secure2.akamaized.net/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/6RYq1MS/extram.png",CANAL EXTRAMADURA
https://cdnapisec.kaltura.com/p/5581662/sp/558166200/playManifest/entryId/1_in8cxw3w/protocol/https/format/applehttp/a.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/LtG0fMD/galic.jpg",TVG GALICIA EU
https://crtvg-europa.flumotion.cloud/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/LtG0fMD/galic.jpg",TVG GALICIA AM
https://crtvg-america.flumotion.cloud/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/LtG0fMD/galic.jpg",TVG GALICIA MO
https://crtvg-amodino.flumotion.cloud/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/LtG0fMD/galic.jpg",TVG CULTURAL
https://crtvg-cultural.flumotion.cloud/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/LtG0fMD/galic.jpg",TVG INFANTIL
https://infantil-crtvg.flumotion.com/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/LtG0fMD/galic.jpg",TVG 2
https://crtvg-tvg2.flumotion.cloud/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/FhXvbPN/eitb.jpg",EITB 1
https://multimedia.eitb.eus/live-content/etb1hd-hls/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/FhXvbPN/eitb.jpg",EITB 2
https://multimedia.eitb.eus/live-content/etb2hd-hls/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/FhXvbPN/eitb.jpg",EITB INT
https://multimedia.eitb.eus/live-content/eitbbasque-hls/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/56TvMjR/etbs.jpg",EITB DEPORTE
https://multimedia.eitb.eus/live-content/oka3hd-hls/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/ySq76W3/rtva.png",ANDORRA DIFUSIÓ
https://play.cdn.enetres.net/56495F77FD124FECA75590A906965F2C021/021/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/0rxVFbs/tvcanaria.png",TV CANARIA
https://ythls.armelin.one/channel/UCTQrUTmzCWIfG6h4EVCdOCQ.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/0rxVFbs/tvcanaria.png",TV CANARIA
https://new.cache-stream.workers.dev/stream/UCTQrUTmzCWIfG6h4EVCdOCQ/live.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/2dHP72G/tvrioja.jpg",TV RIOJA
https://5924d3ad0efcf.streamlock.net/riojatv/riojatvlive/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/2dHP72G/tvrioja.jpg",RIOJA COCINA
https://stream-us-east-1.getpublica.com/playlist.m3u8?network_id=12108
#EXTINF:-1 tvg-logo="https://i.ibb.co/3yvX74m/101sevilla.jpg",101TV SEVILLA
https://www.streaming101tv.es:19360/sevilla/sevilla.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/NCQtNX5/telesur.png",TELESUR
https://cdnesmain.telesur.ultrabase.net/mbliveMain/hd/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/hKP8X8B/f24.png",FRANCE 24 ES
https://live.france24.com/hls/live/2037220/F24_ES_HI_HLS/master_5000.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/84XLZJq/dw.png",DW ESPAÑOL
https://dwamdstream104.akamaized.net/hls/live/2015530/dwstream104/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/JCjsXZm/nhk.png",NHK WORLD ESP
https://cdn.nhkworld.jp/www11/nhkworld-tv/bmcc-live/es/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/CH8JGfJ/cgtnes.png",CGTN ESPAÑOL
http://news.cgtn.com/resource/live/espanol/cgtn-e.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/CH8JGfJ/cgtnes.png",CGTN ESPAÑOL
https://espanol-livews.cgtn.com/hls/LSveOGBaBw41Ea7ukkVAUdKQ220802LSTexu6xAuFH8VZNBLE1ZNEa220802cd/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/pRYF5QL/hispantv.png",PRESS HISPAN TV
https://live.presstv.ir/hls/hispantv.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/XbSHxd5/cnn.png",CNN EN ESPAÑOL [geoblocked]
https://amg00803-amg00803c3-rakuten-us-5347.playouts.now.amagi.tv/playlist/amg00803-cnnfastinternational-cnnesponal-rakutenus/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/XbSHxd5/cnn.png",CNN EN ESPAÑOL [geoblocked]
https://amg00803-amg00803c3-samsung-es-4975.playouts.now.amagi.tv/playlist/amg00803-cnnfastinternational-cnnesponal-samsunges/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/D7w9h7Q/rt.png",RT ESPAÑOL [censure-blocked]
https://rt-esp.rttv.com/live/rtesp/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/D7w9h7Q/rt.png",RT ESPAÑOL [censure-blocked]
https://rt-esp.rttv.com/dvr/rtesp/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/hKP8X8B/f24.png",FRANCE 24 ES (backup)
https://live.france24.com/hls/live/2037220/F24_ES_HI_HLS/master_2300.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/VxLFYSj/euronews.png",EURONEWS ES (backup)
https://d35j504z0x2vu2.cloudfront.net/v1/master/0bc8e8376bd8417a1b6761138aa41c26c7309312/euronews-spa/euronews-es.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/VxLFYSj/euronews.png",EURONEWS ES (backup)
https://euronews-euronews-spanish-2-mx.samsung.wurl.tv/manifest/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/VxLFYSj/euronews.png",EURONEWS ES (backup)
https://rakuten-euronews-12-es.lg.wurl.tv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/VxLFYSj/euronews.png",EURONEWS ES (backup)
https://jmp2.uk/sam-ES260000968.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/VxLFYSj/euronews.png",EURONEWS ES (backup)
https://7c8b7dbf12d64234a983336fdddb88c2.mediatailor.us-east-1.amazonaws.com/v1/master/44f73ba4d03e9607dcd9bebdcb8494d86964f1d8/Samsung-es_EuroNewsLive/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/VxLFYSj/euronews.png",EURONEWS ES (backup)
http://stitcher-ipv4.pluto.tv/v1/stitch/embed/hls/channel/619d59b7cbef25000728221clivestitch/master.m3u8?deviceDNT=%7BTARGETOPT%7D&deviceModel=samsung&deviceVersion=unknown&appVersion=unknown&deviceType=samsung-tvplus&deviceMake=samsung
#EXTINF:-1 tvg-logo="https://i.ibb.co/VxLFYSj/euronews.png",EURONEWS ES (backup)
http://stitcher-ipv4.pluto.tv/v1/stitch/embed/hls/channel/60d3583ef310610007fb02b1livestitch/master.m3u8?deviceDNT=%7BTARGETOPT%7D&deviceModel=samsung&deviceVersion=unknown&appVersion=unknown&deviceType=samsung-tvplus&deviceMake=samsung
#EXTINF:-1 tvg-logo="https://i.ibb.co/VxLFYSj/euronews.png",EURONEWS ES (backup)
http://stitcher-ipv4.pluto.tv/v1/stitch/embed/hls/channel/60492dcf1c9b6a00089f41dflivestitch/master.m3u8?deviceDNT=%7BTARGETOPT%7D&deviceModel=samsung&deviceVersion=unknown&appVersion=unknown&deviceType=samsung-tvplus&deviceMake=samsung
#EXTINF:-1 tvg-logo="https://i.ibb.co/VM5vGBV/la1.jpg",TVE LA 1 (backup)
https://rtvelivestream.akamaized.net/rtvesec/la1/la1_main_dvr.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/ssGmhbH/la2.jpg",TVE LA 2 (backup)
https://rtvelivestream.akamaized.net/rtvesec/la2/la2_main_dvr.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/fqg1vfr/24h.png",TVE 24 H (backup)
https://rtvelivestream.akamaized.net/rtvesec/24h/24h_main.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/fqg1vfr/24h.png",TVE 24 H (backup)
https://rtvelivestream.rtve.es/rtvesec/24h/24h_main.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/ypn5DBD/tveint.png",TVE INTERNACIONAL (backup)
https://ztnr.rtve.es/ztnr/6891743.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/ypn5DBD/tveint.png",TVE INTERNACIONAL (america)
https://rtvelivestream-rtveplayplus.rtve.es/rtvesec/int/tvei_ame_main_dvr_1080.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/ypn5DBD/tveint.png",TVE INTERNACIONAL (america)
https://rtvelivestream.akamaized.net/rtvesec/int/tvei_ame_main.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/99kVf9W/somoscine.png",TVE SOMOS CINE (backup)
https://rtvelivestream.akamaized.net/hls/nxrtgolumi/music/stream1.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/99kVf9W/somoscine.png",TVE SOMOS CINE (backup)
https://rtvelivestream.akamaized.net/eventual/gofast/play_cine_main_dvr_1080.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/3T2TS2p/tvestar.jpg",STAR TVE (espana)
https://rtvelivestream-rtveplayplus.rtve.es/rtvesec/int/star_main_dvr_1080.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/hYTkm8L/A3es.png",ANTENA 3 (backup)
http://nodep002.service.openstream.es/SVoriginOperatorEdge3/smil:7_HD.smil/manifest.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/hYTkm8L/A3es.png",ANTENA 3 (backup)
https://spa-ha-p005.cdn.masmediatv.es/SVoriginOperatorEdge3/smil:7_premium.smil/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/hYTkm8L/A3es.png",ANTENA 3 (backup)
https://spa-ha-p005.cdn.masmediatv.es/SVoriginOperatorEdge3/smil:7_HD.smil/manifest.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/hYTkm8L/A3es.png",ANTENA 3 (backup)
https://gitlab.com/movrey/movrel/-/raw/main/ant3.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/hRs6WrH/C4es.png",CUATRO (backup)
http://nodep002.service.openstream.es/SVoriginOperatorEdge3/smil:9_HD.smil/manifest.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/hRs6WrH/C4es.png",CUATRO (backup)
https://spa-ha-p005.cdn.masmediatv.es/SVoriginOperatorEdge3/smil:9_premium.smil/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/hRs6WrH/C4es.png",CUATRO (backup)
https://spa-ha-p005.cdn.masmediatv.es/SVoriginOperatorEdge3/smil:9_HD.smil/manifest.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/7gMg1nb/t5es.png",TELECINCO (backup)
http://nodep002.service.openstream.es/SVoriginOperatorEdge3/smil:8_HD.smil/manifest.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/7gMg1nb/t5es.png",TELECINCO (backup)
https://spa-ha-p005.cdn.masmediatv.es/SVoriginOperatorEdge3/smil:8_premium.smil/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/7gMg1nb/t5es.png",TELECINCO (backup)
https://spa-ha-p005.cdn.masmediatv.es/SVoriginOperatorEdge3/smil:8_HD.smil/manifest.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/6JF4BK4/l6es.png",LA SEXTA (backup)
http://nodep002.service.openstream.es/SVoriginOperatorEdge3/smil:11_HD.smil/manifest.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/6JF4BK4/l6es.png",LA SEXTA (backup)
https://spa-ha-p005.cdn.masmediatv.es/SVoriginOperatorEdge3/smil:11_premium.smil/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/6JF4BK4/l6es.png",LA SEXTA (backup)
https://spa-ha-p005.cdn.masmediatv.es/SVoriginOperatorEdge3/smil:11_HD.smil/manifest.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/hYTkm8L/A3es.png" user-agent="VAVOO/1.0" referer="https://vavoo.to/",ANTENA 3 (backup)
https://joaquinito02.es/vavoo/254679370.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/hYTkm8L/A3es.png" user-agent="VAVOO/1.0" referer="https://vavoo.to/",ANTENA 3 (backup)
https://joaquinito02.es/vavoo/2255480833.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/hRs6WrH/C4es.png" user-agent="VAVOO/1.0" referer="https://vavoo.to/",CUATRO (backup)
https://joaquinito02.es/vavoo/1590334161.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/hRs6WrH/C4es.png" user-agent="VAVOO/1.0" referer="https://vavoo.to/",CUATRO (backup)
https://joaquinito02.es/vavoo/4194733823.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/7gMg1nb/t5es.png" user-agent="VAVOO/1.0" referer="https://vavoo.to/",TELECINCO (backup)
https://joaquinito02.es/vavoo/1024256819.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/7gMg1nb/t5es.png" user-agent="VAVOO/1.0" referer="https://vavoo.to/",TELECINCO (backup)
https://joaquinito02.es/vavoo/353095972.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/6JF4BK4/l6es.png" user-agent="VAVOO/1.0" referer="https://vavoo.to/",LA SEXTA (backup)
https://joaquinito02.es/vavoo/2660027208.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/6JF4BK4/l6es.png" user-agent="VAVOO/1.0" referer="https://vavoo.to/",LA SEXTA (backup)
https://joaquinito02.es/vavoo/238901671.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/BGy5vM5/clan.jpg",TVE CLAN [geo-restricted]
https://rtvelivestream-clnx.rtve.es/rtvesec/clan/clan_main_dvr_720.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/BGy5vM5/clan.jpg",TVE CLAN [geo-restricted]
https://rtvelivestream-rtveplayplus.rtve.es/rtvesec/clan/clan_main_720.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/BGy5vM5/clan.jpg",TVE CLAN [geo-restricted]
https://rtvelivestream.akamaized.net/rtvesec/clan/clan_main.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/BGy5vM5/clan.jpg",TVE CLAN [geo-restricted]
https://rtvelivestream.rtve.es/rtvesec/clan/clan_main.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/crzKf1n/tenerife4.jpg",TENERIFE 4 (offlink)
https://5940924978228.streamlock.net/Directo1/Directo1/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/QnMxFJD/madr.jpg",TELE MADRID (offlink)
https://telemadridhls2-live-hls.secure2.footprint.net/egress/chandler/telemadrid/telemadrid_1/index.m3u8


#EXTINF:-1 tvg-logo="https://i.ibb.co/n0Pwp2S/alaoulainter.png" group-title="15. |MA-DZ-TN|🇲🇦🇩🇿🇹🇳 MAGHREB المغرب",AL AOULA LAÂYOUNE الأولى
https://cdn.live.easybroadcast.io/abr_corp/73_laayoune_pgagr52/playlist_dvr.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/n0Pwp2S/alaoulainter.png",Al AOULA INT الأولى
https://cdn.live.easybroadcast.io/abr_corp/73_aloula_w1dqfwm/playlist_dvr.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/dp5Z2dh/2m.png" user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0" referer="https://2m.ma",2M MONDE الثانية
https://cdn-globecast.akamaized.net/live/eds/2m_monde/hls_video_ts_tuhawxpiemz257adfc/2m_monde.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Wk8BWg4/arryadia.png",ARRYADIA الرياضية
https://cdn.live.easybroadcast.io/abr_corp/73_arryadia_k2tgcj0/playlist_dvr.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/k8gk0Hb/arrabiaa.png",ATHAQAFIA الثقافية
https://cdn.live.easybroadcast.io/abr_corp/73_arrabia_hthcj4p/playlist_dvr.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/5kp5CmP/almaghribia.png",AL MAGHRIBIA المغربية الإخبارية
https://cdn.live.easybroadcast.io/abr_corp/73_almaghribia_83tz85q/playlist_dvr.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Gxn4XrB/assadissa.png",ASSADISSA القرآن الكريم
https://cdn.live.easybroadcast.io/abr_corp/73_assadissa_7b7u5n1/playlist_dvr.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/rmRc08Z/tamazight.png",TAMAZIGHT الأمازيغية
https://cdn.live.easybroadcast.io/abr_corp/73_tamazight_tccybxt/playlist_dvr.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/rQJcGTc/medi1tv.png",MEDI 1 MG العربية
https://streaming1.medi1tv.com/live/smil:medi1tv.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/rQJcGTc/medi1tv.png",MEDI 1 AR العربية
https://streaming1.medi1tv.com/live/smil:medi1ar.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/rQJcGTc/medi1tv.png",MEDI 1 FR العربية
https://streaming1.medi1tv.com/live/smil:medi1fr.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/pdd2VqB/chada.jpg",CHADA TV شدى
https://edge14.vedge.infomaniak.com/livecast/chadatv/manifest.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/pdd2VqB/chada.jpg",CHADA TV شدى
https://test-streamer.eagrpservices.com/video/live/720p/chada.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/5M4CwmQ/watania1.png",WATANIA 1
http://live.watania1.tn:1935/live/watanya1.stream/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/5M4CwmQ/watania1.png",WATANIA 1
https://github.com/MassinDV/Youtube-arabic-channels/raw/main/live/ch96.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/TM8sRjr/watanya-2.png",WATANIA 2
https://github.com/MassinDV/Youtube-arabic-channels/raw/main/live/ch35.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/TM8sRjr/watanya-2.png",WATANIA 2
http://live.watania2.tn:1935/live/watanya2.stream/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/8DxdBPf/Attessia9.png",ATTASIA 9
https://cdn.bestream.io:19360/alqanat9/alqanat9.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/stZxQHF/nessma.png",NESSMA
https://edge66.magictvbox.com/liveApple/nessma/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/9tsD8WP/TV2Al.png",TV2 ALGÉRIE
http://69.64.57.208/canalalgerie/playlist.m3u8
#EXTINF:-1  tvg-logo="https://i.ibb.co/Gn19S8p/al24dz.png",AL24 NEWS
https://cdn.live.easybroadcast.io/abr_corp/66_al24_u4yga6h/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/yQmcHjz/echourouk.png",ECHOROUK TV DZ
https://hls-distrib-rlb1.dzsecurity.net/live/EchoroukTV/playlist.m3u8?e=&token=
#EXTINF:-1 tvg-logo="https://i.ibb.co/1vH6q4L/echounws.png",ECHOROUK NEWS DZ
https://hls-distrib-rlb1.dzsecurity.net/live/EchoroukNews/playlist.m3u8?e=&token=
#EXTINF:-1 tvg-logo="https://i.ibb.co/7Q4Zv2v/elhayat.png",EL HAYAT DZ
https://hls-distrib-rlb1.dzsecurity.net/live/ElhayatTV/playlist.m3u8?e=&token=
#EXTINF:-1 tvg-logo="https://i.ibb.co/pbQCS5g/elwataniadz.jpg" referer="https://player.castr.com/",EL WATANIA TV
https://stream.castr.com/62c18c3f14d09a0b7e5355a5/live_1b36cfb0ba2411ee9700956e0f7084c8/index.fmp4.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/pPwR2Tc/ennahar.png" referer="https://echorouk.dzsecurity.net/embed/echorouk.php",ENNAHAR TV
https://ennahar-live.dzsecurity.net/fullres/EnnaharTV_First/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/pPwR2Tc/ennahar.png" referer="https://echorouk.dzsecurity.net/embed/echorouk.php",ENNAHAR TV
https://ennahar-live.dzsecurity.net/fullsrc/EnnaharTV/chunks.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/H4N2sNS/cna.png",CNA
https://live.creacast.com/cna/smil:cna.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/5M4CwmQ/watania1.png",WATANIA 1 (backup)
https://new.cache-stream.workers.dev/stream/UCdvWVsmQBROkgcGzVep73oA/live.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/5M4CwmQ/watania1.png",WATANIA 1 (backup)
https://ythls.armelin.one/channel/UCdvWVsmQBROkgcGzVep73oA.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/TM8sRjr/watanya-2.png",WATANIA 2 (backup)
https://new.cache-stream.workers.dev/stream/UCJW9gatYczI191TunQxMGbA/live.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/TM8sRjr/watanya-2.png",WATANIA 2 (backup)
https://ythls.armelin.one/channel/UCJW9gatYczI191TunQxMGbA.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/pdd2VqB/chada.jpg",CHADA TV شدى (backup)
https://chadatv.vedge.infomaniak.com/livecast/chadatv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/pdd2VqB/chada.jpg",CHADA TV شدى (backup)
https://chadatv.vedge.infomaniak.com/livecast/chadatv/manifest.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/rQJcGTc/medi1tv.png",MEDI 1 MG العربية (backup)
https://streaming1.medi1tv.com/live/smil:medi1tv.smil/chunklist_w1675843453_b978000_slar.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/rQJcGTc/medi1tv.png",MEDI 1 MG العربية (backup)
https://streaming1.medi1tv.com/live/smil:medi1tv.smil/chunklist_w_b978000_slar.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/rQJcGTc/medi1tv.png",MEDI 1 AR العربية (backup)
https://streaming1.medi1tv.com/live/smil:medi1ar.smil/chunklist_w_b978000_slar.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/rQJcGTc/medi1tv.png",MEDI 1 FR العربية (backup)
https://streaming1.medi1tv.com/live/smil:medi1fr.smil/chunklist_w_b978000_slar.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/rQJcGTc/medi1tv.png",MEDI 1 MG العربية (off-backup)
https://streaming2.medi1tv.com/live/smil:medi1tv.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/n0Pwp2S/alaoulainter.png" referer="https://snrtlive.ma/",AL AOULA LAÂYOUNE الأولى (backup)
https://cdnamd-hls-globecast.akamaized.net/live/ramdisk/al_aoula_laayoune/hls_snrt/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/n0Pwp2S/alaoulainter.png" referer="https://snrtlive.ma/",Al AOULA INT الأولى (backup)
https://cdnamd-hls-globecast.akamaized.net/live/ramdisk/al_aoula_inter/hls_snrt/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/dp5Z2dh/2m.png" user-agent="ExoPlayerDemo/2.0.6 (Linux;Android 14) ExoPlayerLib/2.14.0" referer="https://2m.ma",2M MONDE (exopl) الثانية
https://cdn-globecast.akamaized.net/live/eds/2m_monde/hls_video_ts_tuhawxpiemz257adfc/2m_monde.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/dp5Z2dh/2m.png",2M MONDE (n/f) الثانية
https://cdnamd-hls-globecast.akamaized.net/live/ramdisk/2m_monde/hls_video_ts_tuhawxpiemz257adfc/2m_monde.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/dp5Z2dh/2m.png" referer="https://2m.ma/",2M MONDE الثانية (backupoff)
https://cdn-globecast.akamaized.net/live/eds/2m_monde/hls_video_ts_tuhawxpiemz257adfc/2m_monde.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Wk8BWg4/arryadia.png" referer="https://snrtlive.ma/",ARRYADIA الرياضية (backup)
https://cdnamd-hls-globecast.akamaized.net/live/ramdisk/arriadia/hls_snrt/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/k8gk0Hb/arrabiaa.png" referer="https://snrtlive.ma/",ATHAQAFIA الثقافية (backup)
https://cdnamd-hls-globecast.akamaized.net/live/ramdisk/arrabiaa/hls_snrt/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/5kp5CmP/almaghribia.png" referer="https://snrtlive.ma/",AL MAGHRIBIA المغربية الإخبارية (backup)
https://cdnamd-hls-globecast.akamaized.net/live/ramdisk/al_maghribia_snrt/hls_snrt/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Gxn4XrB/assadissa.png" referer="https://snrtlive.ma/",ASSADISSA القرآن الكريم (backup)
https://cdnamd-hls-globecast.akamaized.net/live/ramdisk/assadissa/hls_snrt/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/rmRc08Z/tamazight.png" referer="https://snrtlive.ma/",TAMAZIGHT الأمازيغية (backup)
https://cdnamd-hls-globecast.akamaized.net/live/ramdisk/tamazight_tv8_snrt/hls_snrt/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/n0Pwp2S/alaoulainter.png" referer="https://snrtlive.ma/",AL AOULA LAÂYOUNE الأولى
https://cdn-globecast.akamaized.net/live/eds/al_aoula_laayoune/hls_snrt/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/n0Pwp2S/alaoulainter.png" referer="https://snrtlive.ma/",Al AOULA INT الأولى
https://cdn-globecast.akamaized.net/live/eds/al_aoula_inter/hls_snrt/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/dp5Z2dh/2m.png" user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0" referer="https://2m.ma",2M MONDE الثانية
https://cdn-globecast.akamaized.net/live/eds/2m_monde/hls_video_ts_tuhawxpiemz257adfc/2m_monde.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Wk8BWg4/arryadia.png" referer="https://snrtlive.ma/",ARRYADIA الرياضية
https://cdn-globecast.akamaized.net/live/eds/arriadia/hls_snrt/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/k8gk0Hb/arrabiaa.png" referer="https://snrtlive.ma/",ATHAQAFIA الثقافية
https://cdn-globecast.akamaized.net/live/eds/arrabiaa/hls_snrt/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/5kp5CmP/almaghribia.png" referer="https://snrtlive.ma/",AL MAGHRIBIA المغربية الإخبارية
https://cdn-globecast.akamaized.net/live/eds/al_maghribia_snrt/hls_snrt/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Gxn4XrB/assadissa.png" referer="https://snrtlive.ma/",ASSADISSA القرآن الكريم
https://cdn-globecast.akamaized.net/live/eds/assadissa/hls_snrt/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/rmRc08Z/tamazight.png" referer="https://snrtlive.ma/",TAMAZIGHT الأمازيغية
https://cdn-globecast.akamaized.net/live/eds/tamazight_tv8_snrt/hls_snrt/index.m3u8
#EXTINF:-1 group-title="15. |MA-DZ-TN|🇲🇦🇩🇿🇹🇳 MAGHREB المغرب",--- |⬇DOWN/OFFLINES⬇| ---
https://blank
#EXTINF:-1 tvg-logo="https://i.ibb.co/stZxQHF/nessma.png",NESSMA
https://raw.githubusercontent.com/ipstreet312/freeiptv/master/ressources/dzflix/nessma.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/JmRh3Xn/helwa.png",HELWA
https://raw.githubusercontent.com/ipstreet312/freeiptv/master/ressources/dzflix/helwa.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/HzvjJq6/samira.png",SAMIRA
https://raw.githubusercontent.com/ipstreet312/freeiptv/master/ressources/dzflix/samira.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/1vH6q4L/echounws.png",ECHOROUK NEWS
https://bledflix-echorouk-news.b-cdn.net/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/1vH6q4L/echounws.png",ECHOROUK NEWS (backup)
https://raw.githubusercontent.com/ipstreet312/freeiptv/master/ressources/dzflix/echorouknews.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/yQmcHjz/echourouk.png",ECHOROUK TV
https://raw.githubusercontent.com/ipstreet312/freeiptv/master/ressources/dzflix/echorouktv.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/ByPHXnt/bilad.png",EL BILAD
https://raw.githubusercontent.com/ipstreet312/freeiptv/master/ressources/dzflix/elbilad.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/9tsD8WP/TV2Al.png",TV2 ALGERIE [hta_dz-off]
https://cdn02.hta.dz/abr_htatv/CANAL_ALGERIE/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/xY39PSC/TV1-ENTV.png",TV1 ENTV [hta_dz-off]
https://cdn02.hta.dz/abr_htatv/PROGRAMME_NATIONAL/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/qR3CZP8/tv3al.png",TV3 ALGERIE [hta_dz-off]
https://cdn02.hta.dz/abr_htatv/A3_HD/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/4tmp0NH/tv4al.png",TV4 ALGERIE [hta_dz-off]
https://cdn02.hta.dz/abr_htatv/TV_4/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/SXjJGYZ/tv5al.png",TV5 ALGERIE [hta_dz-off]
https://cdn02.hta.dz/abr_htatv/TV_5/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/fXcD722/tv6al.png",TV6 ALGERIE [hta_dz-off]
https://cdn02.hta.dz/abr_htatv/TV_6_HD/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/hBCbJ22/tv7al.png",TV7 ELMAARIFA [hta_dz-off]
https://cdn02.hta.dz/abr_htatv/TV7_ELMAARIFA/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/zSWw6QZ/tv8al.png",TV8 EDHAKIRA [hta_dz-off]
https://cdn02.hta.dz/abr_htatv/TV8_EDHAKIRA/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/HzvjJq6/samira.png",SAMIRA TV [hta_dz-off]
https://cdn02.hta.dz/abr_htatv/SamiraTV/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/ByPHXnt/bilad.png",EL BILAD [hta_dz-off]
https://cdn02.hta.dz/abr_htatv/EL_BILAD/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/pPwR2Tc/ennahar.png",ENNAHAR TV [hta_dz-off]
https://cdn02.hta.dz/abr_htatv/ENNAHAR_TV/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/7Q4Zv2v/elhayat.png",EL HAYAT TV [hta_dz-off]
https://cdn02.hta.dz/abr_htatv/EL_HAYAT_TV_ALGERIE/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Gn8kzrj/fadrj.png",EL FADRJ TV [hta_dz-off]
https://cdn02.hta.dz/abr_htatv/EL_FADJR_TV_DZ/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/BfwWGdQ/djan1.png",EL DJAZAIR N1 [hta_dz-off]
https://cdn02.hta.dz/abr_htatv/El_Djazair_N1/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/sVMjt0y/bahia.png",BAHIA TV [hta_dz-off]
https://cdn02.hta.dz/abr_htatv/Bahia_TV/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/fnc8K1s/al24.jpg",AL24 NEWS [hta_dz-off]
https://cdn02.hta.dz/abr_htatv/AL24_News/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/y5rY7zJ/heddaf.png",EL HEDDAF TV [hta_dz-off]
https://cdn02.hta.dz/abr_htatv/EL_HEDDAF_TV/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/3MdNH7S/alanis.png",ALANIS TV [hta_dz-off]
https://cdn02.hta.dz/abr_htatv/El_Fhama_TV/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/yQmcHjz/echourouk.png",ECHOROUK TV [hta_dz-off]
https://cdn02.hta.dz/abr_htatv/Echorouk_TV_HD/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/1vH6q4L/echounws.png",ECHOROUK NEWS  [hta_dz-off]
https://cdn02.hta.dz/abr_htatv/ECHOROUK_NEWS/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/PMpGQk6/beur.png",BEUR TV [hta_dz-off]
https://cdn02.hta.dz/abr_htatv/Beur_TV/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/j8L3hMr/djaz1.png",EL DJAZAIRIA TV [downline]
https://cdn02.hta.dz/abr_htatv/EL_DJAZAIRIA_TV/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/h9yh1nr/lina.png",LINA TV [downline]
https://cdn02.hta.dz/abr_htatv/Lina_TV/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/HzvjJq6/samira.png",SAMIRA TV [downline]
https://shls-live-ak.akamaized.net/out/v1/2daff8b433344d659bd5079224afc3ab/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/HzvjJq6/samira.png",SAMIRA TV [downline]
https://d2p6676ajpsg1j.cloudfront.net/out/v1/2daff8b433344d659bd5079224afc3ab/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/stZxQHF/nessma.png",NESSMA [offlink]
https://shls-live-ak.akamaized.net/out/v1/119ae95bbc91462093918a7c6ba11415/index.m3u8


#EXTINF:-1 tvg-logo="https://i.ibb.co/fMMBKqc/kan11.png" group-title="16. |IL|🇮🇱 ISRAEL ישראל",KAN 11 כאן
https://kan11w.media.kan.org.il/hls/live/2105694/2105694/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/fMMBKqc/kan11.png",KAN 11 sub-cc כאן
https://kan11sub.media.kan.org.il/hls/live/2024678/2024678/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/5TQ4RM3/Keshet12.png" user-agent="SmartOs Tv",KESHET 12 קשת
https://raw.githubusercontent.com/ipstreet312/freeiptv/master/ressources/keshetil/py/k12.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/5TQ4RM3/Keshet12.png" user-agent="SmartOs Tv",KESHET 12 sub-cc קשת
https://raw.githubusercontent.com/ipstreet312/freeiptv/master/ressources/keshetil/py/k12cc.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/MnSQCcr/R1322.jpg",RESHET 13 רשת
https://d2xg1g9o5vns8m.cloudfront.net/out/v1/66d4ac8748ce4a9298b4e40e48d1ae2f/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/MnSQCcr/R1322.jpg",RESHET 13 sub-cc רשת
https://d198ztbnlup2iq.cloudfront.net/out/v1/2d9050c90fb94df8b78d1d98306a1a65/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/4g6BSYf/now14smgri.png",NOW 14 עכשיו
https://ch14-channel14-content.akamaized.net/hls/live/2104807/CH14_CHANNEL14/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/j68q1Bp/i24.png",i24 NEWS HE עברית
https://bcovlive-a.akamaihd.net/d89ede8094c741b7924120b27764153c/eu-central-1/5377161796001/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tLYB26T/h2322.png",HINUCHIT 23 חינוכית
https://kan23.media.kan.org.il/hls/live/2024691/2024691/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/7nYM8MK/arutz24tvtrp.png",MAKO 24 ערוץ
https://mako-streaming.akamaized.net/direct/hls/live/2035340/ch24live/video_10801920_p_1.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/3hN9N8X/tv10coil.png",CALCALA 10 ערוץ_הכלכלה
https://r.il.cdn-redge.media/livehls/oil/calcala/live/channel10/live.livx/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/zP5vjLD/knesset.png",HAKNESSET 99 כנסת
https://kneset.gostreaming.tv/p2-kneset/_definst_/myStream/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/zP5vjLD/knesset.png",HAKNESSET 99 sub-cc כנסת
https://kneset.gostreaming.tv/p2-Accessibility/_definst_/myStream/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/sQd5XDT/13comedy.jpg",RESHET 13 COMEDY
https://d15ds134q59udk.cloudfront.net/out/v1/fbba879221d045598540ee783b140fe2/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tPh5D2w/13nofesh.jpg",RESHET 13 NOFESH
https://d1yd8hohnldm33.cloudfront.net/out/v1/19dee23c2cc24f689bd4e1288661ee0c/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/9sX793L/13reality.jpg",RESHET 13 REALITY
https://d2dffl3588mvfk.cloudfront.net/out/v1/d8e15050ca4148aab0ee387a5e2eb46b/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/jzRyjBn/walla.png",WALLA !+ וואלה! חדשות
https://cdn-uw2-prod.tsv2.amagi.tv/linear/amg01742-walla-wallanews-ono/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Yc5Yf1q/sport5il.png",SPORT5 STUDIO RADIO LIVE
https://rgelive.akamaized.net/hls/live/2043151/radiolive/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Yc5Yf1q/sport5il.png",SPORT5 STUDIO RADIO LIVE
https://rgelive.akamaized.net/hls/live/2043095/live3/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/kq4XM0Y/ynet.png",YNET NEWS ידיעות אחרונות
https://ynet-live-01.ynet-pic1.yit.co.il/ynet/live.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/1rSGfFw/N12n.png" user-agent="SmartOs Tv",NEWS 12 חדשות 
https://raw.githubusercontent.com/ipstreet312/freeiptv/master/ressources/keshetil/py/n12.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/j68q1Bp/i24.png",i24 NEWS FR
https://bcovlive-a.akamaihd.net/41814196d97e433fb401c5e632d985e9/eu-central-1/5377161796001/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/j68q1Bp/i24.png",i24 NEWS EN
https://bcovlive-a.akamaihd.net/ecf224f43f3b43e69471a7b626481af0/eu-central-1/5377161796001/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/j68q1Bp/i24.png",i24 NEWS AR
https://bcovlive-a.akamaihd.net/95116e8d79524d87bf3ac20ba04241e3/eu-central-1/5377161796001/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/MG43H4H/hala.png",PANET 30 HALA هلا
https://stream.panet.com/edge/halaTV/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/fqTYrGY/33.png",KAN 33 MAKAN مكان
https://makan.media.kan.org.il/hls/live/2024680/2024680/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/PYtP8fm/arutz9ru.png",ISRAEL 9TV канал
https://new.cache-stream.workers.dev/channel/UCixtbfonx_QIjS1DB96zcFg/live.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/PYtP8fm/arutz9ru.png",ISRAEL 9TV канал
https://ythls.armelin.one/channel/UCixtbfonx_QIjS1DB96zcFg.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/6yjTszg/kan26.png",KAN 26 אפיק
https://reshetbetvideo.media.kan.org.il/hls/live/2044082/2044082/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/93bQz4t/kabalah.png",KABBALAH 96
http://edge3.uk.kab.tv/live/tv66-heb-high/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/93bQz4t/kabalah.png",KABBALAH 96
https://edge2.il.kab.tv/live/tv66-heb-high/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/bJVPhHD/hidabroot.png",HIDABROOT 97
https://cdn.cybercdn.live/HidabrootIL/Live97/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/bJVPhHD/hidabroot.png",HIDABROOT 97
https://edge-fs-10.cybercdn.live/HidabrootIL/Live97/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Ph3cBMj/musayof.jpg",MUSAYOF מוסאיוף
http://wowza.media-line.co.il/Musayof-Live/livestream.sdp/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tMm7vdM/shelanug.jpg",SHELANU GOD-IL
https://1247634592.rsc.cdn77.org/1247634592/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/2g7Sw4c/21.jpg",SHOPPING 21 [ended]
https://shoppingil-rewriter.vidnt.com/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/5MyMYqB/relevantil.png",RELEVANT רלוונט [ended]
https://6180c994cb835402.mediapackage.eu-west-1.amazonaws.com/out/v1/f1339272dd24416ca60b00e69075d783/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/3RwfT5M/bigbil.png" referer="https://13tv.co.il/home/bb-livestream/",BIG BROTHER IL [geo-blocked]
https://d2lckchr9cxrss.cloudfront.net/out/v1/c73af7694cce4767888c08a7534b503c/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/fMMBKqc/kan11.png",KAN 11 כאן (backup)
https://kan11.media.kan.org.il/hls/live/2024514/2024514/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/fMMBKqc/kan11.png",KAN 11 כאן (backup)
https://kan11b.media.kan.org.il/hls/live/2096972/2096972/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/5TQ4RM3/Keshet12.png",KESHET 12 קשת (backup)
https://mako-streaming.akamaized.net/stream/hls/live/2033791/k12/profile/3/profileManifest.m3u8?_uid=a004f873-f654-4ab8-a86c-4aa2bbfc909d&rK=a1
#EXTINF:-1 tvg-logo="https://i.ibb.co/5TQ4RM3/Keshet12.png",KESHET 12 קשת (backup)
https://mako-streaming.akamaized.net/stream/hls/live/2033791/k12n12wad/profile/4/profileManifest.m3u8?_uid=a004f873-f654-4ab8-a86c-4aa2bbfc909d&rK=a1
#EXTINF:-1 tvg-logo="https://i.ibb.co/5TQ4RM3/Keshet12.png",KESHET 12 קשת (backup)
https://mako-streaming.akamaized.net/stream/hls/live/2033791/k12dvr/profile/5/profileManifest.m3u8?_uid=f0ea0c4b-0bfe-491a-a7d6-7cfd23125300&rK=a
#EXTINF:-1 tvg-logo="https://i.ibb.co/MnSQCcr/R1322.jpg",RESHET 13 רשת (backup)
https://reshet.g-mana.live/media/cdefce3a-14ec-46cc-a147-1275c4a8b9ed/mainManifest.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/MnSQCcr/R1322.jpg",RESHET 13 רשת (backup)
https://d2xg1g9o5vns8m.cloudfront.net/out/v1/0855d703f7d5436fae6a9c7ce8ca5075/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/MnSQCcr/R1322.jpg",RESHET 13 רשת (backup)
https://d18b0e6mopany4.cloudfront.net/out/v1/08bc71cf0a0f4712b6b03c732b0e6d25/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/MnSQCcr/R1322.jpg",RESHET 13 רשת (backup)
https://d18b0e6mopany4.cloudfront.net/out/v1/2f2bc414a3db4698a8e94b89eaf2da2a/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/MnSQCcr/R1322.jpg",RESHET 13 רשת (backup)
https://reshet.g-mana.live/media/87f59c77-03f6-4bad-a648-897e095e7360/mainManifest.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/MnSQCcr/R1322.jpg",RESHET 13 sub-cc רשת (backup)
https://reshet.g-mana.live/media/4607e158-e4d4-4e18-9160-3dc3ea9bc677/mainManifest.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/1rSGfFw/N12n.png" user-agent="SmartOs Tv",NEWS 12 חדשות (backup)
https://raw.githubusercontent.com/ipstreet312/freeiptv/master/ressources/keshetil/py/n12b.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tLYB26T/h2322.png",HINUCHIT 23 sub-cc חינוכית (backup rescue)
https://kan23w.media.kan.org.il/hls/live/2108842/2108842/source1_2.5k/chunklist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/7nYM8MK/arutz24tvtrp.png",MAKO 24 ערוץ (backup)
https://mako-streaming.akamaized.net/direct/hls/live/2035340/ch24live/video_7201280_p_1.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/3hN9N8X/tv10coil.png",CALCALA 10 ערוץ_הכלכלה (backup)
https://r.il.cdn-redge.media/livedash/oil/calcala/live/channel10/live.livx/manifest.mpd?dummyfile
#EXTINF:-1 tvg-logo="https://i.ibb.co/3hN9N8X/tv10coil.png",CALCALA 10 ערוץ_הכלכלה (backup)
https://r.il.cdn-redge.media/livedash/oil/calcala/live/channel10/live.livx
#EXTINF:-1 tvg-logo="https://i.ibb.co/jzRyjBn/walla.png",WALLA !+ וואלה! חדשות (backup)
https://amg01742-walla-wallanews-ono-btlna.amagi.tv/playlist/amg01742-walla-wallanews-ono/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/jzRyjBn/walla.png",WALLA ! + (backup rescue)
https://live.wcdn.co.il/news/prog_index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/jzRyjBn/walla.png",WALLA ! + (backup secure)
https://live.wcdn.co.il/yes/prog_index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/5MyMYqB/relevantil.png",RELEVANT רלוונט (backup)
https://6180c994cb835402.mediapackage.eu-west-1.amazonaws.com/out/v1/06e44cd7f7e0445fbd669f279c997fd4/index.mpd
#EXTINF:-1 tvg-logo="https://i.ibb.co/kq4XM0Y/ynet.png",YNET NEWS (feed)
https://ynet-live-02.ynet-pic1.yit.co.il/ynet/live.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/kq4XM0Y/ynet.png",YNET NEWS (feed)
https://ynet-live-03.ynet-pic1.yit.co.il/ynet/live.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/kq4XM0Y/ynet.png",YNET NEWS (feed)
https://ynet-live-04.ynet-pic1.yit.co.il/ynet/live.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/kq4XM0Y/ynet.png",YNET NEWS (feed)
https://ynet-live-05.ynet-pic1.yit.co.il/ynet/live.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/fMMBKqc/kan11.png",KAN 11 כאן (backlink)
https://cdnapisec.kaltura.com/p/2717431/sp/2717431/playManifest/entryId/1_sdqcljik/deliveryProfileId/672/protocol/https/format/applehttp/a.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/fMMBKqc/kan11.png",KAN 11 כאן sub-cc (backlink)
https://cdnapisec.kaltura.com/p/2717431/sp/2717431/playManifest/entryId/1_8ji7g6s3/deliveryProfileId/672/protocol/https/format/applehttp/a.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/fMMBKqc/kan11.png",KAN 11 כאן (backlink)
https://cdnapisec.kaltura.com/p/2717431/sp/2717431/playManifest/entryId/1_syhxntss/deliveryProfileId/672/protocol/https/format/applehttp/a.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tLYB26T/h2322.png",HINUCHIT 23 חינוכית (backlink)
https://cdnapisec.kaltura.com/p/2717431/sp/2717431/playManifest/entryId/1_vd30ud46/deliveryProfileId/672/protocol/https/format/applehttp/a.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/fqTYrGY/33.png",KAN 33 MAKAN مكان (backlink)
https://cdnapisec.kaltura.com/p/2717431/sp/2717431/playManifest/entryId/1_vw6qllis/deliveryProfileId/672/protocol/https/format/applehttp/a.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/MnSQCcr/R1322.jpg",RESHET 13 רשת (backlink)
https://cdnapisec.kaltura.com/p/2748741/sp/2748741/playManifest/entryId/1_l38msgjy/deliveryProfileId/672/protocol/https/format/applehttp/a.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/zP5vjLD/knesset.png",HAKNESSET 99 כנסת (backlink)
https://contactgbs.mmdlive.lldns.net/contactgbs/a40693c59c714fecbcba2cee6e5ab957/manifest.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/zP5vjLD/knesset.png",HAKNESSET 99 כנסת (backlink)
http://contactgbs.mmdlive.lldns.net/contactgbs/a40693c59c714fecbcba2cee6e5ab957/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/zP5vjLD/knesset.png",HAKNESSET 99 כנסת (backlink)
https://contactgbs.mmdlive.lldns.net/contactgbs/ed17ad332cc146d78a8a8a7a48d9771b/manifest.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/zP5vjLD/knesset.png",HAKNESSET 99 כנסת (backlink)
https://contactgbs.mmdlive.lldns.net/contactgbs/a40693c59c714fecbcba2cee6e5ab957/chunklist_b1128000.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/zP5vjLD/knesset.png",HAKNESSET 99 כנסת (backlink)
https://contact.gostreaming.tv/Accessibility/myStream/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/zP5vjLD/knesset.png",HAKNESSET 99 כנסת (backlink)
https://contact.gostreaming.tv/Knesset/myStream/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/5TQ4RM3/Keshet12.png",KESHET 12 קשת [find-host]
https://PuthereYourserverHostaddress/k12.php?m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/5TQ4RM3/Keshet12.png",KESHET 12 קשת [find-host]
https://PuthereYourserverHostaddress/k12dvr.php?m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/5TQ4RM3/Keshet12.png",KESHET 12 קשת [find-host]
https://PuthereYourserverHostaddress/k12cc.php?m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/7nYM8MK/arutz24tvtrp.png",MAKO 24 ערוץ [find-host]
https://PuthereYourserverHostaddress/ch24.php?m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/1rSGfFw/N12n.png",NEWS 12 חדשות [find-host/offline]
https://PuthereYourserverHostaddress/n12.php?m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/4g6BSYf/now14smgri.png",NOW 14 עכשיו [deadlink]
https://ch14-channel14.akamaized.net/hls/live/2097589/CH14_CHANNEL14/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/4g6BSYf/now14smgri.png",NOW 14 עכשיו [deadlink]
https://ch14-channel14eur.akamaized.net/hls/live/2099700/CH14_CHANNEL14/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/4g6BSYf/now14smgri.png",NOW 14 עכשיו [deadlink]
https://now14.g-mana.live/media/91517161-44ab-4e46-af70-e9fe26117d2e/mainManifest.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/PYtP8fm/arutz9ru.png",ISRAEL 9TV канал [diedlink]
https://contactgbs.mmdlive.lldns.net/contactgbs/dd4f5f04932345f1b47c4bfb45fbd682/manifest.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/5TQ4RM3/Keshet12.png",KESHET 12 קשת [mako-src]
https://mako-streaming.akamaized.net/direct/hls/live/2035325/k12cc/index.m3u8?hdnea=
#EXTINF:-1 tvg-logo="https://i.ibb.co/5TQ4RM3/Keshet12.png",KESHET 12 קשת [mako-src]
https://mako-streaming.akamaized.net/direct/hls/live/2033791/k12/index.m3u8?hdnea=
#EXTINF:-1 tvg-logo="https://i.ibb.co/5TQ4RM3/Keshet12.png",KESHET 12 קשת [mako-src]
https://mako-streaming.akamaized.net/direct/hls/live/2033791/k12dvr/index.m3u8?hdnea=
#EXTINF:-1 tvg-logo="https://i.ibb.co/5TQ4RM3/Keshet12.png",KESHET 12 קשת [frame-issue]
http://mako-streaming.akamaized.net/direct/hls/live/2033791/k12dvr/index_4000_I-Frame.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/7nYM8MK/arutz24tvtrp.png",MAKO 24 ערוץ [mako-src]
https://mako-streaming.akamaized.net/direct/hls/live/2035340/ch24live/index.m3u8?hdnea=
#EXTINF:-1 tvg-logo="https://i.ibb.co/1rSGfFw/N12n.png",NEWS 12 חדשות [mako-src/offline]
https://mako-streaming.akamaized.net/n12/hls/live/2041434/n12s/index.m3u8?hdnea=


#EXTINF:-1 tvg-logo="https://i.ibb.co/s107QNv/araby2.png" group-title="17. |AR|🇸🇦 MIDDLE EAST-1 عربي",AL ALARABY 2
https://alaraby.cdn.octivid.com/alaraby2n/smil:alaraby2n.stream.smil/chunklist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/s107QNv/araby2.png",AL ALARABY 2
https://alarabyta.cdn.octivid.com/alaraby2n/smil:alaraby2n.stream.smil/chunklist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/F3rnLz2/mtvleb.png",MURR LBN
https://hms.pfs.gdn/v1/broadcast/mtv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/vJj1gdb/onetvlb.jpg",ONE LBN
https://hms.pfs.gdn/v1/broadcast/one/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/zH7W9tX/volbn.png",VOICE OF LBN
https://svs.itworkscdn.net/vdltvlive/vdltv.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/ZB8x8TP/futlbn.png",FUTURE LBN
https://live.kwikmotion.com/futurelive/ftv.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/wR2jkMz/nbnlb.png",NBN
http://5.9.119.146:8883/nbn/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/wR2jkMz/nbnlb.png" referer="https://odysee.com",NBN
https://cloud.odysee.live/content/1d8edd84bd42e695555dbf20d83b45e203ed9ed0/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/ygKx229/lana1.png",LANA TV
https://p-ltv.akamaized.net/ltv/ltv.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/JrFjqrc/nabaa.png",NABAA TV
https://655ca86f46b1f.streamlock.net/live/Nabaa/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/h872gKg/taha.png",TAHA TV
https://media2.livaat.com/TAHA-TV/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/h872gKg/taha.png",TAHA TV
https://media2.livaat.com/TAHA-TV/index.fmp4.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/80JQ9zg/teleliban.webp" referer="https://www.teleliban.com.lb/live",TL LIBAN
https://cdn.catiacast.video/abr/ed8f807e2548db4507d2a6f4ba0c4a06/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/YhMgggj/lbcb.jpg" referer="https://rotana.net/",LBC LBN
https://rotana.hibridcdn.net/rotananet/lbc_net-7Y83PP5adWixDF93/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Svnqq8G/otv.jpg",OTV LBN
http://185.9.2.18/chid_312/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/hM98B0V/jadeed.png",AL JADEED
http://185.9.2.18/chid_391/mono.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/XVGL3qH/alaan.png",AL AAN TV
https://shls-live-ak.akamaized.net/out/v1/dfbdea4c1bf149629764e58c6ff314c8/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/HVLDcrR/abudhabi.png",ABU DHABI
https://vo-live.cdb.cdn.orange.com/Content/Channel/AbuDhabiChannel/HLS/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/yV6Jhjg/alemarat.png",AL EMARAT
https://vo-live.cdb.cdn.orange.com/Content/Channel/EmiratesChannel/HLS/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/L61bf70/adspts.png",ABU DHABI SPORTS 1
https://vo-live-media.cdb.cdn.orange.com/Content/Channel/AbuDhabiSportsChannel1/HLS/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/L61bf70/adspts.png",ABU DHABI SPORTS 2
https://vo-live.cdb.cdn.orange.com/Content/Channel/AbuDhabiSportsChannel2/HLS/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Q6tZWdh/yas.png",YAS TV
https://vo-live.cdb.cdn.orange.com/Content/Channel/YASSportsChannel/HLS/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/GdpWZ7h/baynounah.png",BAYNOUNAH TV
https://vo-live.cdb.cdn.orange.com/Content/Channel/Baynounah/HLS/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Dr7jn2L/baynounah.png",BAYNOUNAH TV
https://baynounah.cdn.mangomolo.com/btv/smil:btv.stream.smil/chunklist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/b2KHBPn/halalnd.png",HALA LONDON
https://halalondon-live.ercdn.net/halalondon/halalondon.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mCBL5fNk/lybiawat.jpg",LIBYA WATANYA
https://cdn-globecast.akamaized.net/live/eds/libya_al_watanya/hls_roku/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/qJ7qVTF/Al-Mamlaka.png",AL MAMLKA
https://bcovlive-a.akamaihd.net/4109c7ba30fd4a44ad9afe917c67a8c8/eu-central-1/6415809151001/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/5LvvstB/elshasha.png",SYDAT EL SHASHA
https://daiconnect.com/live/hls/rotana/selshasha/.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/b6ZvV2r/fujairah.png",FUJAIRAH TV
https://live.kwikmotion.com/fujairahlive/fujairah.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/84HtHzK/Roya-TV.png",ROYA TV
https://royatv-live.daioncdn.net/royatv/royatv.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/3mfSV6R6/almasar.jpg",AL MASAR
https://starmenajo.com/hls/almasar/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/DtWPcjN/alw.png",ALAWLA TV
https://63b03f7689049.streamlock.net/live/1tv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/HtKQ15z/alw1.png",ALAWLA TV
https://63b03f7689049.streamlock.net/live/_definst_/1tv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Lh6wp1q4/assirat.png",ASSIRAT
https://softverse.b-cdn.net/Assirat/assiratobs/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/nnQnFjg/sharjahtv.png",SHARJAH TV
https://svs.itworkscdn.net/smc1live/smc1.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/nnQnFjg/sharjahtv.png",SHARJAH TV
https://cdn-globecast.akamaized.net/live/eds/sharjah_tv/hls_roku/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/7KSJQYX/sharjah2.png",SHARJAH TV 2
https://svs.itworkscdn.net/smc2live/smc2tv.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/1bpYYZ2/shrspt.png",SHARJAH TV SPORTS
https://svs.itworkscdn.net/smc4sportslive/smc4.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/x8ftqHr/qattv.png",QATAR TV
https://qatartv.akamaized.net/hls/live/2026573/qtv1/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/x8ftqHr/qattv.png",QATAR TV
https://live.kwikmotion.com/qtv1live/qtv1.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/y4qNK42/qattv2.png",QATAR TV 2
https://qatartv.akamaized.net/hls/live/2026574/qtv2/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/y4qNK42/qattv2.png",QATAR TV 2
https://live.kwikmotion.com/qtv2live/qtv2.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/d58T05P/Syria-tv.jpg",SYRIA TV
https://svs.itworkscdn.net/syriatvlive/syriatv.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/d58T05P/Syria-tv.jpg",SYRIA TV
https://stream.ads.ottera.tv/playlist.m3u8?network_id=6017
#EXTINF:-1 tvg-logo="https://i.ibb.co/d58T05P/Syria-tv.jpg",SYRIA TV
https://live.kwikmotion.com/syriatvlive/syriatv.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/0kQdg9X/syria2.png",SYRIA TV 2
https://live.kwikmotion.com/syriatv02live/syriatv02.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/XrC6F6JW/salam.png",SALAM
https://amsart-live.ercdn.net/salamtv/salamtv.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/QPv27Qc/wtw.jpg",AL WASAT TV
https://alwasattv.hibridcdn.net/alwasattv/alwasat_abr/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/dp728rg/rayan.png",AL RAYYAN
https://alrayyancdn.vidgyor.com/pub-nooldraybinbdh/liveabr/playlist_dvr.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/n333gP9/rayanqdm.png",AL RAYYAN QADEEM
https://alrayyancdn.vidgyor.com/pub-noalrayy3pwz0l/liveabr/playlist_dvr.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/1KcjbKf/almayadeen.png",AL MAYADEEN
https://mdnlv.cdn.octivid.com/almdn/smil:mpegts.stream.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/gZKY6Tn/almanar.png",AL MANAR
https://edge.fastpublish.me/live/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mN2JhVS/alghad.png",AL GHAD TV
https://eazyvwqssi.erbvr.com/alghadtv/alghadtv.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mN2JhVS/alghad.png",AL GHAD PLUS
https://playlist.fasttvcdn.com/pl/ykvm3f2fhokwxqsurp9xcg/alghad-plus/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/4Vfg55v/almasira.png",AL MASIRA
https://svs.itworkscdn.net/almasiralive/almasira.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/zGHHGbj/alkhalij.jpg",AL KHALIJ TV
https://mn-nl.mncdn.com/khalij/khalij/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/MG43H4H/hala.png",PANET 30 HALA
https://live1.panet.co.il/edge_abr/halaTV/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/MG43H4H/hala.png",PANET 30 HALA
https://gstream4.panet.co.il/edge/halaTV/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/fqTYrGY/33.png",KAN 33 MAKAN
https://makan.media.kan.org.il/hls/live/2024680/2024680/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/S6xK2x9/aone.jpg",A ONE
http://master.starmena-cloud.com/hls/a1jo.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/qMyBBdb/kab.png",KAB 1
https://svs.itworkscdn.net/kablatvlive/kabtv1.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/fFZ3kZj/alwousta.png",AL WOUSTA
https://svs.itworkscdn.net/alwoustalive/alwoustatv.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/5TZPHf6/atfal.jpg",ATFAL
https://5d658d7e9f562.streamlock.net/atfal1.com/atfal2/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/sKJGV9q/Ajman.jpg",AJMAN TV
https://cdn1.logichost.in/ajmantv/live/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Y7PcRQCG/sudan.png",SUDAN TV
https://cdn-globecast.akamaized.net/live/eds/sudan_tv/hls_roku/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/svNjxMqW/dabanga.png",DABANGA
https://hls.dabangasudan.org/hls/stream.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/vm3481D/amman.png",AMMAN TV
https://ammantv-live.ercdn.net/ammantvhd/ammantvhd.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/C2c1NJN/alraimedia.png",ALRAIMEDIA
https://svs.itworkscdn.net/alraitvlive/alraitv.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/C2c1NJN/alraimedia.png",ALRAIMEDIA
https://new.cache-stream.workers.dev/stream/UCTny7s_VPsTS_TtnWIlJF6w/live.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/0mtj39x/Mekameleen.png",MEKAMELEEN
http://mn-nl.mncdn.com/mekameleen/smil:mekameleentv.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/kDhcymF/ifilm.png",IFILM AR
https://live.presstv.ir/hls/ifilmar_4_482/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/kDhcymF/ifilm.png",IFILM AR
https://ncdn.telewebion.com/ifilmar/live/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/gZ1q6zP9/ontve.png",ON E
https://bcovlive-a.akamaihd.net/3dc60bab470f4c9fbf00408ecb7c3d7a/eu-west-1/6057955906001/playlist_dvr.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mVPZh6Gz/Aliraqia.jpg",AL IRAQIA
https://cdn.catiacast.video/abr/8d2ffb0aba244e8d9101a9488a7daa05/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/99cj3D4g/Masirah.jpg",AL MASIRAH
https://live.cdnbridge.tv/Almasirah/Almasirah_all/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/HCZGRZk/bahraintv.png",BAHRAIN TV
https://5c7b683162943.streamlock.net/live/ngrp:bahraintvmain_all/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/HCZGRZk/bahraintv.png",BAHRAIN TV INT
https://5c7b683162943.streamlock.net/live/ngrp:bahraininternational_all/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/M9MzqDm/bedaya.png",BEDAYA TV
https://shls-live-enc.edgenextcdn.net/out/v1/97427be47b79457b9ca245e22a8db23a/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/VCfg2xY/almahriah.png",YEMEN MAHRIAH
https://starmenajo.com/hls/almahriah/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/PFCf0SG/jaylia.jpg",AL JAYLIA
https://media2.livaat.com/AL-Jaleyah/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/740Znb4/ittihad.png",ETIHAD
https://live.alittihad.tv:444/ittihad/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/GT1LMyS/thaqafeyyah.webp",THAQAFEYYAH
https://thaqafeyyah-ak.akamaized.net/out/v1/f6851f68ada94f82ae6b64a441eb5ab1/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/PYwbLwJ/haqiqat.jpg",AL HAQIQA
https://jmc-live.ercdn.net/alhaqiqa/alhaqiqa.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Lkwk0zB/almashd.png",AL MASHHAD
https://bcovlive-a.akamaihd.net/20c3ca22be3c4f03b30afbf3c92cfd14/ap-south-1/6313884884001/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Lkwk0zB/almashd.png",AL MASHHAD
https://bcovlive-a.akamaihd.net/385ca06841b3430f99327f0c44d6d008/ap-south-1/6313884884001/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/2KwY06R/alyaum.png",AL YAUM
https://alyaum-tv.akamaized.net/hls/alyaum-tv.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/2KwY06R/alyaum.png",AL YAUM
https://iko-live.akamaized.net/AlyuamTV/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/nPBCcKq/payam.jpg",PAYAM TV
https://media2.streambrothers.com:1936/8218/8218/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/f2XWR2M/alrabiaa.jpg" referer="https://player.castr.com/",AL RABIAA
https://stream.castr.com/65045e4aba85cfe0025e4a60/live_c6c4040053cd11ee95b47153d2861736/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/f2XWR2M/alrabiaa.jpg",AL RABIAA
https://206222.global.ssl.fastly.net/65045e4aba85cfe0025e4a60/live_c6c4040053cd11ee95b47153d2861736/index.fmp4.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mcd2S4f/samaatv.png",SAMA TV
https://app.sama-tv.net/hls/samatv.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/FYdQXH1/aldafrah.png",AL DAFRAH
https://rtmp-live-ingest-eu-west-3-universe-dacast-com.akamaized.net/transmuxv1/streams/dbb8ac05-a020-784c-3a95-6ed027941532.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/gJcnzXw/rajeen.png",RAJEEN
https://mn-nl.mncdn.com/palabroad/live/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/4g4VNx7/quds-tv.png",QUDS TV
http://live.alqudstoday.tv:8080/hls/alqudstv/alqudstv.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/RS72QHZ/pbcpalestine.png",PAL PBC
https://pbc.furrera.ps/palestinehd/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/RS72QHZ/pbcpalestine.png",PAL PBC
https://pbc.furrera.ps/palestinelivehd/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/r5FwmZQ/musawa.png",MUSAWA
https://pbc.furrera.ps/musawahd/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/TMFyykR/paltv.png",PAL TV
https://live.paltodaytv.com/paltv/live/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/nkfS0P4/palsat.jpg",PAL SAT
http://htvpalsat.mada.ps:8888/audeh/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/nkfS0P4/palsat.jpg",WATAR PS
http://htvint.mada.ps:8889/orient/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/nkfS0P4/palsat.jpg",WATAR PS
https://htvint.mada.ps/orient/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/RNHM3Xx/falastini.png",FALASTINI TV
https://rp.tactivemedia.com/falastinitv/live/chunks.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/RNHM3Xx/falastini.png",PALESTINIAN TV
https://rp.tactivemedia.com/palestiniantv_source/live/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/0yytb9K/yementoday.png",YEMEN TODAY
https://video.yementdy.tv/hls/yementoday.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/230j3Kr/yemenshabab.png",YEMEN SHABAB
https://starmenajo.com/hls/yemenshabab/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/wK6B1QV/utv.png",UTV IRAQI
https://mn-nl.mncdn.com/utviraqi2/64c80359/chunklist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/8jK0ZR5/alrasheed.png",AL RASHEED
https://media1.livaat.com/AL-RASHEED-HD/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/8jK0ZR5/alrasheed.png",AL RASHEED
https://media1.livaat.com/static/AL-RASHEED-HD/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/MfLxCY6/alrafidain.png",AL RAFIDAIN
https://arrafidain.tvplayer.online/arrafidaintv/source/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/MfLxCY6/alrafidain.png",AL RAFIDAIN
https://arrafidain.tvplayer.online/arrafidaintv/source2/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/zSv52T7/watanegypt.png",WATAN EGYPT
https://n101.stream.tactivemedia.com/watantv/live/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/b5gcrBs4/Alshoob.jpg",AL SHOOB
https://alshoobtv.rp.tactivemedia.com/alshoobtv/live/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mFb5JL3/qaftv.png",QAF
https://mn-nl.mncdn.com/qaf/live/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/zGS6X8G/ssad.jpg",SSAD TV
https://www.enterweb.tv:25463/live/ssadtv/live-tv/1.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/ZNQPS3x/Ishtar.jpg",ISHTAR TV
http://ishtar.cdncast.xyz:1935/live/iShtarHD/chunklist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/CQjzKk9/alsabah.png",AL SABAH KW
https://ffs1.gulfsat.com/Al-Sabah-TV/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/ygKx229/lana1.png",LANA TV (backup)
https://eitc3.secure2.footprint.net/hls/LTV.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/s107QNv/araby2.png",AL ALARABY 2 (backup)
https://stream.ads.ottera.tv/playlist.m3u8?network_id=5617
#EXTINF:-1 tvg-logo="https://i.ibb.co/s107QNv/araby2.png",AL ALARABY 2 (backup)
https://stream.ads.ottera.tv/cl/250113cu26vu63iomqklmptvfg/1280x720_2000000_0_f.m3u8?i=475_5617
#EXTINF:-1 tvg-logo="https://i.ibb.co/s107QNv/araby2.png",AL ALARABY 2 (backup)
https://origin-cae-t482536.cdn.nextologies.com/63d8c759c5db83b4/25c4f89d27a79014ALA2306/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/84HtHzK/Roya-TV.png",ROYA TV (backup)
https://roya.daioncdn.net/royatv/royatv.m3u8?app=8c1e143a-39cf-40b4-acb2-e78faa1f322d
#EXTINF:-1 tvg-logo="https://i.ibb.co/84HtHzK/Roya-TV.png",ROYA TV (backup)
https://roya-live.ercdn.net/roya/roya.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/84HtHzK/Roya-TV.png",ROYA TV (backup)
https://weyyak-live.akamaized.net/weyyak_roya/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/F3rnLz2/mtvleb.png",MTV LBN
https://hms.pfs.gdn/hms/v1/stream/mtv.m3u8?token=m67zo
#EXTINF:-1 tvg-logo="https://i.ibb.co/F3rnLz2/mtvleb.png" user-agent="Mozilla/5.0",MTV_LBN [offline]
https://live.3cd.io/v1/broadcast/mtv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/vJj1gdb/onetvlb.jpg" user-agent="Mozilla/5.0",ONE TV_LBN [offline]
https://live.3cd.io/v1/broadcast/one/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/vJj1gdb/onetvlb.jpg",ONE TV LBN
https://hms.pfs.gdn/hms/v1/stream/mtv.m3u8?token=4c8RZ
#EXTINF:-1 tvg-logo="https://i.ibb.co/YhMgggj/lbcb.jpg",LBC LBN [geoblocked]
https://daiconnect.com/live/hls/rotana/lbc-cdn/.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Svnqq8G/otv.jpg",OTV LBN [brokenlink]
http://62.182.82.104/OTV/tracks-v1a1/mono.m3u8?token=test


#EXTINF:-1 tvg-logo="https://i.ibb.co/BCK1L31/DubaiTV.png" group-title="18. |AR|🇸🇦 MIDDLE EAST-2 عربي",DUBAI TV
https://dmieigthvllta.cdn.mgmlcdn.com/dubaitvht/smil:dubaitv.stream.smil/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/BCK1L31/DubaiTV.png",DUBAI TV
https://dmieigthvllta.cdn.mangomolo.com/dubaitvht/smil:dubaitv.stream.smil/chunklist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/ngKnxmq/dubaione.png",DUBAI ONE
https://dminnvllta.cdn.mgmlcdn.com/dubaione/smil:dubaione.stream.smil/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/ngKnxmq/dubaione.png",DUBAI ONE
https://dminnvllta.cdn.mgmlcdn.com/dubaione/smil:dubaione.stream.smil/playlist.m3u?m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/jMsSmvg/dubainoor.png",DUBAI NOOR
https://dmiffthftl.cdn.mangomolo.com/noordubaitv/smil:noordubaitv.smil/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/g4LTFCS/dubaisama.png",DUBAI SAMA
https://dmieigthvllta.cdn.mgmlcdn.com/samadubaiht/smil:samadubai.stream.smil/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/xDs4dGV/dubaizaman.png",DUBAI ZAMAN
https://dmiffthftl.cdn.mangomolo.com/dubaizaman/smil:dubaizaman.stream.smil/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/LR2KqPJ/dbaispt.png",DUBAI SPORTS 1
https://dmidspta.cdn.mangomolo.com/dubaisports/smil:dubaisports.stream.smil/playlist.m3u?m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/LR2KqPJ/dbaispt.png",DUBAI SPORTS 1
https://dmidspta.cdn.mgmlcdn.com/dubaisports/smil:dubaisports.stream.smil/chunklist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/LR2KqPJ/dbaispt.png",DUBAI SPORTS 2
https://dmitwlvvll.cdn.mangomolo.com/dubaisportshd/smil:dubaisportshd.smil/playlist.m3u?m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/LR2KqPJ/dbaispt.png",DUBAI SPORTS 2
https://dmitwlvvll.cdn.mgmlcdn.com/dubaisportshd/smil:dubaisportshd.smil/chunklist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/LR2KqPJ/dbaispt.png",DUBAI SPORTS 3
https://dmitwlvvll.cdn.mangomolo.com/dubaisportshd5/smil:dubaisportshd5.smil/playlist.m3u?m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/LR2KqPJ/dbaispt.png",DUBAI SPORTS 3
https://dmitwlvvll.cdn.mgmlcdn.com/dubaisportshd5/smil:dubaisportshd5.smil/chunklist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/MD9vwnv/dubairacing.png",DUBAI RACING 1
https://dmisdracta.cdn.mgmlcdn.com/events/smil:events.stream.smil/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/MD9vwnv/dubairacing.png",DUBAI RACING 2
https://dmithrvllta.cdn.mgmlcdn.com/dubairacing/smil:dubairacing.smil/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/MD9vwnv/dubairacing.png",DUBAI RACING 3
https://dmithrvllta.cdn.mgmlcdn.com/dubaimubasher/smil:dubaimubasher.smil/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/3h4XCtZ/kasqatar.png",KAS QATAR 1
https://liveakgr.alkassdigital.net/hls/live/2097037/Alkass1mhu/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/3h4XCtZ/kasqatar.png",KAS QATAR 2
https://liveakgr.alkassdigital.net/hls/live/2097037/Alkass2hef/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/3h4XCtZ/kasqatar.png",KAS QATAR 3
https://liveakgr.alkassdigital.net/hls/live/2097037/Alkass3vak/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/3h4XCtZ/kasqatar.png",KAS QATAR 4
https://liveakgr.alkassdigital.net/hls/live/2097037/Alkass4cn/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/3h4XCtZ/kasqatar.png",KAS QATAR 5
https://liveakgr.alkassdigital.net/hls/live/2097037/Alkass5nnha/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/3h4XCtZ/kasqatar.png",KAS QATAR 5
https://liveakgr.alkassdigital.net/hls/live/2097037/Alkass5xtgb/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/3h4XCtZ/kasqatar.png",KAS QATAR 6
https://liveakgr.alkassdigital.net/hls/live/2097037/Alkass6buzay/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/3h4XCtZ/kasqatar.png",KAS QATAR 6
https://liveakgr.alkassdigital.net/hls/live/2097037/Alkass6buzat/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/3h4XCtZ/kasqatar.png",KAS QATAR SHOOF
https://liveakgr.alkassdigital.net/hls/live/2097037/Alkass6Shoof1/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/WcQV072/saudi1sbc.png",SAUDI SBC SA
https://sbc-prod-dub-ak.akamaized.net/out/v1/2eb1ad0f29984a339bc0fce4ce94dcbb/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/WcQV072/saudi1sbc.png",SAUDI SBC SA
https://shd-gcp-live.edgenextcdn.net/live/bitmovin-sbc/90e09c0c28db26435799b4a14892a167/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/qNXgWyZ/sauditv.jpg",SAUDIA TV CH 1
https://shls-masr2-ak.akamaized.net/out/v1/5ae66b453b62403199811ab78da9982a/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/qNXgWyZ/sauditv.jpg",SAUDIA TV CH 1
https://saudi-tv-prod-dub-enc.edgenextcdn.net/out/v1/5ae66b453b62403199811ab78da9982a/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/qNXgWyZ/sauditv.jpg",SAUDIA TV CH 1
https://cdn-globecast.akamaized.net/live/eds/saudi_tv/hls_roku/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/qNXgWyZ/sauditv.jpg",SAUDIA TV CH 1
https://shd-gcp-live.edgenextcdn.net/live/bitmovin-saudi-tv/2ad66056b51fd8c1b624854623112e43/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/qNXgWyZ/sauditv.jpg",SAUDIA TV KSA NOW
https://shd-gcp-live.edgenextcdn.net/live/bitmovin-ksa-now/71ed3aa814c643306c0a8bc4fcc7d17f/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/6PH6566/thikrayat.jpg",SAUDIA THIKRAYAT
https://al-ekhbaria-prod-dub.shahid.net/out/v1/ef87956651694f4ba2ccc16e852dbb95/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/c6QBhj8/actionwalid.png",SAUDI ACTION WALEED
https://shls-live-event2-prod-dub.shahid.net/out/v1/0456ede1a39145d98b3d8c8062ddc998/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/GJVSFNt/oman.png",OMAN 1
https://partneta.cdn.mgmlcdn.com/omantv/smil:omantv.stream.smil/chunklist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/GJVSFNt/oman.png",OMAN MUNASHER
https://partwota.cdn.mgmlcdn.com/omlive/smil:omlive.stream.smil/chunklist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/GJVSFNt/oman.png",OMAN CULTURE
https://partwota.cdn.mgmlcdn.com/omcultural/smil:omcultural.stream.smil/chunklist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/GJVSFNt/oman.png",OMAN SPORT
https://partneta.cdn.mgmlcdn.com/omsport/smil:omsport.stream.smil/chunklist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/GJVSFNt/oman.png",OMAN TV
https://cdn-globecast.akamaized.net/live/eds/oman_tv/hls_roku/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/y4xS49d/jordan-tv.png",JORDAN TV
https://jrtv-live.ercdn.net/jordanhd/jordanhd.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/y4xS49d/jordan-tv.png",JORDAN TOURISM
https://playlist.fasttvcdn.com/pl/cc0blorawy1ibohhrupraa/Tourism/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/y4xS49d/jordan-tv.png",JORDAN DRAMA
https://playlist.fasttvcdn.com/pl/cc0blorawy1ibohhrupraa/Drama/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/y4xS49d/jordan-tv.png",JORDAN COMEDY
https://playlist.fasttvcdn.com/pl/cc0blorawy1ibohhrupraa/Comedy/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/y4xS49d/jordan-tv.png",JORDAN KITCHEN
https://playlist.fasttvcdn.com/pl/cc0blorawy1ibohhrupraa/cooking/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/y4xS49d/jordan-tv.png",JORDAN ARCHIVE
https://playlist.fasttvcdn.com/pl/cc0blorawy1ibohhrupraa/Archive/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/y4xS49d/jordan-tv.png",JORDAN SONG
https://playlist.fasttvcdn.com/pl/cc0blorawy1ibohhrupraa/Song/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tMLDMdy/kwttv.png",KUWAIT TV 1
https://kwtktv1ta.cdn.mangomolo.com/ktv1/smil:ktv1.stream.smil/chunklist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tMLDMdy/kwttv.png",KUWAIT TV 2
https://kwtktv2ta.cdn.mangomolo.com/ktv2/smil:ktv2.stream.smil/chunklist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tMLDMdy/kwttv.png",KUWAIT TV NEWS
https://kwtktvata.cdn.mangomolo.com/ktva/smil:ktva.stream.smil/chunklist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tMLDMdy/kwttv.png",KUWAIT TV ARAB
https://kwtktvata.cdn.mangomolo.com/ktva/smil:tktva.stream.smil/chunklist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tMLDMdy/kwttv.png",KUWAIT TV ETHRAA
https://kwtethta.cdn.mangomolo.com/eth/smil:eth.stream.smil/chunklist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tMLDMdy/kwttv.png",KUWAIT TV KHALLIK
https://kwtkbta.cdn.mangomolo.com/kb/smil:kb.stream.smil/chunklist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tMLDMdy/kwttv.png",KUWAIT TV KHALLIK
https://kwtsplta.cdn.mangomolo.com/kb/smil:kb.stream.smil/chunklist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tMLDMdy/kwttv.png",KUWAIT TV QURAIN
https://kwtktvaqta.cdn.mangomolo.com/ktvaq/smil:tktvaq.stream.smil/chunklist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tMLDMdy/kwttv.png",KUWAIT TV SPORTS
https://kwtspta.cdn.mangomolo.com/sp/smil:sp.stream.smil/chunklist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tMLDMdy/kwttv.png",KUWAIT TV SPORT PLUS
https://kwtsplta.cdn.mangomolo.com/spl/smil:spl.stream.smil/chunklist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tMLDMdy/kwttv.png",KUWAIT TV SPORT EXTRA
https://kwtalmta.cdn.mangomolo.com/alm/smil:alm.stream.smil/chunklist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tMLDMdy/kwttv.png",KUWAIT TV 1
https://cdn-globecast.akamaized.net/live/eds/kuwait_tv1/hls_roku/index.m3u8
#EXTINF:-1 group-title="18. |AR|🇸🇦 MIDDLE EAST-2 عربي",--- |⬇DOWN/OFFLINES⬇| ---
http://blank
#EXTINF:-1 tvg-logo="https://i.ibb.co/WcQV072/saudi1sbc.png",SAUDI CH 1
https://edge.taghtia.com/sa/1.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/T0Rc9mJ/saudi2.png",SAUDI CH 2
https://edge.taghtia.com/sa/2.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mtqZsZ4/saudi3.png",SAUDI CH 3
https://edge.taghtia.com/sa/3.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/jh0s9P6/saudich4.png",SAUDI CH 4
https://edge.taghtia.com/sa/4.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/FwDhYDv/saudi6.png",SAUDI CH 6 SUNNAH
https://edge.taghtia.com/sa/6.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/9p3b0MW/saudi7.png",SAUDI CH 7 KABE
https://edge.taghtia.com/sa/7.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/qNXgWyZ/sauditv.jpg",SAUDI CH 9
https://edge.taghtia.com/sa/9.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/qNXgWyZ/sauditv.jpg",SAUDI CH 10
https://edge.taghtia.com/sa/10.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/qNXgWyZ/sauditv.jpg",SAUDI CH 17
https://edge.taghtia.com/sa/17.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/3h4XCtZ/kasqatar.png",KAS QATAR 1
https://liveakgr.alkassdigital.net/hls/live/2097037/Alkass1xtgb/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/3h4XCtZ/kasqatar.png",KAS QATAR 1
https://liveakgr.alkassdigital.net/hls/live/2097037/Alkass1ctfsd/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/3h4XCtZ/kasqatar.png",KAS QATAR 2
https://liveakgr.alkassdigital.net/hls/live/2097037/Alkass2uyce/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/3h4XCtZ/kasqatar.png",KAS QATAR 2
https://liveakgr.alkassdigital.net/hls/live/2097037/Alkass2nbcq/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/3h4XCtZ/kasqatar.png",KAS QATAR 3
https://liveakgr.alkassdigital.net/hls/live/2097037/Alkass3lavya/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/3h4XCtZ/kasqatar.png",KAS QATAR 3
https://liveakgr.alkassdigital.net/hls/live/2097037/Alkass3actfsdc/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/3h4XCtZ/kasqatar.png",KAS QATAR 4
https://liveakgr.alkassdigital.net/hls/live/2097037/Alkass4xtgb/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/3h4XCtZ/kasqatar.png",KAS QATAR 4
https://liveak.alkassdigital.net/livehttporigin/smil:YWxrYXNh2.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/3h4XCtZ/kasqatar.png",KAS QATAR 5
https://liveakgr.alkassdigital.net/hls/live/2097037/Alkass5xtgb/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/3h4XCtZ/kasqatar.png",KAS QATAR 6
https://liveakgr.alkassdigital.net/hls/live/2097037/Alkass6laq/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/3h4XCtZ/kasqatar.png",KAS QATAR 1
https://liveakgr.alkassdigital.net/hls/live/2097037/Alkass1bup/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/3h4XCtZ/kasqatar.png",KAS QATAR 2
https://liveakgr.alkassdigital.net/hls/live/2097037/Alkass2hgof/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/3h4XCtZ/kasqatar.png",KAS QATAR 3
https://liveakgr.alkassdigital.net/hls/live/2097037/Alkass3pzrjl/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/3h4XCtZ/kasqatar.png",KAS QATAR 4
https://liveakgr.alkassdigital.net/hls/live/2097037/Alkass4xiuytgfficcn/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/3h4XCtZ/kasqatar.png",KAS QATAR 5
https://liveakgr.alkassdigital.net/hls/live/2097037/Alkass5xtyuwqa/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/3h4XCtZ/kasqatar.png",KAS QATAR 5
https://liveakgr.alkassdigital.net/hls/live/2097037/Alkass5xtgb/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/3h4XCtZ/kasqatar.png",KAS QATAR 5
https://liveakgr.alkassdigital.net/hls/live/2097037/Alkass5xtwe/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/3h4XCtZ/kasqatar.png",KAS QATAR 6
https://liveakgr.alkassdigital.net/hls/live/2097037/Alkass6xydam/master.m3u8


#EXTINF:-1 tvg-logo="https://i.ibb.co/jLYWYh7/Al-Jazeera.png" group-title="19. |AR|🇸🇦 THEMATICS-1 عربي",AL JAZEERA
http://live-hls-web-aja.getaj.net/AJA/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/jLYWYh7/Al-Jazeera.png",AL JAZEERA
https://live-hls-apps-aja-v3-fa.getaj.net/AJA/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/hcCJkhq/Al-Arabiya.png",AL ARABIYA
https://live.alarabiya.net/alarabiapublish/alarabiya.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/hcCJkhq/Al-Arabiya.png",AL ARABIYA
https://shls-live-ak.akamaized.net/out/v1/f5f319206ed740f9a831f2097c2ead23/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/h27qpLJ/araby1.png",AL ALARABY
https://alarabyta.cdn.octivid.com/alaraby/smil:alaraby.stream.smil/chunklist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/h27qpLJ/araby1.png",AL ALARABY
https://alaraby.cdn.octivid.com/alaraby/smil:alaraby.stream.smil/chunklist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/nc8F1dj/Al-Hadath.png",AL ARABIYA HADATH
https://av.alarabiya.net/alarabiapublish/alhadath.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/nc8F1dj/Al-Hadath.png",AL ARABIYA HADATH
https://shls-hadath-prod-dub.shahid.net/out/v1/0e1a306399c346faac4226aa0858f99b/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/nc8F1dj/Al-Hadath.png",AL ARABIYA HADATH
https://hadath-prod-dub-ak.akamaized.net/out/v1/0e1a306399c346faac4226aa0858f99b/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/R4vMgQV/alarabiyabus.jpg",AL ARABIYA BUSINESS
https://live.alarabiya.net/alarabiapublish/aswaaq.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/R4vMgQV/alarabiyabus.jpg",AL ARABIYA BUSINESS
https://alarabiya-business-ak.akamaized.net/out/v1/126027fa2f8c4d19be4551b77ec08cbb/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/hcCJkhq/Al-Arabiya.png",AL ARABIYA PROGRAMS
https://d1j4r34gq3qw9y.cloudfront.net/out/v1/96804f3a14864641a21c25e8ca9afb74/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/dbFBq5k/Al-Jazeera-Mubasher.png",AL JAZEERA MUBASHER
https://live-hls-web-ajm.getaj.net/AJM/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/dbFBq5k/Al-Jazeera-Mubasher.png",AL JAZEERA MUBASHER
https://live-hls-apps-ajm-v3-fa.getaj.net/AJM/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/dbFBq5k/Al-Jazeera-Mubasher.png",AL JAZEERA MUBASHER 2
https://newajm2.getaj.net/AJM2/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/dbFBq5k/Al-Jazeera-Mubasher.png",AL JAZEERA MUBASHER 2
https://live-hls-web-ajm2-fa.getaj.net/AJM2/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/dbFBq5k/Al-Jazeera-Mubasher.png",AL JAZEERA MUBASHER 24
https://live-hls-web-ajm24-fa.getaj.net/AJM24/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mNnyV1K/alhurra.png",AL HURRA
https://mbnv-video-ingest.akamaized.net/hls/live/2038904/MBNV_ALHURRA_MAIN_HLS/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mNnyV1K/alhurra.png",AL HURRA
https://mbn-ingest-worldsafe.akamaized.net/hls/live/2038900/MBN_Alhurra_Worldsafe_HLS/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/CMk8DS1/alqahera.png",AL QAHERA NEWS
https://bcovlive-a.akamaihd.net/d30cbb3350af4cb7a6e05b9eb1bfd850/eu-west-1/6057955906001/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/nzjbYfR/asharq.png",ASHARQ NEWS
https://bcovlive-a.akamaihd.net/0b75ef0a49e24704a4ca023d3a82c2df/ap-south-1/6203311941001/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/nzjbYfR/asharq.png",ASHARQ NEWS
https://asharq-prod-dub-ak.akamaized.net/out/v1/3b6b4902cf8747a28619411239584002/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/nzjbYfR/asharq.png",ASHARQ NEWS
https://svs.itworkscdn.net/bloomberarlive/bloomberg.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/84HtHzK/Roya-TV.png",ROYA NEWS
https://raw.githubusercontent.com/MassinDV/Youtube-arabic-channels/main/live/ch39.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/m4tvbmp/inewsar.png",INEWS IQ
https://live.i-news.tv/hls/stream.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/m4tvbmp/inewsar.png",INEWS IQ
https://svs.itworkscdn.net/inewsiqlive/inewsiq.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/JcP5JHq/bbcaranw.png",BBC NEWS ARABIA
https://vs-hls-pushb-ww.live.cf.md.bbci.co.uk/x=4/i=urn:bbc:pips:service:bbc_arabic_tv/mobile_wifi_main_sd_abr_v2.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/JcP5JHq/bbcaranw.png",BBC NEWS ARABIA
https://vs-hls-pushb-ww-live.akamaized.net/x=4/i=urn:bbc:pips:service:bbc_arabic_tv/t=3840/v=pv14/b=5070016/main.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/dGjByMq/Sky-News-Arabia.png",SKY NEWS ARABIA
https://stream.skynewsarabia.com/hls/sna.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/dGjByMq/Sky-News-Arabia.png",SKY NEWS ARABIA
https://stream.skynewsarabia.com/ott/ott.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/FxZYHhM/cnbc.jpg",CNBC ARABIA
https://cnbc-live.akamaized.net/cnbc/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/L8KP0z9/DW-arabic.png",DW ARABIC
https://dwamdstream103.akamaized.net/hls/live/2015526/dwstream103/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/njBtvts/cgtnar.png",CGTN ARABIC
https://news.cgtn.com/resource/live/arabic/cgtn-a.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/j68q1Bp/i24.png",i24 NEWS AR
https://bcovlive-a.akamaihd.net/95116e8d79524d87bf3ac20ba04241e3/eu-central-1/5377161796001/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/hKP8X8B/f24.png",FRANCE 24 AR
https://live.france24.com/hls/live/2037222/F24_AR_HI_HLS/master_5000.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/vPkb8TQ/trtar.png",TRT ARABIYA
https://tv-trtarabi.medya.trt.com.tr/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/XDC5cBX/alalam.png",AL ALAM IR [censure-ifany] 
https://live2.alalam.ir/alalam.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/D7w9h7Q/rt.png",RT ARABIC [censure-blocked]
https://rt-arb.rttv.com/live/rtarab/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/D7w9h7Q/rt.png",RT ARABIC [censure-blocked]
https://rt-arb.rttv.com/dvr/rtarab/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/nzjbYfR/asharq.png",ASHARQ DOCS
https://svs.itworkscdn.net/asharqdocumentarylive/asharqdocumentary.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/nzjbYfR/asharq.png",ASHARQ DOCS 2
https://svs.itworkscdn.net/asharqdiscoverylive/asharqd.smil/playlist_dvr.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Fs6CgPG/Al-Hiwar.png",AL HIWAR
https://mn-nl.mncdn.com/alhiwar_live/smil:alhiwar.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/PNLHyhs/Al-Sharqiya-News.png",AL SHARQIYA
http://ns8.indexforce.com:1935/alsharqiyalive/mystream/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/PNLHyhs/Al-Sharqiya-News.png",AL SHARQIYA
https://5d94523502c2d.streamlock.net/alsharqiyalive/mystream/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/PNLHyhs/Al-Sharqiya-News.png",AL SHARQIYA
https://5d94523502c2d.streamlock.net/home/mystream/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/nMzmrDFJ/Aliraqianews.jpg",AL IRAQIA NEWS
https://cdn.catiacast.video/abr/78054972db7708422595bc96c6e024ac/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tsWQ5pz/panorama.jpg",PANORAMA FM TV
https://panoramafm-prod-dub-ak.akamaized.net/out/v1/66262e420d824475aaae794dc2d69f14/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/H4shFvm/elsharq.png",EL SHARQ
https://mn-nl.mncdn.com/elsharq_live/live/chunklist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/KX5tK6Q/Wanasa.png",WANASAH
https://shls-wanasah-prod-dub.shahid.net/out/v1/c84ef3128e564b74a6a796e8b6287de6/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/DbFpsdR/majid.png",MAJID
https://vo-live.cdb.cdn.orange.com/Content/Channel/MajidChildrenChannel/HLS/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/DbFpsdR/majid.png",MAJID
https://vo-live-media.cdb.cdn.orange.com/Content/Channel/MajidChildrenChannel/HLS/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/QFvZPd9/spacetoon.png",SPACE TOON
https://streams.spacetoon.com/live/stchannel/smil:livesmil.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/QFvZPd9/spacetoon.png",SPACE TOON
https://shls-spacetoon-prod-dub.shahid.net/out/v1/6240b773a3f34cca95d119f9e76aec02/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/QFvZPd9/spacetoon.png",SPACE TOON
https://spacetoon-prod-dub-ak.akamaized.net/out/v1/6240b773a3f34cca95d119f9e76aec02/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/QFvZPd9/spacetoon.png",SPACE TOON
https://shd-gcp-live.edgenextcdn.net/live/bitmovin-spacetoon/d8382fb9ab4b2307058f12c7ea90db54/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/LYMKBP2/Sat7kids.png",SAT7 KIDS
https://svs.itworkscdn.net/sat7kidslive/sat7kids.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/HVLKncL/afarin.png",AFARIN TV
https://65f16f0fdfc51.streamlock.net/afarinTV/livestream/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/k8Xbs2n/alshallal.jpg",AL SHALLAL
https://amg01480-alshallalfze-alshallal-ono-q0hfg.amagi.tv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Ch3FNj9/tenar.jpg",TEN WEYYAK
https://weyyak-live.akamaized.net/weyyak_ten_tv/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/S3Wm3q9/iqraanew.png",IQRAA 1
https://playlist.fasttvcdn.com/pl/dlkqw1ftuvuuzkcb4pxdcg/Iqraafasttv1/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/S3Wm3q9/iqraanew.png",IQRAA 2
https://playlist.fasttvcdn.com/pl/dlkqw1ftuvuuzkcb4pxdcg/Iqraafasttv2/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/S3Wm3q9/iqraanew.png",IQRAA 3
https://playlist.fasttvcdn.com/pl/dlkqw1ftuvuuzkcb4pxdcg/Iqraafasttv3/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/S3Wm3q9/iqraanew.png",IQRAA
https://iqraa-live.ercdn.net/iqraa/iqraa.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/S3Wm3q9/iqraanew.png",IQRAA
https://jmc-live.ercdn.net/iqraa/iqraa.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/S3Wm3q9/iqraanew.png",IQRAA EUR
https://jmc-live.ercdn.net/iqraaeurope/iqraaeurope.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/S3Wm3q9/iqraanew.png",IQRAA 2
https://cdn5.iqsat.net/iqb/f0c1abab1c44d5f01879991c979a6821.sdp/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/GnfgKbs/alquran.png",QURAN
http://m.live.net.sa:1935/live/quran/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/GnfgKbs/alquran.png",QURAN
https://cdn-globecast.akamaized.net/live/eds/saudi_quran/hls_roku/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/cygNtwH/bahrain-quaran.png",BAHRAIN QURAN
https://5c7b683162943.streamlock.net/live/ngrp:bahrainquran_all/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/2qdGPCh/Sharjahtvquran.png",SHARJAH QURAN
https://live.kwikmotion.com/sharjahtvquranlive/shqurantv.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/dQtMFVT/qamar.jpg",AL QAMAR
https://streamer3.premio.link/alqamar/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/ypj95gJ/almasirah.png",ALMASIRA MUBASHER
https://svs.itworkscdn.net/almasiramubacherlive/almasira.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/ypj95gJ/almasirah.png",ALMASIRA MUBASHER
https://live2.cdnbridge.tv/AlmasirahMubasher/Mubasher_All/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/TkVK043/ekbariya.png",AL EKHBARIA
https://al-ekhbaria-prod-dub.shahid.net/out/v1/d443f3203b444032896e3233cb6eaa84/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/TkVK043/ekbariya.png",AL EKHBARIA
https://cdn-globecast.akamaized.net/live/eds/al_ekhbariya/hls_roku/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/TkVK043/ekbariya.png",AL EKHBARIA
https://shd-gcp-live.edgenextcdn.net/live/bitmovin-al-ekhbaria/297b3ef1cd0633ad9cfba7473a686a06/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/MctgDQ8/sunnah.png",AL SUNNAH TV
https://shls-euronews-en-prod-dub.shahid.net/out/v1/b09bbb8d9b684763be4211b088168de7/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/MctgDQ8/sunnah.png",AL SUNNAH TV
https://sbc-prod-dub-enc.edgenextcdn.net/out/v1/b09bbb8d9b684763be4211b088168de7/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/MctgDQ8/sunnah.png",AL SUNNAH TV
http://m.live.net.sa:1935/live/sunnah/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/MctgDQ8/sunnah.png",AL SUNNAH TV
https://cdn-globecast.akamaized.net/live/eds/saudi_sunnah/hls_roku/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Qj9JJTCZ/amhquran.png",AL MAJD HOLY QURAN TV
https://edge66.magictvbox.com/liveApple/al_majd/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/f0cKj4S/kareem.jpg",QURAN KAREEM TV
https://al-ekhbaria-prod-dub.shahid.net/out/v1/9885cab0a3ec4008b53bae57a27ca76b/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/G3xHLRPy/resalah.png" referer="https://rotana.net/",AL RESALAH
https://rotana.hibridcdn.net/rotananet/risala_net-7Y83PP5adWixDF93/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/HPzRmd3/alistiqama.png",AL ISTIQAMA
https://jmc-live.ercdn.net/alistiqama/alistiqama.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Mgm51w6/sat7ara.webp",SAT7 ARABIC
https://svs.itworkscdn.net/sat7arabiclive/sat7arabic.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Tgg3JpC/noursat.png",NOURSAT
https://svs.itworkscdn.net/nour4satlive/livestream/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Tgg3JpC/noursat.png",NOURSAT AL SHARQ
https://svs.itworkscdn.net/nour8satlive/livestream/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Tgg3JpC/noursat.png",NOURSAT AL KODDASS
https://svs.itworkscdn.net/nour1satlive/livestream/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Tgg3JpC/noursat.png",NOURSAT EL SHABEB
https://svs.itworkscdn.net/nour3satlive/livestream/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Tgg3JpC/noursat.png",NOURSAT MARIAM
https://svs.itworkscdn.net/nour9satlive/livestream/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Tgg3JpC/noursat.png",NOURSAT ENG
https://svs.itworkscdn.net/noursatenglive/noursateng.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/St7FsRJ/ctvcop.jpg",CTV COPTIC
https://5aafcc5de91f1.streamlock.net/ctvchannel.tv/ctv.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/St7FsRJ/ctvcop.jpg",CTV COPTIC
https://58cc65c534c67.streamlock.net/ctvchannel.tv/ctv.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mNnyV1K/alhurra.png",AL HURRA (backup)
https://mbn-ingest-worldsafe.akamaized.net/hls/live/2038900/MBN_Alhurra_Worldsafe_HLS/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/nzjbYfR/asharq.png",ASHARQ NEWS (backup)
https://asharq-prod-dub-enc.edgenextcdn.net/out/v1/3b6b4902cf8747a28619411239584002/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/nzjbYfR/asharq.png",ASHARQ NEWS (backup)
https://shls-asharq-prod-dub.shahid.net/out/v1/3b6b4902cf8747a28619411239584002/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/nzjbYfR/asharq.png",ASHARQ NEWS (portrait mode)
https://bcovlive-a.akamaihd.net/ed81ac1118414d4fa893d3a83ccec9be/eu-central-1/6203311941001/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/jLYWYh7/Al-Jazeera.png",AL JAZEERA (backup)
https://d35j504z0x2vu2.cloudfront.net/v1/master/0bc8e8376bd8417a1b6761138aa41c26c7309312/al-jazeera/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/hcCJkhq/Al-Arabiya.png",AL ARABIYA (backup)
https://d35j504z0x2vu2.cloudfront.net/v1/master/0bc8e8376bd8417a1b6761138aa41c26c7309312/al-arabiya/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/hcCJkhq/Al-Arabiya.png",AL ARABIYA (backup)
https://shls-live-enc.edgenextcdn.net/out/v1/f5f319206ed740f9a831f2097c2ead23/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/h27qpLJ/araby1.png",AL ALARABY (backup)
https://origin-cae-t482536.cdn.nextologies.com/6837800d47c40cb2/1544c5accd8e84d5ALA2306/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/h27qpLJ/araby1.png",AL ALARABY (backup)
https://stream.ads.ottera.tv/playlist.m3u8?network_id=5616
#EXTINF:-1 tvg-logo="https://i.ibb.co/h27qpLJ/araby1.png",AL ALARABY (backup)
https://stream.ads.ottera.tv/cl/250113cu2707e7g596f0blb9c0/1280x720_900000_1_f.m3u8?i=475_5616
#EXTINF:-1 tvg-logo="https://i.ibb.co/s107QNv/araby2.png",AL ARABY 2 (part-time)
https://new.cache-stream.workers.dev/stream/UCuCtlmcyOPNqdBf_FfrS7kg/live.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/hKP8X8B/f24.png",FRANCE 24 AR (backup)
https://live.france24.com/hls/live/2037222/F24_AR_HI_HLS/master_2300.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/JcP5JHq/bbcaranw.png",BBC NEWS ARABIA (backup)
https://vs-hls-pushb-ww-live.akamaized.net/x=4/i=urn:bbc:pips:service:bbc_arabic_tv/pc_hd_abr_v2.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/JcP5JHq/bbcaranw.png",BBC NEWS ARABIA (backup)
https://new.cache-stream.workers.dev/stream/UCelk6aHijZq-GJBBB9YpReA/live.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/9nsvXcf/maannews.png",MAAN NEWS [issue]
https://htvmada.mada.ps:4443/maannews/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Zxd0j45/cartoonnetwork.png",CARTOON NETWORK AR [down]
https://shls-cartoon-net-prod-dub.shahid.net/out/v1/dc4aa87372374325a66be458f29eab0f/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Zxd0j45/cartoonnetwork.png",CARTOON NETWORK AR [down]
https://shls-masr2-ak.akamaized.net/out/v1/dc4aa87372374325a66be458f29eab0f/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/PjCYRWx/gulliar.jpg",GULLI ARABI [down]
https://shls-gulli-bil-arabi-prod-dub.shahid.net/out/v1/5454d215afba410c90b233f400730958/index.m3u8


#EXTINF:-1 tvg-logo="https://i.ibb.co/N19JFwZ/mbc.png" group-title="20. |AR|🇸🇦 THEMATICS-2 عربي",MBC 1
https://shls-mbc1na-prod-dub.shahid.net/out/v1/84ab37e99d6e4b16b33c6600f94f6ccb/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/N19JFwZ/mbc.png",MBC 1
https://mbc1-enc.edgenextcdn.net/out/v1/0965e4d7deae49179172426cbfb3bc5e/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/N19JFwZ/mbc.png",MBC 1
https://d3o3cim6uzorb4.cloudfront.net/out/v1/0965e4d7deae49179172426cbfb3bc5e/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/N19JFwZ/mbc.png",MBC 1
https://mbc1-usa-enc.edgenextcdn.net/out/v1/8c1ce74bfd0743aab1026ef5b2aecfa4/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/N19JFwZ/mbc.png",MBC 1 USA
https://mbc-1-usa-ak.akamaized.net/out/v1/8c1ce74bfd0743aab1026ef5b2aecfa4/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/bvbsV1Z/mbc3.png",MBC 3
https://shls-mbc3-prod-dub.shahid.net/out/v1/d5bbe570e1514d3d9a142657d33d85e6/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/bvbsV1Z/mbc3.png",MBC 3
https://mbc3-usa-enc.edgenextcdn.net/out/v1/8bbfec9446d84c9ea0dfa34edede6db9/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/bvbsV1Z/mbc3.png",MBC 3 USA
https://mbc-3-usa-ak.akamaized.net/out/v1/8bbfec9446d84c9ea0dfa34edede6db9/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/5smk763/mbc4.png",MBC 4
https://shls-mbc4-prod-dub.shahid.net/out/v1/c08681f81775496ab4afa2bac7ae7638/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/5smk763/mbc4.png",MBC 4
https://shls-masr-prod-dub.shahid.net/out/v1/c08681f81775496ab4afa2bac7ae7638/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/5smk763/mbc4.png",MBC 4
https://mbc4-prod-dub-enc.edgenextcdn.net/out/v1/c08681f81775496ab4afa2bac7ae7638/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/vzbhKTj/mbc5.png",MBC 5
https://shls-mbc5-prod-dub.shahid.net/out/v1/2720564b6a4641658fdfb6884b160da2/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/2ndSCfQ/mbcdrama0.png",MBC DRAMA
https://mbc1-enc.edgenextcdn.net/out/v1/b0b3a0e6750d4408bb86d703d5feffd1/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/2ndSCfQ/mbcdrama0.png",MBC DRAMA
https://mbcdrama-usa-enc.edgenextcdn.net/out/v1/876f960feec24a8aba9e9d3f9023174b/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/2ndSCfQ/mbcdrama0.png",MBC DRAMA USA
https://mbcdrama-usa-ak.akamaized.net/out/v1/876f960feec24a8aba9e9d3f9023174b/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/2ndSCfQ/mbcdrama0.png",MBC DRAMA MASR
https://shls-live-enc.edgenextcdn.net/out/v1/08eca926a78a41339b8010c882410307/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/xzdqq9y/mbcdrama.png",MBC DRAMA PLUS
https://shls-mbcplusdrama-prod-dub.shahid.net/out/v1/97ca0ce6fc6142f4b14c0a694af59eab/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/xzdqq9y/mbcdrama.png",MBC DRAMA PLUS
https://mbcplusdrama-prod-dub-enc.edgenextcdn.net/out/v1/97ca0ce6fc6142f4b14c0a694af59eab/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/BnhWg65/mbcmasr.png",MBC MASR 1
https://shls-masr-prod-dub.shahid.net/out/v1/d5036cabf11e45bf9d0db410ca135c18/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/BnhWg65/mbcmasr.png",MBC MASR 1
https://mbc1-enc.edgenextcdn.net/out/v1/d5036cabf11e45bf9d0db410ca135c18/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/BnhWg65/mbcmasr.png",MBC MASR 1
https://shls-live-enc.edgenextcdn.net/out/v1/d5036cabf11e45bf9d0db410ca135c18/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/BnhWg65/mbcmasr.png",MBC MASR 1
https://masr-usa-enc.edgenextcdn.net/out/v1/5fcaf05b5cd64b3cb4a969e0470080c8/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/BnhWg65/mbcmasr.png",MBC MASR USA
https://masr-usa-ak.akamaized.net/out/v1/5fcaf05b5cd64b3cb4a969e0470080c8/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/M7B22HL/mbcmasr2.jpg",MBC MASR 2
https://shls-masr2-prod-dub.shahid.net/out/v1/f683685242b549f48ea8a5171e3e993a/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/M7B22HL/mbcmasr2.jpg",MBC MASR 2
https://shls-masr2-ak.akamaized.net/out/v1/f683685242b549f48ea8a5171e3e993a/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/M7B22HL/mbcmasr2.jpg",MBC MASR 2
https://shls-masr2-enc.edgenextcdn.net/out/v1/2720564b6a4641658fdfb6884b160da2/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/rkr6JSX/mbc-iraq.png",MBC IRAQ
https://shd-gcp-live.edgenextcdn.net/live/bitmovin-mbc-iraq/e38c44b1b43474e1c39cb5b90203691e/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/rkr6JSX/mbc-iraq.png",MBC IRAQ
https://shls-iraq-prod-dub.shahid.net/out/v1/c9bf1e87ea66478bb20bc5c93c9d41ea/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/rkr6JSX/mbc-iraq.png",MBC IRAQ
https://iraq-prod-dub-enc.edgenextcdn.net/out/v1/c9bf1e87ea66478bb20bc5c93c9d41ea/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/m5gGgfJ/mbcbollywood.png",MBC BOLLYWOOD
https://shls-mbcbollywood-prod-dub.shahid.net/out/v1/a79c9d7ef2a64a54a64d5c4567b3462a/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/m5gGgfJ/mbcbollywood.png",MBC BOLLYWOOD
https://mbcbollywood-prod-dub-enc.edgenextcdn.net/out/v1/d5bbe570e1514d3d9a142657d33d85e6/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mc475nQ/shadidblck.jpg",MBC AFLAM
https://shls-live-enc.edgenextcdn.net/out/v1/0044dd4b001a466c941ad77b04a574a2/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mc475nQ/shadidblck.jpg",MBC MOVIES
https://shls-live-enc.edgenextcdn.net/out/v1/90143f040feb40589d18c57863d9e829/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mc475nQ/shadidblck.jpg",MBC MOVIES ACTION
https://shls-live-enc.edgenextcdn.net/out/v1/46079e838e65490c8299f902a7731168/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mc475nQ/shadidblck.jpg",MBC MOVIES THRILLER
https://shls-live-enc.edgenextcdn.net/out/v1/f6d718e841f8442f8374de47f18c93a7/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/98TBSSm/mbcfmtv.png",MBC RABEH SAQER
https://shls-live-enc.edgenextcdn.net/out/v1/ea4275b6dc0840c198c17f6dc6f1ec49/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/98TBSSm/mbcfmtv.png",MBC FM LIVE TV
https://mbcfm-riyadh-prod-dub.shahid.net/out/v1/69c8a03f507e422f99cf5c07291c9e3a/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Hy2GLK8/mbcloud.png",MBC LOUD FM TV
https://d2lfa0y84k5bwn.cloudfront.net/out/v1/86dd4506a70c4d7fb35e2ab50296d9a3/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/7W5nWYV/rotanacinema.png",ROTANA CINEMA KSA
https://bcovlive-a.akamaihd.net/9527a892aeaf43019fd9eeb77ad1516e/eu-central-1/6057955906001/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/7W5nWYV/rotanacinema.png",ROTANA CINEMA KSA
https://rotana.hibridcdn.net/rotana/cinema_net-7Y83PP5adWixDF93/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/7W5nWYV/rotanacinema.png" referer="https://rotana.net/",ROTANA CINEMA MASR
https://rotana.hibridcdn.net/rotananet/cinemamasr_net-7Y83PP5adWixDF93/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/7W5nWYV/rotanacinema.png",ROTANA AFLAM PLUS
https://d35j504z0x2vu2.cloudfront.net/v1/master/0bc8e8376bd8417a1b6761138aa41c26c7309312/rotana-aflam-plus/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/N2C6FMyv/Mplus.png",ROTANA M PLUS
https://d35j504z0x2vu2.cloudfront.net/v1/master/0bc8e8376bd8417a1b6761138aa41c26c7309312/m-plus/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/HNm4jw9/rotanaclip.png" referer="https://rotana.net/",ROTANA CLIP
https://rotana.hibridcdn.net/rotananet/clip_net-7Y83PP5adWixDF93/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/6DcdjwT/rotanaclassic.png" referer="https://rotana.net/",ROTANA CLASSIC
https://rotana.hibridcdn.net/rotananet/classical_net-7Y83PP5adWixDF93/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/SwZKHJj/rcomedy.jpg" referer="https://rotana.net/",ROTANA COMEDY
https://rotana.hibridcdn.net/rotananet/comedy_net-7Y83PP5adWixDF93/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/5sJ9vSJ/rotanakhalijia.png",ROTANA KHALIJA
https://edge66.magictvbox.com/liveApple/rotana_khalijiah/tracks-v1a1/mono.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/5sJ9vSJ/rotanakhalijia.png",ROTANA KHALIJA
https://rotana.hibridcdn.net/rotana/khaleejiya_net-7Y83PP5adWixDF93/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/207NnrF1/pncdr.png",ROTANA PNC DRAMA
https://d35j504z0x2vu2.cloudfront.net/v1/master/0bc8e8376bd8417a1b6761138aa41c26c7309312/pnc-drama/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/207NnrF1/pncdr.png" referer="https://rotana.net/",ROTANA DRAMA
https://rotana.hibridcdn.net/rotananet/drama_net-7Y83PP5adWixDF93/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/84HtHzK/Roya-TV.png",ROYA TV
https://royatv-live.daioncdn.net/royatv/royatv.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/84HtHzK/Roya-TV.png",ROYA MUSIC
https://playlist.fasttvcdn.com/pl/toa2uuhhygheuly7xtuqrg/roya-music/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/84HtHzK/Roya-TV.png",ROYA KITCHEN
https://playlist.fasttvcdn.com/pl/toa2uuhhygheuly7xtuqrg/roya-kitchen/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/84HtHzK/Roya-TV.png",ROYA COMEDY
https://playlist.fasttvcdn.com/pl/toa2uuhhygheuly7xtuqrg/roya-comedy/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/84HtHzK/Roya-TV.png",ROYA PALESTINE
https://playlist.fasttvcdn.com/pl/toa2uuhhygheuly7xtuqrg/roya-palestine/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/84HtHzK/Roya-TV.png",ROYA KIDS
https://playlist.fasttvcdn.com/pl/ptllxjd03j6g9oxxjdfapg/roya-kids/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/84HtHzK/Roya-TV.png",ROYA KIDS ORIGINALS
https://playlist.fasttvcdn.com/pl/ptllxjd03j6g9oxxjdfapg/roya-kids-originals/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/84HtHzK/Roya-TV.png",ROYA KIDS SONGS
https://playlist.fasttvcdn.com/pl/ptllxjd03j6g9oxxjdfapg/roya-kids-songs/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/84HtHzK/Roya-TV.png",ROYA KIDS STORIES
https://playlist.fasttvcdn.com/pl/ptllxjd03j6g9oxxjdfapg/roya-kids-stories/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/84HtHzK/Roya-TV.png",ROYA DRAMA
https://playlist.fasttvcdn.com/pl/a2le4pbpa6rpzv147haf4w/drama/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/84HtHzK/Roya-TV.png",ROYA SPORTS
https://playlist.fasttvcdn.com/pl/a2le4pbpa6rpzv147haf4w/youth-jordan/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/84HtHzK/Roya-TV.png",ROYA WORLD
https://playlist.fasttvcdn.com/pl/toa2uuhhygheuly7xtuqrg/around-the-world/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/84HtHzK/Roya-TV.png",ROYA ADVENTURES
https://playlist.fasttvcdn.com/pl/toa2uuhhygheuly7xtuqrg/roya-adventures/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/84HtHzK/Roya-TV.png",ROYA MARAYA
https://playlist.fasttvcdn.com/pl/toa2uuhhygheuly7xtuqrg/maraya/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/84HtHzK/Roya-TV.png",ROYA CARAVAN
https://playlist.fasttvcdn.com/pl/toa2uuhhygheuly7xtuqrg/caravan/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/84HtHzK/Roya-TV.png",ROYA IMAM
https://playlist.fasttvcdn.com/pl/toa2uuhhygheuly7xtuqrg/adel-imam-movies/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/84HtHzK/Roya-TV.png",ROYA PRODUCTION
https://playlist.fasttvcdn.com/pl/toa2uuhhygheuly7xtuqrg/roya-production/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/84HtHzK/Roya-TV.png",ROYA AL HAYBA
https://playlist.fasttvcdn.com/pl/toa2uuhhygheuly7xtuqrg/alhayba/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/84HtHzK/Roya-TV.png",ROYA ACTION
https://playlist.fasttvcdn.com/pl/toa2uuhhygheuly7xtuqrg/action/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/84HtHzK/Roya-TV.png",ROYA AH SHAMYEH
https://playlist.fasttvcdn.com/pl/toa2uuhhygheuly7xtuqrg/by2ah-shamyeh/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/84HtHzK/Roya-TV.png",ROYA AL QUEBBEH
https://playlist.fasttvcdn.com/pl/toa2uuhhygheuly7xtuqrg/haret-alqubbeh/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/84HtHzK/Roya-TV.png",ROYA NADINENJAIM
https://playlist.fasttvcdn.com/pl/toa2uuhhygheuly7xtuqrg/nadinenjaim/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/84HtHzK/Roya-TV.png",ROYA AYMAN ZAYDAN
https://playlist.fasttvcdn.com/pl/toa2uuhhygheuly7xtuqrg/ayman-zaydan/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/84HtHzK/Roya-TV.png",ROYA AL ZAEEM
https://playlist.fasttvcdn.com/pl/toa2uuhhygheuly7xtuqrg/alzaeem/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/84HtHzK/Roya-TV.png",ROYA HAKI MONAWWA
https://playlist.fasttvcdn.com/pl/toa2uuhhygheuly7xtuqrg/haki-monawwa/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/84HtHzK/Roya-TV.png",ROYA ANA BAHKILAK
https://playlist.fasttvcdn.com/pl/toa2uuhhygheuly7xtuqrg/ana-bahkilak-elgessa/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/84HtHzK/Roya-TV.png",ROYA MASRAHYYAT
https://playlist.fasttvcdn.com/pl/toa2uuhhygheuly7xtuqrg/masrahyyat/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/84HtHzK/Roya-TV.png",ROYA DOCU
https://playlist.fasttvcdn.com/pl/toa2uuhhygheuly7xtuqrg/documentaries/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/84HtHzK/Roya-TV.png",ROYA MOJTAMAII
https://playlist.fasttvcdn.com/pl/toa2uuhhygheuly7xtuqrg/mojtamaii/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/84HtHzK/Roya-TV.png",ROYA NEWS
https://royatv-live.daioncdn.net/royatv/royatv.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/84HtHzK/Roya-TV.png",ROYA NEWS
https://raw.githubusercontent.com/MassinDV/Youtube-arabic-channels/main/live/ch39.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/84HtHzK/Roya-TV.png",ROYA TV (backup)
https://roya.daioncdn.net/royatv/royatv.m3u8?app=8c1e143a-39cf-40b4-acb2-e78faa1f322d
#EXTINF:-1 tvg-logo="https://i.ibb.co/84HtHzK/Roya-TV.png",ROYA TV (backup)
https://roya-live.ercdn.net/roya/roya.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/84HtHzK/Roya-TV.png",ROYA TV (backup)
https://weyyak-live.akamaized.net/weyyak_roya/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/5RGbN6g/Zee-Afam.png",ZEE AFLAM
https://weyyak-live.akamaized.net/weyyak_zee_aflam/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/c1zsKkv/Zee-Alwan.png",ZEE ALWAN
https://weyyak-live.akamaized.net/weyyak_zee_alwan/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/3WCfsRq/weyk.png",WEYYAK DRAMA
https://weyyak-live.akamaized.net/weyyak_drama/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/3WCfsRq/weyk.png",WEYYAK MIX
https://weyyak-live.akamaized.net/weyyak_mix/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/3WCfsRq/weyk.png",WEYYAK ACTION
https://weyyak-live.akamaized.net/weyyak_action/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/3WCfsRq/weyk.png",WEYYAK NAWAEM
https://weyyak-live.akamaized.net/weyyak_nawaem/index.m3u8
#EXTINF:-1 group-title="20. |AR|🇸🇦 THEMATICS-2 عربي",--- |⬇DOWN/OFFLINES⬇| ---
http://blank
#EXTINF:-1 tvg-logo="https://i.ibb.co/dQV1zQG/cbclive.jpg",CBC LIVE
https://new.cache-stream.workers.dev/stream/UCUHq39HXLyAjjMPIjsNRLpw/live.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/0jpsxm7/cbcsofra.png",CBC SOFRA
https://new.cache-stream.workers.dev/stream/UC--UtxrU7FWNCp0l7AG9EIw/live.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/HKtfJmp/cbcextranews.jpg",CBC NEWS
https://new.cache-stream.workers.dev/stream/UC65F33K2cXk9hGDbOQYhTOw/live.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/7W5nWYV/rotanacinema.png",ROTANA CINEMA MASR
https://shls-masr2-ak.akamaized.net/out/v1/c39c0ecbcbdb46e890e91106776397a8/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/7W5nWYV/rotanacinema.png",ROTANA CINEMA MASR
https://shls-rotanacinema-egy-prod-dub.shahid.net/out/v1/c39c0ecbcbdb46e890e91106776397a8/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/7W5nWYV/rotanacinema.png",ROTANA CINEMA KSA
https://shls-rotanacinema-ksa-prod-dub.shahid.net/out/v1/6cee1c57ea7841e697eb15cefc98e0a6/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/RC0XZrb/rotanaplus.png",ROTANA PLUS
https://shls-rotanaplus-prod-dub.shahid.net/out/v1/1fc6103458be480b96e6a574b00fe1c0/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/RC0XZrb/rotanaplus.png",ROTANA PLUS
https://rotanaplus-prod-dub-ak.akamaized.net/out/v1/1fc6103458be480b96e6a574b00fe1c0/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/PN8G6F8/rotanakids.png",ROTANA KIDS
https://shls-masr2-ak.akamaized.net/out/v1/df6e0eb3cdc4410b98209aafc8677cef/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/PN8G6F8/rotanakids.png",ROTANA KIDS
https://shls-rotanakids-prod-dub.shahid.net/out/v1/df6e0eb3cdc4410b98209aafc8677cef/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/5sJ9vSJ/rotanakhalijia.png",ROTANA KHALIJA
https://shls-masr2-ak.akamaized.net/out/v1/a639fd49db684f1b8c063d398101a888/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/5sJ9vSJ/rotanakhalijia.png",ROTANA KHALIJA
https://shls-rotanakhalijia-prod-dub.shahid.net/out/v1/a639fd49db684f1b8c063d398101a888/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Tw3gRvT/rotanadrama.png",ROTANA DRAMA
https://shls-rotanadrama-prod-dub.shahid.net/out/v1/20c617b40dc743589ecc9d08d9d3345d/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/YL1wKY8/Duhkwabas.png",ROTANA DUHK WABASS
https://daiconnect.com/live/hls/rotana/dwbass/.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/YL1wKY8/Duhkwabas.png",ROTANA DUHK WABASS
https://daiconnect.com/live/hls/rotana/dwbass/2863b804cde7974b846f64583832be11/.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/JqnC8VY/shahid.png",SHAHID AL ZAEEM
https://cdxaws-ak.akamaized.net/v1/channel/AlZaeem--/index_hls.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/JqnC8VY/shahid.png",SHAHID AL MASRAH
https://cdxaws-ak.akamaized.net/v1/channel/Al_Masrah/index_hls.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/JqnC8VY/shahid.png",SHAHID AL USTURA
https://cdxaws-ak.akamaized.net/v1/channel/Al_Ostoura_/index_hls.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/JqnC8VY/shahid.png",SHAHID COMEDY
https://cdxaws-ak.akamaized.net/v1/channel/Comedy---/index_hls.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/JqnC8VY/shahid.png",SHAHID 1
https://cdxaws-ak.akamaized.net/v1/channel/Shahid_Al_Oula__/index_hls.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/JqnC8VY/shahid.png",SHAHID SHAM
https://cdxaws-ak.akamaized.net/v1/channel/Al_Sham--/index_hls.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/JqnC8VY/shahid.png",SHAHID MAQALEB
https://cdxaws-ak.akamaized.net/v1/channel/Maqaleb--/index_hls.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/JqnC8VY/shahid.png",SHAHID AL ZARAQ
https://cdxaws-ak.akamaized.net/v1/channel/Ma_Al_Zaraq/index_hls.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/N19JFwZ/mbc.png",MBC 1 [offlink]
https://shls-mbcdramaksa-ak.akamaized.net/out/v1/84ab37e99d6e4b16b33c6600f94f6ccb/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/BnhWg65/mbcmasr.png",MBC MASR 1 [offlink]
https://shls-masr-prod-dub.shahid.net/out/v1/b7093401da27496797a8949de23f4578/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/BnhWg65/mbcmasr.png",MBC MASR 1 [offlink]
https://shls-masr-ak.akamaized.net/out/v1/b7093401da27496797a8949de23f4578/index.m3u8


#EXTINF:-1 tvg-logo="https://i.ibb.co/xGG27kS/raiit.png" group-title="21. |IT|🇮🇹 ITALIA - LOCALE",RAI NEWS 24
https://rainews2-live.akamaized.net/hls/live/598327/rainews2/rainews2/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/xGG27kS/raiit.png",RAI NEWS 24
https://8e7439fdb1694c8da3a0fd63e4dda518.msvdn.net/rainews1/hls/playlist_mo.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/xGG27kS/raiit.png",RAI 3
https://wzstreaming.rai.it/TVlive/smil:liveStream.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.imgur.com/oAiSU8O.png",CLASS CNBC
https://859c1818ed614cc5b0047439470927b0.msvdn.net/live/S57048752/8raQqCXozN1H/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.imgur.com/02vCECa.png",LA C NEWS 24
https://f5842579ff984c1c98d63b8d789673eb.msvdn.net/live/S27391994/HVvPMzy/playlist.m3u8
#EXTINF:-1 tvg-logo="http://odmsto.com/uploads/tv_image/sm/teleticino.png",TELETICINO
https://vstream-cdn.ch/hls/teleticino_720p/index.m3u8
#EXTINF:-1 tvg-logo="https://i.imgur.com/F90mpSa.png",LA 7
https://d3749synfikwkv.cloudfront.net/v1/master/3722c60a815c199d9c0ef36c5b73da68a62b09d1/cc-74ylxpgd78bpb/Live.m3u8
#EXTINF:-1 tvg-logo="https://i.imgur.com/ISbxfY0.png",ITALIA 2 TV
https://59d7d6f47d7fc.streamlock.net/italia2/italia2/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.imgur.com/lXGWoV9.png",RETE TV
https://57068da1deb21.streamlock.net/retetvitalia/retetvitalia/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.imgur.com/EsZn2cj.png",RETE 55
https://live1.giocabet.tv/stream/6/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/KmY1chC/Canale-7.png",CANALE 7
http://wms.shared.streamshow.it/canale7/canale7/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/JCzkhFF/cafe24.png",CAFE TV 24
https://srvx1.selftv.video/cafe/live/playlist.m3u8
#EXTINF:-1 tvg-name="Canale 10" tvg-logo="https://i.imgur.com/KuQcjYV.png",CANALE 10
https://nrvideo1.newradio.it:1936/desxcerbht/desxcerbht/playlist.m3u8
#EXTINF:-1 tvg-name="Euro Tv" tvg-logo="https://i.imgur.com/HCl5Zbu.png",EURO TV
https://5f22d76e220e1.streamlock.net/eurotv/eurotv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.imgur.com/3NiLKvj.png",RADIO 105 TV
https://live02-seg.msr.cdn.mediaset.net/live/ch-ec/ec-clr.isml/index.m3u8
#EXTINF:-1 tvg-logo="https://i.imgur.com/rlaKH6k.png",DEEJAY TV
https://4c4b867c89244861ac216426883d1ad0.msvdn.net/live/S85984808/sMO0tz9Sr2Rk/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.imgur.com/4VCEJuJ.png",RADIO ITALIA TV
https://radioitaliatv.akamaized.net/hls/live/2093117/RadioitaliaTV/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/vj6rjWs/radioitrrend.png",RADIO ITALIA TREND
https://radioitalia-samsungitaly.amagi.tv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.imgur.com/UTStxDW.png",RADIO KISS KISS TV
https://kk.fluid.stream/KKMulti/smil:KissKissTV.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.imgur.com/mWeEa9T.png",R101 TV
https://live02-seg.msr.cdn.mediaset.net/live/ch-er/er-clr.isml/index.m3u8
#EXTINF:-1 tvg-logo="https://i.imgur.com/KdissvS.png",RTL 102.5
https://dd782ed59e2a4e86aabf6fc508674b59.msvdn.net/live/S97044836/tbbP8T1ZRPBL/playlist_video.m3u8
#EXTINF:-1 tvg-logo="https://i.imgur.com/zDByOwo.png",SUPER!
https://vimnitaly.akamaized.net/hls/live/2094034/super/master.m3u8
#EXTINF:-1 tvg-logo="https://i.imgur.com/KCBurST.png",EXTRA TV
https://rst2.saiuzwebnetwork.it:8081/extratvlive/index.m3u8
#EXTINF:-1 tvg-logo="https://www.tvdream.net/img/sportitalia.png",SPORT ITALIA
https://di-kzbhv8pw.vo.lswcdn.net/sportitalia/sihd/playlist.m3u8
#EXTINF:-1 tvg-logo="http://odmsto.com/uploads/tv_image/sm/sportitalia-24-live.jpg",SPORT ITALIA LIVE
https://di-kzbhv8pw.vo.lswcdn.net/sportitalia/smil:silive24.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="http://odmsto.com/uploads/tv_image/sm/rtv-smarino-sport.png",RTV S.MARINO
https://d2hrvno5bw6tg2.cloudfront.net/smrtv-ch02/_definst_/smil:ch-02.smil/chunklist_b1692000_slita.m3u8
#EXTINF:-1 tvg-logo="https://www.tvdream.net/img/go-tv.png",GO-TV
https://6zklxkbbdw9b-hls-live.mariatvcdn.it/msmotor/2f759512164fc6fe4acbed6a5648993a.sdp/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.imgur.com/GzsPlbX.png",SUPER TENNIS
https://live-embed.supertennix.hiway.media/restreamer/supertennix_client/gpu-a-c0-16/restreamer/rtmp/hls/h24_supertennix/manifest.m3u8
#EXTINF:-1 tvg-logo="https://i.imgur.com/3TMMXmS.png",RADIO MONTECARLO TV
https://live02-seg.msr.cdn.mediaset.net/live/ch-bb/bb-clr.isml/index.m3u8
#EXTINF:-1 tvg-logo="https://i.imgur.com/7Im3HI1.png",VIRGIN RADIO TV
https://live02-seg.msr.cdn.mediaset.net/live/ch-ew/ew-clr.isml/index.m3u8
#EXTINF:-1 tvg-logo="https://i.imgur.com/S2sCFQi.png",ALTO ADIGE TV
https://5f204aff97bee.streamlock.net/AltoAdigeTV/livestream/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.imgur.com/NfvHIAw.png",ANRENNA 2 BERGAMO
https://58f12ffd2447a.streamlock.net/Antenna2/livestream/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.imgur.com/NiVHLwp.png",ANTENNA 3 VENETO
https://59d7d6f47d7fc.streamlock.net/antennatreveneto/antennatreveneto.stream/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.imgur.com/b8y6ImZ.png",ANTENNA SUD
https://live.antennasudwebtv.it:9443/hls/vod.m3u8
#EXTINF:-1 tvg-logo="https://i.imgur.com/6tBv8VD.png",ANTENNA SUD EXTRA
https://live.antennasudwebtv.it:9443/hls/vod92.m3u8
#EXTINF:-1 tvg-logo="https://i.imgur.com/v8PlAJO.png",ARISTANIS TV
https://video2.azotosolutions.com:1936/supertvoristano/supertvoristano/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.imgur.com/DP5y0Er.png",ARTE NETWORK
https://tsw.streamingwebtv24.it:1936/artenetwork/artenetwork/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.imgur.com/BoLZ5wG.png",AURORA ARTE
https://59d7d6f47d7fc.streamlock.net/auroraarte/auroraarte/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.imgur.com/mSWw8uW.png",AZZURRA TV
https://59d7d6f47d7fc.streamlock.net/azzurratv/azzurratv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/VxLFYSj/euronews.png",EURONEWS IT
https://euronews-live-ita-it.fast.rakuten.tv/v1/master/0547f18649bd788bec7b67b746e47670f558b6b2/production-LiveChannel-6570/bitok/e/25674/euronews-it.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/VxLFYSj/euronews.png",EURONEWS IT
https://jmp2.uk/sam-IT2600009QD.m3u8


#EXTINF:-1 tvg-logo="https://i.ibb.co/h8h2d5Q/tag24.png" group-title="22. |DE|🇩🇪 DEUTSCHLAND - LOKALE",TAGESSCHAU 24
https://tagesschau.akamaized.net/hls/live/2020115/tagesschau/tagesschau_1/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/GcZR4DM/daserste.png",DAS ERSTE INTL
https://derste247liveint.akamaized.net/hls/live/662735/daserste_int/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/GcZR4DM/daserste.png",DAS ERSTE INTL
https://daserste-live.ard-mcdn.de/daserste/live/hls/int/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/GcZR4DM/daserste.png",DAS ERSTE INTL
https://mcdn.daserste.de/daserste/int/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/GcZR4DM/daserste.png",DAS ERSTE DE
https://mcdn.daserste.de/daserste/de/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/GcZR4DM/daserste.png",DAS ERSTE DE
https://daserste-live.ard-mcdn.de/daserste/live/hls/de/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/GcZR4DM/daserste.png",DAS ERSTE DE
http://daserstedash.akamaized.net/dash/live/2103597/daserste/dvbt2/manifest.mpd
#EXTINF:-1 tvg-logo="https://i.ibb.co/Msmh0pG/rtlde.png",RTL DE
https://ma.anixa.tv/clips/stream/rtl/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/cc4J7ZB/Alphaard.png",ALPHA ARD
https://mcdn.br.de/br/fs/ard_alpha/hls/de/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/jkNhhLn/brfde.png",BR DE
https://mcdn.br.de/br/fs/bfs_nord/hls/de/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/JnYMnfw/hrde.png",HR DE
https://hrhls.akamaized.net/hls/live/2024525/hrhls/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/5sJk5v2/srde.png",SR DE
https://srfs.akamaized.net/hls/live/689649/srfsgeo/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/4j4PnNL/wdr.png",WDR DE
https://mcdn.wdr.de/wdr/wdrfs/de/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/BPpZPBn/arte.png",ARTE DE
https://artesimulcast.akamaized.net/hls/live/2030993/artelive_de/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/VxLFYSj/euronews.png",EURONEWS DE
https://euronews-live-deu-de.fast.rakuten.tv/v1/master/0547f18649bd788bec7b67b746e47670f558b6b2/production-LiveChannel-6567/bitok/e/26033/euronews-de.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/VxLFYSj/euronews.png",EURONEWS DE
https://jmp2.uk/sam-DE2600003TR.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/D7w9h7Q/rt.png",RT DEUTSCH [censure-blocked]
https://rt-ger.rttv.com/live/rtdeutsch/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/D7w9h7Q/rt.png",RT DEUTSCH [censure-blocked]
https://rt-ger.rttv.com/dvr/rtdeutsch/playlist.m3u8


#EXTINF:-1 group-title="23. |EU|🇪🇺 EUROPEAN COCKTAILTOUR🍸",--- |LU:🇱🇺 LUXEMBOURG| ---
http://blank
#EXTINF:-1 tvg-logo="https://i.ibb.co/VprDD5J/rtllux.png",RTL LUX
https://live-edge.rtl.lu/channel1/smil:channel1/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/VprDD5J/rtllux.png",RTL LUX 2
https://stream.rtl.lu/data/live/tele/channel2/playlist.m3u8
#EXTINF:-1 group-title="23. |EU|🇪🇺 EUROPEAN COCKTAILTOUR🍸",--- |DK:🇩🇰 DENMARK| ---
http://blank
#EXTINF:-1 tvg-logo="https://i.ibb.co/6Rdh3h1Q/drtva.png",DR TVA
https://drlivedrtvahls.akamaized.net/hls/live/2113613/drlivedrtva/master.m3u8
#EXTINF:-1 group-title="23. |EU|🇪🇺 EUROPEAN COCKTAILTOUR🍸",--- |FI:🇫🇮 FINLAND| ---
http://blank
#EXTINF:-1 tvg-logo="https://i.ibb.co/r29pMj4B/Ylew.png",YLE TV WORLD
https://yletvworld.akamaized.net/hls/live/622540/yletv1w/index.m3u8
#EXTINF:-1 group-title="23. |EU|🇪🇺 EUROPEAN COCKTAILTOUR🍸",--- |PL:🇵🇱 POLONIA| ---
http://blank
#EXTINF:-1 tvg-logo="https://i.ibb.co/yhjqqNQ/tvppol.png",TVP POLONIA
http://rr3.tvdosug.net/~109e1a3c05fcad5b22d13b9453dc0db5122/10094/hls/pl.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/yhjqqNQ/tvppol.png",TVP POLONIA
https://raw.githubusercontent.com/ipstreet312/freeiptv/refs/heads/master/ressources/wld/tvpol.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/pxSC2HJ/tvpinfo.png",TVP INFO
https://raw.githubusercontent.com/ipstreet312/freeiptv/refs/heads/master/ressources/wld/tvpin.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/kx2RQ5V/polsatnews1.png",POLSAT NEWS
http://cdn-s-lb2.pluscdn.pl/lv/1517830/349/hls/f03a76f3/masterlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/VxLFYSj/euronews.png",EURONEWS PL
https://euronews-live-pol-pl.fast.rakuten.tv/v1/master/0547f18649bd788bec7b67b746e47670f558b6b2/production-LiveChannel-6769/bitok/e/26235/euronews-pl.m3u8
#EXTINF:-1 group-title="23. |EU|🇪🇺 EUROPEAN COCKTAILTOUR🍸",--- |RO:🇷🇴 ROMANIA| ---
http://blank
#EXTINF:-1 tvg-logo="https://i.ibb.co/w46x9LM/tvri.png",TVR INT
https://tvr-tvri.cdn.zitec.com/live/tvri/main.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/9GHhm6L/ant1ro.png",ANTENA 1 RO
https://live1ag.antenaplay.ro/live_a1ro/live_a1ro.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/FJbq1ML/a3ro.jpg",ANTENA 3 VOX
https://live3vox.antenaplay.ro/a3free/a3free.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/8Mngyds/kd1ro.png",KANAL D RO
https://stream1.kanald.ro/iphone/knd-live.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/gMNsZPf/kd2ro.png",KANAL D2 RO
https://stream2.kanald.ro/iphone/knd-live.m3u8
#EXTINF:-1 group-title="23. |EU|🇪🇺 EUROPEAN COCKTAILTOUR🍸",--- |MD:🇲🇩 MOLDOVA| ---
http://blank
#EXTINF:-1 tvg-logo="https://i.ibb.co/KjgkLjq/md1.png",MOLDOVA 1
https://v0.trm.md/static/streaming-playlists/hls/9b79338b-1870-4cd7-91d4-0f6ce5cac7ca/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Wz954nZ/md2.png",MOLDOVA 2
https://v.trm.md/static/streaming-playlists/hls/937e4e0e-7174-4fb2-a299-480e68b49ecb/master.m3u8


#EXTINF:-1 group-title="24. |HR-BA-RS++|🇭🇷🇧🇦🇷🇸 BALKANIC",--- |HR:🇭🇷 CROATIA| ---
http://blank
#EXTINF:-1 tvg-logo="https://i.ibb.co/nnkDGpc/hrthr.png",HRT 1
https://webtvstream.bhtelecom.ba/hrt1.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/nnkDGpc/hrthr.png",HRT 2
https://webtvstream.bhtelecom.ba/hrt2.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/nnkDGpc/hrthr.png",HRT 3
https://webtvstream.bhtelecom.ba/hrt3.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/zNxvwRc/rtlhr.png",RTL HR
https://d1cs5tlhj75jxe.cloudfront.net/rtl/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/NgPZkKhJ/cmctv.png",CMC TV
https://stream.cmctv.hr:49998/cmc/live.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/nM7rVmT4/jadran.png",TV JADRAN
https://tvjadran.stream.agatin.hr:3412/live/tvjadranlive.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/pBZ486WC/n1bal.png",N1 HRV
https://best-str.umn.cdn.united.cloud/stream?stream=sp1400&sp=n1info&channel=n1hrv&u=n1info&p=n1Sh4redSecre7iNf0&player=m3u8
#EXTINF:-1 group-title="24. |HR-BA-RS++|🇭🇷🇧🇦🇷🇸 BALKANIC",--- |BA:🇧🇦 BOSNIA| ---
http://blank
#EXTINF:-1 tvg-logo="https://i.ibb.co/HLzRKs7k/bhrt.png",BH RT
https://webtvstream.bhtelecom.ba/hls13/bhrtportal.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/YFPPw1Wf/tvmba.png",TELEVIZIJA M
https://live.tv-m.net/hls/stream.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/4nyQwgwX/Aljbalk.png",AL JAZEERA BALKANS
https://live-hls-web-ajb.getaj.net/AJB/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/pBZ486WC/n1bal.png",N1 BOS
https://best-str.umn.cdn.united.cloud/stream?stream=sp1400&sp=n1info&channel=n1bos&u=n1info&p=n1Sh4redSecre7iNf0&player=m3u8
#EXTINF:-1 group-title="24. |HR-BA-RS++|🇭🇷🇧🇦🇷🇸 BALKANIC",--- |RS:🇷🇸 SERBIA| ---
http://blank
#EXTINF:-1 tvg-logo="https://i.ibb.co/xHMT7Jz/rtsrs.png",RTS 1
https://webtvstream.bhtelecom.ba/rts1.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/xHMT7Jz/rtsrs.png",RTS 2
https://webtvstream.bhtelecom.ba/rts2.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/xHMT7Jz/rtsrs.png",RTS SVET
https://webtvstream.bhtelecom.ba/rts_svet.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/ZJB71LL/pinktvrs.png",PINK TV
https://edge8.pink.rs/pinktv/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/ZJB71LL/pinktvrs.png",PINK RED
https://edge8.pink.rs/redtv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/TBZ2pnKW/bntv.png",BN TV
https://rtvbn.tv:8080/live/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Wvttv9WX/Tvas.png",TV AS
https://srv1.adriatelekom.com/TVAS/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/0y3F6QYq/Piknl.png",PI KANAL
https://stream.pikanal.rs/pikanal/pgm.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/pBZ486WC/n1bal.png",N1 SRB
https://best-str.umn.cdn.united.cloud/stream?stream=sp1400&sp=n1info&channel=n1srp&u=n1info&p=n1Sh4redSecre7iNf0&player=m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/VxLFYSj/euronews.png",EURONEWS SRB
https://d1ei8ofhgfmkac.cloudfront.net/app-19518-1306/ngrp:QoZfNjsg_all/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/F4FwJnNY/moba.png",MOBA
https://muzzik-live.morescreens.com/mts-2/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/gMLsMZ9P/popstar.png",POP STAR
https://muzzik-live.morescreens.com/mts-3/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/kVXqj9fQ/Jeka.png",JEKA
https://muzzik-live.morescreens.com/mts-4/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/W4zhWby6/Zztv.png",ZZ TV
https://muzzik-live.morescreens.com/mts-a4/playlist.m3u8
#EXTINF:-1 group-title="24. |HR-BA-RS++|🇭🇷🇧🇦🇷🇸 BALKANIC",--- |ME:🇲🇪 MONTENEGRO| ---
http://blank
#EXTINF:-1 tvg-logo="https://i.ibb.co/5x1cbJqN/rtcg.png",TVCG 1
http://cdn3.bcdn.rs:1935/cg1/smil:cg1.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/5x1cbJqN/rtcg.png",TVCG 2
http://cdn3.bcdn.rs:1935/cg2/smil:cg2.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/5x1cbJqN/rtcg.png",TVCG 3
https://parlament.rtcg.me:1936/pr/smil:parlament.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/5x1cbJqN/rtcg.png",TVCG MNE
http://cdn3.bcdn.rs:1935/cgsat/smil:cgsat.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/5x1cbJqN/rtcg.png",TVCG MNE
http://rtcg2.videostreaming.rs:1935/rtcg/rtcg.2.stream/playlist.m3u8
#EXTINF:-1 group-title="24. |HR-BA-RS++|🇭🇷🇧🇦🇷🇸 BALKANIC",--- |AL:🇦🇱 ALBANIA| ---
http://blank
#EXTINF:-1 tvg-logo="https://i.ibb.co/rf1Vmfs5/Nwsalb.png",NEWS 24 ALB
https://tv.balkanweb.com/news24/livestream/playlist.m3u8


#EXTINF:-1 tvg-logo="https://i.ibb.co/RN3dJQ7/geoflag.png" group-title="25. |GE-AM-AZ|🇬🇪🇦🇲🇦🇿 CAUCASIAN",GPB 1TV პირველი არხი
https://tv.cdn.xsg.ge/gpb-1tv/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/RN3dJQ7/geoflag.png",GPB 2TV
https://tv.cdn.xsg.ge/gpb-2tv/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/RN3dJQ7/geoflag.png",IMEDI
https://tv.cdn.xsg.ge/imedihd/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/RN3dJQ7/geoflag.png",RUSTAVI 2
https://dvrfl05.tulix.tv/gin-rustavi2/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/RN3dJQ7/geoflag.png",PALITRA
https://livestream.palitra.ge/hls/palitratv/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/RN3dJQ7/geoflag.png",FORMULA
https://tv.cdn.xsg.ge/c4635/TVFormula/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/RN3dJQ7/geoflag.png",ADJARA
https://dvrfl05.tulix.tv/gin-adjara/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/RN3dJQ7/geoflag.png",MTAVARI ARKHI
https://bozztv.com/36bay2/mtavariarxi/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/RN3dJQ7/geoflag.png",GDS TV
http://31.146.5.178:8087/play/a00a/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tmkv6RC/armflag.png",H1 ARM Հանրային հեռուստաը
https://amtv.tulixcdn.com/amtv2/am2abr/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tmkv6RC/armflag.png",H1 NEWS
https://amtv.tulixcdn.com/amtv3/am3abr/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tmkv6RC/armflag.png",H1 NEWS
https://amtvusdvr.tulix.tv/am3abr/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tmkv6RC/armflag.png",SONG ARM
https://songtv.hls.iptvdc.com/web-armenia/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tmkv6RC/armflag.png",FRESH ARM
https://freshtv-live.ru/FreshTV/index.m3u8?token=livestream
#EXTINF:-1 tvg-logo="https://i.ibb.co/tmkv6RC/armflag.png",USA ARMENIA
https://usarmenia-tv.icdndhcp.com/hls/master-iUSATVLIVENET.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tmkv6RC/armflag.png",KINOMAN ARM
http://stream02.vnet.am/Kinoman/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tmkv6RC/armflag.png",ARTN SHANT
https://streamer1.connectto.com/ARTN_mobile/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/VC7Q18V/azflag.png",AZ TV Azərbaycan Televiziyası
http://str.yodacdn.net/aztv/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/VC7Q18V/azflag.png",AZ TV
https://hw2.jemtv.com/app/aztv1/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/VC7Q18V/azflag.png",AZ STAR
http://live.azstartv.com/azstar/smil:azstar.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/VC7Q18V/azflag.png",AZ STAR
https://live.livestreamtv.ca/azstar/amlst:azstar/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/VC7Q18V/azflag.png",ATV AZ
https://stream.atv.az/WebRTCAppEE/streams/780339739845112514894920_adaptive.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/VC7Q18V/azflag.png",ICT TV
https://raw.githubusercontent.com/UzunMuhalefet/streams/main/myvideo-az/ictimai-tv.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/VC7Q18V/azflag.png",ARB
https://raw.githubusercontent.com/UzunMuhalefet/streams/main/myvideo-az/arb.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/VC7Q18V/azflag.png",AZAD
https://raw.githubusercontent.com/UzunMuhalefet/streams/main/myvideo-az/atv-azad.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/VC7Q18V/azflag.png",CBC
https://stream.cbctv.az:5443/LiveApp/streams/cbctv.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/VC7Q18V/azflag.png",BAKU TV
https://rtmp.baku.tv/streams/bakutv.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/VC7Q18V/azflag.png",MEDENİYYET
http://str.yodacdn.net/medeniyyet/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/VC7Q18V/azflag.png",SPACE TV
https://raw.githubusercontent.com/UzunMuhalefet/streams/main/myvideo-az/space-tv.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/VC7Q18V/azflag.png",TMB AZ
http://str.yodacdn.net/tmb_az_app/index.m3u8?token=tmb_app_token_13579
#EXTINF:-1 tvg-logo="https://i.ibb.co/VC7Q18V/azflag.png",XEZER TV
http://stream.tvcdn.net/azerbaycan/xezer-tv.m3u8


#EXTINF:-1 tvg-logo="https://i.ibb.co/tMV7LBL/irib1.png" group-title="26. |IR|🇮🇷 IRAN",IRIB 1
https://s1.ettehadlive.com/live/39/chunklist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/6ndKkPM/irib2.png",IRIB 2
https://s1.ettehadlive.com/live/40/chunklist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/4YQsfv9/irib3.png",IRIB 3
https://s1.ettehadlive.com/live/114/chunklist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/D5S2Q2z/irib4.png",IRIB 4
https://s1.ettehadlive.com/live/41/chunklist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tMV7LBL/irib1.png",IRIB 1
https://ncdn.telewebion.com/tv1/live/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/6ndKkPM/irib2.png",IRIB 2
https://ncdn.telewebion.com/tv2/live/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/4YQsfv9/irib3.png",IRIB 3
https://ncdn.telewebion.com/tv3/live/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/D5S2Q2z/irib4.png",IRIB 4
https://ncdn.telewebion.com/tv4/live/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Kzb8VkY/irib5.png",IRIB 5 TEHRAN
https://ncdn.telewebion.com/tehran/live/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/GMLStpQ/amoozesh.png",IRIB AMOOZESH
https://ncdn.telewebion.com/amouzesh/live/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/1LmYfnH/mostanad.png",IRIB MOSTANAD
https://ncdn.telewebion.com/mostanad/live/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/wsVP42F/namayesh.png",IRIB NAMAYESH
https://ncdn.telewebion.com/namayesh/live/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/pwxkFvX/nassim.jpg",IRIB NASIM
https://ncdn.telewebion.com/nasim/live/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/RgQXYbM/pooya.png",IRIB POOYA
https://ncdn.telewebion.com/pooya/live/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/wJHhH03/salamat.png",IRIB SALAMAT
https://ncdn.telewebion.com/salamat/live/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/PYMzQFX/tamasha.png",IRIB TAMASHA
https://ncdn.telewebion.com/hdtest/live/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/XsXzKJG/varzesh.png",IRIB VARZESH
https://ncdn.telewebion.com/varzesh/live/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/xHSzVy5/eshareh.png",IRIB ESHAREH
https://ncdn.telewebion.com/eshragh/live/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/hVkbvpQ/irinn.png",IRIB IRINN
https://ncdn.telewebion.com/irinn/live/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/hVkbvpQ/irinn.png",IRIB IRINN 2
https://ncdn.telewebion.com/irinn2/live/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/kDhcymF/ifilm.png",IFILM IR
https://ncdn.telewebion.com/ifilm/live/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/X5KJmDS/aiosport1.jpg",IRIB TWSPORT
https://ncdn.telewebion.com/twsport/live/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/VDQwTkz/aiosport2.jpg",IRIB TWSPORT 2
https://ncdn.telewebion.com/twsport2/live/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/X5KJmDS/aiosport1.jpg",IRIB TWSPORT 3
https://ncdn.telewebion.com/twsport3/live/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tqkV2sn/irflag.png",JJTV 1
https://ncdn.telewebion.com/jjtv1/live/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tqkV2sn/irflag.png",JJTV 3
https://ncdn.telewebion.com/jjtv3/live/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tqkV2sn/irflag.png",SEPEHR
https://ncdn.telewebion.com/sepehr/live/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tqkV2sn/irflag.png",OMID
https://ncdn.telewebion.com/omid/live/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tqkV2sn/irflag.png",OFOGH
https://ncdn.telewebion.com/ofogh/live/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tqkV2sn/irflag.png",QURAN
https://ncdn.telewebion.com/quran/live/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tqkV2sn/irflag.png",PALESTINE
https://ncdn.telewebion.com/palestine/live/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tqkV2sn/irflag.png",JAM
https://ncdn.telewebion.com/jam/live/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tqkV2sn/irflag.png",SHARAFGHAN
https://ncdn.telewebion.com/saharafghan/live/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tqkV2sn/irflag.png",NAVA
https://ncdn.telewebion.com/nava/live/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tqkV2sn/irflag.png",NAMA
https://ncdn.telewebion.com/nama/live/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tqkV2sn/irflag.png",ARA
https://ncdn.telewebion.com/ara/live/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tqkV2sn/irflag.png",HABIB
https://ncdn.telewebion.com/habib/live/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tqkV2sn/irflag.png",AZARBAYJANGHARBI
https://ncdn.telewebion.com/azarbayjangharbi/live/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tqkV2sn/irflag.png",SAHAND
https://ncdn.telewebion.com/sahand/live/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tqkV2sn/irflag.png",ALBORZ
https://ncdn.telewebion.com/alborz/live/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tqkV2sn/irflag.png",ESFAHAN
https://ncdn.telewebion.com/esfahan/live/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tqkV2sn/irflag.png",SABALAN
https://ncdn.telewebion.com/sabalan/live/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tqkV2sn/irflag.png",ILAM
https://ncdn.telewebion.com/ilam/live/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tqkV2sn/irflag.png",BUSHEHR
https://ncdn.telewebion.com/bushehr/live/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tqkV2sn/irflag.png",JAHANBIN
https://ncdn.telewebion.com/jahanbin/live/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tqkV2sn/irflag.png",ABADAN
https://ncdn.telewebion.com/abadan/live/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tqkV2sn/irflag.png",KHORASANRAZAVI
https://ncdn.telewebion.com/khorasanrazavi/live/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tqkV2sn/irflag.png",ATRAK
https://ncdn.telewebion.com/atrak/live/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tqkV2sn/irflag.png",KHALIJEFARS
https://ncdn.telewebion.com/khalijefars/live/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tqkV2sn/irflag.png",KHOOZESTAN
https://ncdn.telewebion.com/khoozestan/live/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tqkV2sn/irflag.png",SEMNAN
https://ncdn.telewebion.com/semnan/live/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tqkV2sn/irflag.png",HAMOON
https://ncdn.telewebion.com/hamoon/live/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tqkV2sn/irflag.png",FARS
https://ncdn.telewebion.com/fars/live/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tqkV2sn/irflag.png",QAZVIN
https://ncdn.telewebion.com/qazvin/live/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tqkV2sn/irflag.png",NOOR
https://ncdn.telewebion.com/noor/live/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tqkV2sn/irflag.png",KERMAN
https://ncdn.telewebion.com/kerman/live/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tqkV2sn/irflag.png",DENA
https://ncdn.telewebion.com/dena/live/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tqkV2sn/irflag.png",ZAGROS
https://ncdn.telewebion.com/zagros/live/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tqkV2sn/irflag.png",KISH
https://ncdn.telewebion.com/kish/live/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tqkV2sn/irflag.png",SABZ
https://ncdn.telewebion.com/sabz/live/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tqkV2sn/irflag.png",BARAN
https://ncdn.telewebion.com/baran/live/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tqkV2sn/irflag.png",KORDESTAN
https://ncdn.telewebion.com/kordestan/live/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tqkV2sn/irflag.png",TABAN
https://ncdn.telewebion.com/taban/live/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tqkV2sn/irflag.png",TABARESTAN
https://ncdn.telewebion.com/tabarestan/live/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tqkV2sn/irflag.png",AFTAB
https://ncdn.telewebion.com/aftab/live/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tqkV2sn/irflag.png",MAHABAD
https://ncdn.telewebion.com/mahabad/live/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tqkV2sn/irflag.png",SINA
https://ncdn.telewebion.com/sina/live/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tqkV2sn/irflag.png",KHAVARAN
https://ncdn.telewebion.com/khavaran/live/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/hVkbvpQ/irinn.png",IRIB IRINN
https://s1.ettehadlive.com/live/42/chunklist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/kDhcymF/ifilm.png",IRIB IFILM FAR
https://live.presstv.ir/hls/ifilmfa_4_482/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tqkV2sn/irflag.png",MBC PERSIA
https://shls-mbcpersia-prod-dub.shahid.net/out/v1/bdc7cd0d990e4c54808632a52c396946/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tqkV2sn/irflag.png",MBC PERSIA
https://mbcpersia-prod-dub-ak.akamaized.net/out/v1/bdc7cd0d990e4c54808632a52c396946/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tqkV2sn/irflag.png",HASTI TV
https://live.hastitv.com/hls/livetv.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tqkV2sn/irflag.png",ASIL TV
https://live.asil.tv/asiltv/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tqkV2sn/irflag.png",SNN TV
https://live2.snn.ir/hls/snn.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tqkV2sn/irflag.png",NEJAT TV
https://hls.nejat.live/hls/stream.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tqkV2sn/irflag.png",VOX 1
https://hls.vox1.live/hls/stream.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tqkV2sn/irflag.png",YOUR TIME
https://hls.yourtime.live/hls/stream.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tqkV2sn/irflag.png",HOD HOD
https://hls.hodhod.live/hls/stream.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tqkV2sn/irflag.png",24/7 BOX
https://hls.247box.live/hls/stream.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tqkV2sn/irflag.png",OX IR
https://hls.oxir.live/hls/stream.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tqkV2sn/irflag.png",AVA FAMILY
https://familyhls.avatv.live/hls/stream.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tqkV2sn/irflag.png",PARS
https://parshls.wns.live/hls/stream.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tqkV2sn/irflag.png",SL ONE
https://slonehls.wns.live/hls/stream.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tqkV2sn/irflag.png",SL TWO
https://sltwohls.wns.live/hls/stream.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tqkV2sn/irflag.png",P FILM
https://pfilmhls.wns.live/hls/stream.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tqkV2sn/irflag.png",ITN
https://itnhls.wns.live/hls/stream.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tqkV2sn/irflag.png",META FILM
https://metafilmhls.wns.live/hls/stream.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tqkV2sn/irflag.png",AVA SERIES
https://avaserieshls.wns.live/hls/stream.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tqkV2sn/irflag.png",BRAVOO
https://bravoohls.wns.live/hls/stream.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tqkV2sn/irflag.png",FX TV
https://fxtvhls.wns.live/hls/stream.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tqkV2sn/irflag.png",OI TN
https://oitnhls.wns.live/hls/stream.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tqkV2sn/irflag.png",TAPESH
https://iptv.tapesh.tv/tapesh/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tqkV2sn/irflag.png",TAPESH IR
https://iptv.tapesh.tv/tapeshiran/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tqkV2sn/irflag.png",MIHAN TV
https://iptv.mihantv.com/mihantv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tqkV2sn/irflag.png",NEGAH TV
https://iptv.negahtv.com/negahtv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tqkV2sn/irflag.png",AL WILAYAH
https://hls.nl3.livekadeh.com/hls2/alwilayah_tv.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tqkV2sn/irflag.png",PAYVAND
https://uni6rtmp.tulix.tv/ucur1/Payvand/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tqkV2sn/irflag.png",PJ TV
https://uni01rtmp.tulix.tv/kensecure/pjtv.stream/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tqkV2sn/irflag.png",PMC TV
https://hls.pmc.live/hls/stream.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tqkV2sn/irflag.png",ASSIRAT
https://svs.itworkscdn.net/assiratvlive/assirat/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tqkV2sn/irflag.png",PERSIANA NOSTALGIA
https://noshls.persiana.live/hls/stream.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tqkV2sn/irflag.png",PERSIANA MUSIC
https://musichls.persiana.live/hls/stream.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tqkV2sn/irflag.png",PERSIANA TURKIYE
https://turkhls.persiana.live/hls/stream.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tqkV2sn/irflag.png",PERSIANA COMEDY
https://comedyhls.persiana.live/hls/stream.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tqkV2sn/irflag.png",PERSIANA IRANIAN
https://irhls.persiana.live/hls/stream.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tqkV2sn/irflag.png",PERSIANA ONE
https://onehls.persiana.live/hls/stream.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tqkV2sn/irflag.png",PERSIANA TWO
https://twohls.persiana.live/hls/stream.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tqkV2sn/irflag.png",PERSIANA KOREA
https://korhls.persiana.live/hls/stream.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tqkV2sn/irflag.png",PERSIANA CINEMA
https://cinehls.persiana.live/hls/stream.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tqkV2sn/irflag.png",PERSIANA HD
https://euhls.persiana.live/hls/stream.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tqkV2sn/irflag.png",PERSIANA LATINO
https://latinohls.persiana.live/hls/stream.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tqkV2sn/irflag.png",PERSIANA FAMILY
https://familyhls.persiana.live/hls/stream.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tqkV2sn/irflag.png",PERSIANA SCIENCE
https://scihls.persiana.live/hls/stream.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tqkV2sn/irflag.png",PERSIANA JUNIOR
https://junhls.persiana.live/hls/stream.m3u8
#EXTINF:-1 group-title="26. |IR|🇮🇷 IRAN",--- |⬇DOWN-OFF/TOKENED⬇| ---
http://blank
#EXTINF:-1 tvg-logo="https://i.ibb.co/tMV7LBL/irib1.png",IRIB 1
https://lb-cdn.sepehrtv.ir/securelive3/tv1hd/tv1hd.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tMV7LBL/irib1.png",IRIB 1
https://live.aionet.ir/hls/tv1/tv1.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/6ndKkPM/irib2.png",IRIB 2
https://lb-cdn.sepehrtv.ir/securelive3/tv1hd/tv1hd.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/6ndKkPM/irib2.png",IRIB 2
https://live.aionet.ir/hls/tv2/tv2.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/4YQsfv9/irib3.png",IRIB 3
https://af.ayas.ir/hls2/tv3.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/4YQsfv9/irib3.png",IRIB 3
https://live.aionet.ir/hls/tv3/tv3.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/D5S2Q2z/irib4.png",IRIB 4
https://live.aionet.ir/hls/tv4/tv4.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Kzb8VkY/irib5.png",IRIB 5
https://live.aionet.ir/hls/tv5/tv5.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/GMLStpQ/amoozesh.png",IRIB AMOOZESH
https://live.aionet.ir/hls/amoozesh/amoozesh.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/1LmYfnH/mostanad.png",IRIB MOSTANAD
https://live.aionet.ir/hls/mostanad/mostanad.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/wsVP42F/namayesh.png",IRIB NAMAYESH
https://live.aionet.ir/hls/namayesh/namayesh.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/pwxkFvX/nassim.jpg",IRIB NASIM
https://live.aionet.ir/hls/nasim/nasim.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/RgQXYbM/pooya.png",IRIB POOYA
https://live.aionet.ir/hls/pooya/pooya.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/wJHhH03/salamat.png",IRIB SALAMAT
https://live.aionet.ir/hls/salamat/salamat.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/PYMzQFX/tamasha.png",IRIB TAMASHA
https://live.aionet.ir/hls/tamasha/tamasha.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/XsXzKJG/varzesh.png",IRIB VARZESH
https://live.aionet.ir/hls/varzesh/varzesh.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/N6PTbMG/mesrafsanjan.png",IRIB MESRAFSANJAN
https://live.aionet.ir/hls/mesrafsanjan/mesrafsanjan.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/xHSzVy5/eshareh.png",IRIB ESHAREH
https://live.aionet.ir/hls/eshareh/eshareh.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/hVkbvpQ/irinn.png",IRIB IRINN
https://live.aionet.ir/hls/irinn/irinn.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/X5KJmDS/aiosport1.jpg",IRIB AIOSPORT
https://live.aionet.ir/hls/aiosport/aiosport.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/VDQwTkz/aiosport2.jpg",IRIB AIOSPORT 2
https://live.aionet.ir/hls/aiosport2/aiosport2.m3u8


#EXTINF:-1 tvg-logo="https://i.ibb.co/XbSHxd5/cnn.png" group-title="27. |EN-UK-US|🇬🇧🇺🇸 WORLDWIDE-INTL ℹ️🌐",CNN INT
https://d3696l48vwq25d.cloudfront.net/v1/master/3722c60a815c199d9c0ef36c5b73da68a62b09d1/cc-0g2918mubifjw/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/XbSHxd5/cnn.png",CNN INT
https://d1yx2biofua75q.cloudfront.net/v1/master/3722c60a815c199d9c0ef36c5b73da68a62b09d1/cc-agcuky3hp0j0j/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/XbSHxd5/cnn.png" user-agent="Star Wars",CNN INT
https://turnerlive.warnermediacdn.com/hls/live/586495/cnngo/cnn_slate/VIDEO_0_3564000.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/XbSHxd5/cnn.png" user-agent="Star Wars",CNN INT
https://turnerlive.warnermediacdn.com/hls/live/586497/cnngo/cnni/VIDEO_0_3564000.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/XbSHxd5/cnn.png" user-agent="Star Wars",CNN INT
https://d3bp6dwmpbdajl.cloudfront.net/v1/master/3722c60a815c199d9c0ef36c5b73da68a62b09d1/cc-ury0meh5m4nzm/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/XbSHxd5/cnn.png" user-agent="Star Wars",CNN FAST
https://amg01448-samsungin-cnnnow-samsungin-4npqg.amagi.tv/playlist/amg01448-samsungin-cnnnow-samsungin/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/XbSHxd5/cnn.png" user-agent="Star Wars",CNN FAST
https://cdn-uw2-prod.tsv2.amagi.tv/linear/amg00405-rakutentv-cnnfastlg-rakuten-lgfr/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/XbSHxd5/cnn.png" user-agent="Star Wars",CNN FAST
https://d2anxhed2mfixb.cloudfront.net/v1/master/3722c60a815c199d9c0ef36c5b73da68a62b09d1/cc-wqc602hxepp0q/CNNFAST_GB.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/XbSHxd5/cnn.png" user-agent="Star Wars",CNN FAST
https://d3fzntptkfpmvg.cloudfront.net/v1/master/3722c60a815c199d9c0ef36c5b73da68a62b09d1/cc-6rc4k0y56fezj/CNNFAST_GB.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/hdBrzcc/fox.png",FOX NEWS
https://fox-foxnewsnow-samsungus.amagi.tv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/hdBrzcc/fox.png",FOX NEWS
https://fox-foxnewsnow-vizio.amagi.tv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/hdBrzcc/fox.png",FOX NEWS
https://d3tlzddkbbpp5n.cloudfront.net/v1/master/3722c60a815c199d9c0ef36c5b73da68a62b09d1/cc-9uzjfw11uj9nn/LiveNOW_from_FOX.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/hdBrzcc/fox.png",FOX NEWS
https://livetv-fa.tubi.video/fox-live-now/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/hdBrzcc/fox.png",FOX NEWS
https://247preview.foxnews.com/hls/live/2020027/fncv3preview/primary.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/CKTjvj8/nbc.jpg",NBC NEWS
https://d2gjhy8g9ziabr.cloudfront.net/v1/master/3fec3e5cac39a52b2132f9c66c83dae043dc17d4/prod-samsungtvplus-stitched/samsungtvplus_us_nbcnewsnow_001.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/CKTjvj8/nbc.jpg",NBC NEWS
https://d2gjhy8g9ziabr.cloudfront.net/v1/master/3fec3e5cac39a52b2132f9c66c83dae043dc17d4/prod-samsungtvplus-stitched/samsungtvplus_ca_nbcnewsnow_001.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/CKTjvj8/nbc.jpg",NBC NEWS
https://d2gjhy8g9ziabr.cloudfront.net/v1/master/3fec3e5cac39a52b2132f9c66c83dae043dc17d4/prod-samsungtvplus-stitched/samsungtvplus_eu_nbcnewsnow_003.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/CKTjvj8/nbc.jpg",NBC NEWS
https://d2ww7x6333b6qp.cloudfront.net/10507/88886006/hls/master.m3u8?ads.xumo_channelId=88886006
#EXTINF:-1 tvg-logo="https://i.ibb.co/CKTjvj8/nbc.jpg",NBC NEWS
http://dai2.xumo.com/xumocdn/p=roku/amagi_hls_data_xumo1212A-xumo-nbcnewsnow/CDN/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/CKTjvj8/nbc.jpg",NBC NEWS
https://d4ybyqrhce41r.cloudfront.net/v1/master/3fec3e5cac39a52b2132f9c66c83dae043dc17d4/prod-xumo-linear-nbcu-hlsv3/master.m3u8?ads.channelId=99991626
#EXTINF:-1 tvg-logo="https://i.ibb.co/CKTjvj8/nbc.jpg",NBC NEWS
https://d4ybyqrhce41r.cloudfront.net/v1/master/3fec3e5cac39a52b2132f9c66c83dae043dc17d4/prod-xumo-linear-nbcu-hlsv3/master.m3u8?ads.channelId=99991247
#EXTINF:-1 tvg-logo="https://i.ibb.co/CKTjvj8/nbc.jpg",NBC NEWS
https://livetv-fa.tubi.video/nbc-news-now/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/CKTjvj8/nbc.jpg",NBC NEWS
http://stitcher-ipv4.pluto.tv/v1/stitch/embed/hls/channel/5df97894467dfa00091c873clivestitch/master.m3u8?deviceDNT=%7BTARGETOPT%7D&deviceModel=samsung&deviceVersion=unknown&appVersion=unknown&deviceType=samsung-tvplus&deviceMake=samsung
#EXTINF:-1 tvg-logo="https://i.ibb.co/jJDxCxN/abc.jpg",ABC NEWS
https://d2fewflvrapcwe.cloudfront.net/v1/master/3722c60a815c199d9c0ef36c5b73da68a62b09d1/cc-fdwnvbyln7gak-ssai-prd/ABCNewsLive_Disney.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/jJDxCxN/abc.jpg",ABC NEWS
https://content.uplynk.com/channel/3324f2467c414329b3b0cc5cd987b6be.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/jJDxCxN/abc.jpg",ABC NEWS
https://content.uplynk.com/channel/ext/72750b711f704e4a94b5cfe6dc99f5e1/wabc_24x7_news.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/jJDxCxN/abc.jpg",ABC NEWS
https://abcnews-streams.akamaized.net/hls/live/2023560/abcnews1/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/YD3G64y/cbs.jpg",CBS NEWS
https://cbsn-us.cbsnstream.cbsnews.com/out/v1/55a8648e8f134e82a470f83d562deeca/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/YD3G64y/cbs.jpg",CBS NEWS
https://dai.google.com/linear/hls/event/EezGs5EpSjSr-sYjB2qysw/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/YD3G64y/cbs.jpg",CBS NEWS
https://dai.google.com/ssai/event/Sid4xiTQTkCT1SLu6rjUSQ/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/YD3G64y/cbs.jpg",CBS NEWS
http://stitcher-ipv4.pluto.tv/v1/stitch/embed/hls/channel/6231ec93779a9d00079ba8e2livestitch/master.m3u8?deviceDNT=%7BTARGETOPT%7D&deviceModel=samsung&deviceVersion=unknown&appVersion=unknown&deviceType=samsung-tvplus&deviceMake=samsung
#EXTINF:-1 tvg-logo="https://i.ibb.co/YD3G64y/cbs.jpg",CBS NEWS
https://cfd-v4-service-channel-stitcher-use1-1.prd.pluto.tv/stitch/hls/channel/5a6b92f6e22a617379789618/master.m3u8?sid=0&deviceDNT=0&deviceId=0&deviceModel=unknown&deviceVersion=unknown&appVersion=unknown&deviceType=unknown&deviceMake=unknown
#EXTINF:-1 tvg-logo="https://i.ibb.co/FxZYHhM/cnbc.jpg",CNBC NEWS
https://amg01079-nbcuuk-amg01079c2-lg-gb-2030.playouts.now.amagi.tv/playlist/amg01079-nbcuukfast-cnbcuk-lggb/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/FxZYHhM/cnbc.jpg",CNBC NEWS
https://amg01079-nbcuuk-amg01079c1-lg-fr-2032.playouts.now.amagi.tv/playlist/amg01079-nbcuukfast-cnbcpe-lgfr/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/FxZYHhM/cnbc.jpg",CNBC NEWS
https://new.cache-stream.workers.dev/stream/UCvJJ_dzjViJCoLf5uKUTwoA/live.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/rH3FDN2/cheddar.jpg",CHEDDAR NEWS
https://livestream.chdrstatic.com/b93e5b0d43ea306310a379971e384964acbe4990ce193c0bd50078275a9a657d/cheddar-42620/cheddarweblive/cheddar/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/rH3FDN2/cheddar.jpg",CHEDDAR NEWS
https://cheddar-us.samsung.wurl.tv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/yNdTPqt/newsmax.png",NEWS MAX
https://nmx1ota.akamaized.net/hls/live/2107010/Live_1/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/yNdTPqt/newsmax.png",NEWS MAX
https://nmxlive.akamaized.net/hls/live/529965/Live_1/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/yNdTPqt/newsmax.png",NEWS MAX
https://newsmax-samsungus.amagi.tv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/VMm5SSz/realamv.png",REAL AMERICAS VOICE
https://d2jiqiw4g5lj5k.cloudfront.net/v1/master/3722c60a815c199d9c0ef36c5b73da68a62b09d1/AmericasVoiceChannel-prod/AVSamsung/AVSamsung.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/VMm5SSz/realamv.png",REAL AMERICAS VOICE
https://content.uplynk.com/channel/26bd482ffe364a1282bc3df28bd3c21f.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/nDJHCWt/Usatod.png",USA TODAY
https://cdn-ue1-prod.tsv2.amagi.tv/linear/amg00731-gannettcoinc-usatodaynews-plex/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/nDJHCWt/Usatod.png",USA TODAY
https://lnc-usa-today.tubi.video/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/nDJHCWt/Usatod.png",USA TODAY
https://dai2.xumo.com/amagi_hls_data_xumo1212A-redboxusatoday/CDN/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/kX8ywwV/oan.png",OANN
https://oneamericanews-vizio.amagi.tv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/kX8ywwV/oan.png",OANN
https://d35j504z0x2vu2.cloudfront.net/v1/master/0bc8e8376bd8417a1b6761138aa41c26c7309312/oan-encore/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/kX8ywwV/oan.png",OANN
https://cdn.herringnetwork.com/80A4DFF/oane_oregon/OAN_Encore.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/71WgnqJ/HLN.png" user-agent="Star Wars",HLN
https://turnerlive.warnermediacdn.com/hls/live/586496/cnngo/hln/VIDEO_0_3564000.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Vt0XZKf/Cbcnews.png",CBC NEWS
https://dai2.xumo.com/amagi_hls_data_xumo1212A-redboxcbcnews/CDN/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Vt0XZKf/Cbcnews.png",CBC NEWS
https://d36tuf8zz9b2bm.cloudfront.net/v1/master/3722c60a815c199d9c0ef36c5b73da68a62b09d1/cc-hfw6opvomwxih/CBC_News_International.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/q0FfqdV/Globalnews.png",GLOBAL NEWS
https://live.corusdigitaldev.com/groupd/live/49a91e7f-1023-430f-8d66-561055f3d0f7/live.isml/live.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/dPmZMqq/bbcn.png",BBC NEWS
https://vs-hls-push-ww-live.akamaized.net/x=4/i=urn:bbc:pips:service:bbc_news_channel_hd/pc_hd_abr_v2.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/dPmZMqq/bbcn.png",BBC NEWS
https://vs-hls-push-ww-live.akamaized.net/x=4/i=urn:bbc:pips:service:bbc_news_channel_hd/t=3840/v=pv14/b=5070016/main.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/dPmZMqq/bbcn.png",BBC NEWS
https://vs-hls-push-ww.live.cf.md.bbci.co.uk/x=4/i=urn:bbc:pips:service:bbc_news_channel_hd/mobile_wifi_main_sd_abr_v2.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/dPmZMqq/bbcn.png",BBC NEWS
https://d2vnbkvjbims7j.cloudfront.net/containerA/LTN/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/dPmZMqq/bbcn.png",BBC NEWS
https://d3pxo1qcgzxtxs.cloudfront.net/10005/99951298/hls/playlist.m3u8?ads.xumo_channelId=99951298
#EXTINF:-1 tvg-logo="https://i.ibb.co/dPmZMqq/bbcn.png",BBC NEWS
https://d1kvlt93j1bc49.cloudfront.net/v1/master/3722c60a815c199d9c0ef36c5b73da68a62b09d1/cc-6vpx7bvwjm7ao/v1/amcnetworks_bbcnews_1/samsungheadend_us/latest/main/hls/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/8MBM4M1/skyn.png",SKY NEWS
https://d2gjhy8g9ziabr.cloudfront.net/v1/master/3fec3e5cac39a52b2132f9c66c83dae043dc17d4/prod-samsungtvplus-stitched/samsungtvplus_us_skynewsamericas_001.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/8MBM4M1/skyn.png",SKY NEWS
https://linear417-gb-hls1-prd-ak.cdn.skycdp.com/100e/Content/HLS_001_1080_30/Live/channel(skynews)/index_1080-30.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/8MBM4M1/skyn.png",SKY NEWS
https://linear417-gb-hls3-prd-ak.cdn.skycdp.com/100e/Content/HLS_004_1080_30/Live/channel(skynews)/index_1080.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/8MBM4M1/skyn.png",SKY NEWS
http://stitcher-ipv4.pluto.tv/v1/stitch/embed/hls/channel/55b285cd2665de274553d66flivestitch/master.m3u8?deviceDNT=%7BTARGETOPT%7D&deviceModel=samsung&deviceVersion=unknown&appVersion=unknown&deviceType=samsung-tvplus&deviceMake=samsung
#EXTINF:-1 tvg-logo="https://i.ibb.co/dpMQyVx/gbn.png",GB NEWS
https://amg01076-lightningintern-gbnews-samsunguk-0lu52.amagi.tv/playlist/amg01076-lightningintern-gbnews-samsunguk/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/dpMQyVx/gbn.png",GB NEWS
https://live-gbnews.simplestreamcdn.com/live5/gbnews/bitrate1.isml/manifest.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/dpMQyVx/gbn.png",GB NEWS
https://live-gbnews-ssai.simplestreamcdn.com/v1/master/82267e84b9e5053b3fd0ade12cb1a146df74169a/gbnews-live-TEST/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/XWNXpVg/talk.png",TALK NEWS
https://live-talktv-ssai.simplestreamcdn.com/v1/master/774d979dd66704abea7c5b62cb34c6815fda0d35/talktv-live/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/GV4JLkr/Guardian.png",THE GUARDIAN CHANNEL
https://0d0239e437124ddcb8090d815caf4013.mediatailor.us-east-1.amazonaws.com/v1/master/04fd913bb278d8775298c26fdca9d9841f37601f/Samsung-gb_TheGuardianChannel/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/GV4JLkr/Guardian.png",THE GUARDIAN CHANNEL
https://d73fb24db4524ddca65ec4935761d3ef.mediatailor.us-east-1.amazonaws.com/v1/master/04fd913bb278d8775298c26fdca9d9841f37601f/RakutenTV-eu_TheGuardianChannel/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/GV4JLkr/Guardian.png",THE GUARDIAN CHANNEL
https://the-guardian-3d0e32e7-aa40-49e5-b9d9-c433151fa61a-fr.fast.rakuten.tv/v1/master/0547f18649bd788bec7b67b746e47670f558b6b2/production-LiveChannel-6437/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/W6TrwQx/freespech.png",FREE SPEECH TV
https://edge.fstv-live-linear-channel.top.comcast.net/Content/HLS_HLSv3/Live/channel(b168a609-19c1-2203-ae1d-6b9726f05e67)/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Cs2Gv1ZG/courttv.jpg",COURT TV
https://content.uplynk.com/channel/6c0bd0f94b1d4526a98676e9699a10ef.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/2YKQ7bR9/newsworld.jpg",NEWS WORLD
https://amg01076-lightning-amg01076c5-rakuten-us-1788.playouts.now.amagi.tv/playlist/amg01076-lightning-newsworld-rakutenus/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/DCntyzt/reuterstv.png",REUTERS TV
https://amg00453-reuters-amg00453c1-samsung-de-2111.playouts.now.amagi.tv/playlist/amg00453-reuters-reuters-samsungde/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/DCntyzt/reuterstv.png",REUTERS TV
https://amg00453-reuters-amg00453c1-samsung-fr-2112.playouts.now.amagi.tv/playlist/amg00453-reuters-reuters-samsungfr/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/DCntyzt/reuterstv.png",REUTERS TV
https://d2kjqd7acfrwt3.cloudfront.net/playlist/amg00453-reuters-reuters-rakutenuk/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/17rc425/voa.png",VOA TV
https://voa-ingest.akamaized.net/hls/live/2033874/tvmc06/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/x82vM4r9/Cspan.png",C-SPAN
http://fl2.moveonjoy.com/C-SPAN/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Nn5x9Hq/bloom.jpg",BLOOMBERG UK
https://bloomberg-bloombergtv-1-gb.samsung.wurl.tv/manifest/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Nn5x9Hq/bloom.jpg",BLOOMBERG UK
https://bc20d7c2a7b14dd0ae827a2e3eb99116.mediatailor.us-east-1.amazonaws.com/v1/master/44f73ba4d03e9607dcd9bebdcb8494d86964f1d8/Samsung-gb_Bloomberg/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Nn5x9Hq/bloom.jpg",BLOOMBERG US
https://0984ed0046994029aafaa07692005474.mediatailor.us-east-1.amazonaws.com/v1/master/44f73ba4d03e9607dcd9bebdcb8494d86964f1d8/Samsung_Bloomberg/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Nn5x9Hq/bloom.jpg",BLOOMBERG US
https://bloomberg-bloombergtv-1-us.samsung.wurl.tv/manifest/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Nn5x9Hq/bloom.jpg",BLOOMBERG US
https://www.bloomberg.com/media-manifest/streams/us-event.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Nn5x9Hq/bloom.jpg",BLOOMBERG US
https://bloomberg.com/media-manifest/streams/eu.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Nn5x9Hq/bloom.jpg",BLOOMBERG US
https://www.bloomberg.com/media-manifest/streams/phoenix-us.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Nn5x9Hq/bloom.jpg",BLOOMBERG EU
https://bloomberg-bloombergtv-5-eu.plex.wurl.tv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Nn5x9Hq/bloom.jpg",BLOOMBERG EU
https://8c916ce141544c85a361e55898216cf0.mediatailor.us-east-1.amazonaws.com/v1/master/04fd913bb278d8775298c26fdca9d9841f37601f/RakutenTV-eu_Bloomberg-2/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Nn5x9Hq/bloom.jpg",BLOOMBERG EU
https://www.bloomberg.com/media-manifest/streams/eu.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Nn5x9Hq/bloom.jpg",BLOOMBERG EU
https://bloomberg-bloombergtv-6-eu.rakuten.wurl.tv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Nn5x9Hq/bloom.jpg",BLOOMBERG QUICK
https://bloomberg-quicktake-2-eu.rakuten.wurl.tv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Nn5x9Hq/bloom.jpg",BLOOMBERG EVENT
https://bloomberg.com/media-manifest/streams/eu-event.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Nn5x9Hq/bloom.jpg",BLOOMBERG ORIGINALS
https://ab1455372fed47d8a88264bab4831d5c.mediatailor.us-east-1.amazonaws.com/v1/master/44f73ba4d03e9607dcd9bebdcb8494d86964f1d8/Samsung_QuickTake-1/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Nn5x9Hq/bloom.jpg",BLOOMBERG ORIGINALS
https://f559b0b61c424ec891e6b7d9963cdd01.mediatailor.us-east-1.amazonaws.com/v1/master/f4e8c53a8367a5b58e20ce054ea3ce25a3e904d3/Samsung-gb_QuickTake/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Nn5x9Hq/bloom.jpg",BLOOMBERG ORIGINALS
https://bloomberg-quicktake-4-us.plex.wurl.tv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Nn5x9Hq/bloom.jpg",BLOOMBERG ORIGINALS
https://bloomberg-quicktake-4-gb.samsung.wurl.tv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Nn5x9Hq/bloom.jpg",BLOOMBERG ORIGINALS
https://d7ec4f6950ed4c6d946e497bd44db7ef.mediatailor.us-east-1.amazonaws.com/v1/master/44f73ba4d03e9607dcd9bebdcb8494d86964f1d8/RakutenTV-eu_QuickTake-1/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/R4xVMYc/enews.png",EURONEWS EN
https://62d77612985e4978b5cec13c47c897b5.mediatailor.us-east-1.amazonaws.com/v1/master/44f73ba4d03e9607dcd9bebdcb8494d86964f1d8/Samsung-gb_EuroNewsLive-1/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/VxLFYSj/euronews.png",EURONEWS EN
https://euronews-live-eng-uk.fast.rakuten.tv/v1/master/0547f18649bd788bec7b67b746e47670f558b6b2/production-LiveChannel-6503/bitok/e/26031/euronews-en.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/R4xVMYc/enews.png",EURONEWS EN
http://stitcher-ipv4.pluto.tv/v1/stitch/embed/hls/channel/5ca1da6c593a5d78f0e7edcelivestitch/master.m3u8?deviceDNT=%7BTARGETOPT%7D&deviceModel=samsung&deviceVersion=unknown&appVersion=unknown&deviceType=samsung-tvplus&deviceMake=samsung
#EXTINF:-1 tvg-logo="https://i.ibb.co/R4xVMYc/enews.png",EURONEWS EN
https://shls-live-ak.akamaized.net/out/v1/115bfcde8fa342d182ef846445cdbdcf/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/R4xVMYc/enews.png",EURONEWS EN
https://d35j504z0x2vu2.cloudfront.net/v1/master/0bc8e8376bd8417a1b6761138aa41c26c7309312/euronews/euronews-en.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/R4xVMYc/enews.png",EURONEWS EN
https://euronews-euronews-world-1-nz.samsung.wurl.tv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/R4xVMYc/enews.png",EURONEWS EN
https://euronews-euronews-world-1-us.plex.wurl.tv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/R4xVMYc/enews.png",EURONEWS EN
https://jmp2.uk/sam-GB2600019ON.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/XSYtYHZ/africanews.png",AFRICANEWS EN
https://rakuten-africanews-1-ie.samsung.wurl.tv/manifest/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/XSYtYHZ/africanews.png",AFRICANEWS EN
https://37c774660687468c821a51190046facf.mediatailor.us-east-1.amazonaws.com/v1/master/04fd913bb278d8775298c26fdca9d9841f37601f/RakutenTV-gb_AfricaNews/playlist.m3u8 
#EXTINF:-1 tvg-logo="https://i.ibb.co/gFjck13/ebssat.png",EUROPE BY SAT
https://eucom-live.freecaster.com/eucom/96098bf4-5a2a-466b-8d7f-e35300fa4f28/96098bf4-5a2a-466b-8d7f-e35300fa4f28.isml/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/gFjck13/ebssat.png",EUROPE BY SAT
https://euc-live.fl.freecaster.net/live/eucom/ebs.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/gFjck13/ebssat.png",EUROPE BY SAT
https://streams.prd.commavservices.eu/live/ebs/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/gFjck13/ebssat.png",EUROPE BY SAT +
https://streams.prd.commavservices.eu/live/ebsplus/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/gFjck13/ebssat.png",EUROPE BY SAT +
https://eucom-live.freecaster.com/eucom/96098c0b-0743-4afc-9562-db1673053f9d/96098c0b-0743-4afc-9562-db1673053f9d.isml/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/gFjck13/ebssat.png",EUROPE BY SAT +
https://euc-live.fl.freecaster.net/live/eucom/ebsp.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mBTzvw8/Abcau.png",ABC NEWS AUSTRALIA
https://abc-iview-mediapackagestreams-2.akamaized.net/out/v1/6e1cc6d25ec0480ea099a5399d73bc4b/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mBTzvw8/Abcau.png",ABC NEWS AUSTRALIA
https://abc-news-dmd-streams-1.akamaized.net/out/v1/abc83881886746b0802dc3e7ca2bc792/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mBTzvw8/Abcau.png",ABC NEWS AUSTRALIA
https://abc-news-dmd-streams-1.akamaized.net/out/v1/701126012d044971b3fa89406a440133/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/8MBM4M1/skyn.png",SKY NEWS AUSTRALIA
https://amg00663-skynews-skynewsau-samsungau-r7n40.amagi.tv/playlist/amg00663-skynews-skynewsau-samsungau/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/94BB1cD/indiatod.jpg",INDIA TODAY
https://indiatodaylive.akamaized.net/hls/live/2014320/indiatoday/indiatodaylive/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/prZ8kjdR/Wion.png",WION NEWS INDIA
https://d7x8z4yuq42qn.cloudfront.net/index_1.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/7J24bwVD/cnaid.png",CHANNEL NEWS ASIA
http://d2e1asnsl7br7b.cloudfront.net/7782e205e72f43aeb4a48ec97f66ebbe/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/hKP8X8B/f24.png",FRANCE 24 EN
https://live.france24.com/hls/live/2037218/F24_EN_HI_HLS/master_5000.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/hKP8X8B/f24.png",FRANCE 24 EN
https://live.france24.com/hls/live/2037218/F24_EN_HI_HLS/master_2300.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/hKP8X8B/f24.png",FRANCE 24 EN
https://cdn.klowdtv.net/803B48A/n1.klowdtv.net/live2/france24_720p/chunks.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/hKP8X8B/f24.png",FRANCE 24 EN
https://amg00106-france24-france24-samsunguk-qvpp8.amagi.tv/playlist/amg00106-france24-france24-samsunguk/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/hKP8X8B/f24.png",FRANCE 24 FAST
https://amg00106-france24-france24-samsungde-39lcm.amagi.tv/playlist/amg00106-france24-france24-samsungde/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/hKP8X8B/f24.png",FRANCE 24 FAST
https://amg00106-france24-france24-samsunguk-qvpp8.amagi.tv/playlist/amg00106-france24-france24-samsunguk/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/hKP8X8B/f24.png",FRANCE 24 FAST
https://amg00106-amg00106c1-rakuten-uk-4654.playouts.now.amagi.tv/playlist/amg00106-france24fast-france24-rakutenuk/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/84XLZJq/dw.png",DW ENGLISH
https://dwamdstream102.akamaized.net/hls/live/2015525/dwstream102/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/84XLZJq/dw.png",DW ENGLISH +
https://dwamdstream105.akamaized.net/hls/live/2015531/dwstream105/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/84XLZJq/dw.png",DW ENGLISH +
https://dwamdstream106.akamaized.net/hls/live/2017965/dwstream106/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/j68q1Bp/i24.png",i24 NEWS EN
https://bcovlive-a.akamaihd.net/ecf224f43f3b43e69471a7b626481af0/eu-central-1/5377161796001/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/NCQtNX5/telesur.png",TELESUR EN
https://cdnenmain.telesur.ultrabase.net/mblivev3/hd/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/pdnMrZn/a24.png",AFRICA 24 EN
https://livevideo.vedge.infomaniak.com/livecast/ik:africa24english/manifest.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/rtqXSWm/arirang.png",ARIRANG WORLD
http://amdlive-ch01.ctnd.com.edgesuite.net/arirang_1ch/smil:arirang_1ch.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/rtqXSWm/arirang.png",ARIRANG WORLD
https://amdlive-ch01-g-ctnd-com.akamaized.net/arirang_1gch/smil:arirang_1gch.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/rtqXSWm/arirang.png" user-agent="Star Wars",ARIRANG WORLD
https://amdlive-ch01-ctnd-com.akamaized.net/arirang_1ch/smil:arirang_1ch.smil/chunklist_b2256000_sleng.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/tQC0d8X/kbsw.jpg",KBS WORLD
https://kbsworld-ott.akamaized.net/hls/live/2002341/kbsworld/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/JCjsXZm/nhk.png",NHK WORLD
https://nhkwlive-ojp.nhkworld.jp/hls/live/2003459/nhkwlive-ojp-en/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/JCjsXZm/nhk.png",NHK WORLD
https://cdn.nhkworld.jp/www11/nhkworld-tv/domestic/2003459/live.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/JCjsXZm/nhk.png",NHK WORLD
https://cdn.nhkworld.jp/www11/nhkworld-tv/bmcc-live/fr/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/JCjsXZm/nhk.png",NHK WORLD
https://cdn.nhkworld.jp/www11/nhkworld-tv/pre/hlscomp.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/JCjsXZm/nhk.png",NHK WORLD
https://master.nhkworld.jp/nhkworld-tv/playlist/live.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/nP9xpck/trtw.png",TRT WORLD
https://tv-trtworld.medya.trt.com.tr/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/NrN5Gy2/tvpworld.png",TVP WORLD
https://raw.githubusercontent.com/ipstreet312/freeiptv/refs/heads/master/ressources/wld/tvpwd.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/MGW5Vv9/aljaz.png",AL JAZEERA NEWS 
https://live-hls-web-aje.getaj.net/AJE/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/MGW5Vv9/aljaz.png",AL JAZEERA NEWS 
https://live-hls-v3-aje.getaj.net/AJE-V3/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/MGW5Vv9/aljaz.png",AL JAZEERA NEWS 
https://live-hls-apps-aje-fa.getaj.net/AJE/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/MGW5Vv9/aljaz.png",AL JAZEERA NEWS
https://d1cy85syyhvqz5.cloudfront.net/v1/master/7b67fbda7ab859400a821e9aa0deda20ab7ca3d2/aljazeeraLive/AJE/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/MGW5Vv9/aljaz.png",AL JAZEERA NEWS
https://d35j504z0x2vu2.cloudfront.net/v1/master/0bc8e8376bd8417a1b6761138aa41c26c7309312/al-jazeera-english/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/s9gLmqv/cgtnch.png",CGTN NEWS
https://news.cgtn.com/resource/live/english/cgtn-news.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/s9gLmqv/cgtnch.png",CGTN NEWS
https://english-livetx.cgtn.com/hls/yypdyyctzb_hd.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/s9gLmqv/cgtnch.png",CGTN NEWS
https://amg00405-rakutentv-cgtn-rakuten-i9tar.amagi.tv/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/s9gLmqv/cgtnch.png",CGTN NEWS
https://english-livebkali.cgtn.com/live/encgtn.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/rwbrckj/pressir.png",PRESS TV [censure-ifany]
https://cdnlive.presstv.ir/cdnlive/smil:cdnlive.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/rwbrckj/pressir.png",PRESS TV [censure-ifany]
https://live.presstv.ir/hls/presstv.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/D7w9h7Q/rt.png",RT NEWS [censure-blocked]
https://rt-glb.rttv.com/live/rtnews/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/D7w9h7Q/rt.png",RT NEWS [censure-blocked]
https://rt-glb.rttv.com/dvr/rtnews/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/D7w9h7Q/rt.png",RT NEWS [censure-blocked]
http://69.64.57.208:8080/russiatoday/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/D7w9h7Q/rt.png",RT NEWS [censure-blocked]
https://rumble-foxo.cdn.rumble.cloud/live/hr6yv36f/slot-4/mxtm-wdfe_1080p/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/XbSHxd5/cnn.png",CNN INT (backup)
https://dqmhiwgbe98iq.cloudfront.net/v1/master/3722c60a815c199d9c0ef36c5b73da68a62b09d1/cc-1e8xhm2nv4xdw/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/XbSHxd5/cnn.png",CNN INT (backup)
https://d3508xo7u38fy2.cloudfront.net/v1/master/3722c60a815c199d9c0ef36c5b73da68a62b09d1/cc-j79jq28qz6knd/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/XbSHxd5/cnn.png",CNN INT (backup)
https://d3bp6dwmpbdajl.cloudfront.net/v1/master/3722c60a815c199d9c0ef36c5b73da68a62b09d1/cc-ury0meh5m4nzm/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/XbSHxd5/cnn.png",CNN INT (backup)
https://ds2c506obo7m8.cloudfront.net/v1/master/3722c60a815c199d9c0ef36c5b73da68a62b09d1/cc-7zjq3tdqasbg8/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/XbSHxd5/cnn.png",CNN FAST (backup)
https://du6zy613vobd4.cloudfront.net/v1/master/3722c60a815c199d9c0ef36c5b73da68a62b09d1/cc-g58rwi2g496ww/CNNFAST_GB.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/XbSHxd5/cnn.png",CNN FAST (backup)
https://d2sybdl23b9psq.cloudfront.net/v1/master/3722c60a815c199d9c0ef36c5b73da68a62b09d1/cc-bocx3i7bjz0dg/CNNFAST_GB.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/XbSHxd5/cnn.png",CNN FAST (backup)
https://d2dbclbbd0dwnj.cloudfront.net/v1/master/3722c60a815c199d9c0ef36c5b73da68a62b09d1/cc-vfen7v8uxmmt1/CNNFAST_GB.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/XbSHxd5/cnn.png",CNN FAST (backup)
https://d1k2s17sgkoemp.cloudfront.net/v1/master/3722c60a815c199d9c0ef36c5b73da68a62b09d1/cc-i4f8wxg6jeqii/CNNFAST_GB.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/XbSHxd5/cnn.png",CNN FAST (backup)
https://d3hnx79nr9mhdw.cloudfront.net/v1/master/3722c60a815c199d9c0ef36c5b73da68a62b09d1/cc-1u2levt4fksmr/CNNFAST_GB.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/XbSHxd5/cnn.png",CNN INT [downlink]
https://d30x5vsa85tvmd.cloudfront.net/v1/master/3722c60a815c199d9c0ef36c5b73da68a62b09d1/cc-7y561g9sa9uht/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/XbSHxd5/cnn.png",CNN INT [downlink]
https://dhzhj55w8hou6.cloudfront.net/v1/master/3722c60a815c199d9c0ef36c5b73da68a62b09d1/cc-bmoob4iijm59i/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/XbSHxd5/cnn.png",CNN INT [downlink]
https://d1mj4zol5huu6l.cloudfront.net/v1/master/3722c60a815c199d9c0ef36c5b73da68a62b09d1/cc-tp1e68v8mb0lb/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/XbSHxd5/cnn.png",CNN INT [downlink]
https://doq6y2m748j16.cloudfront.net/v1/master/3722c60a815c199d9c0ef36c5b73da68a62b09d1/CNN-prod/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/XbSHxd5/cnn.png",CNN INT [downlink]
https://cnn-cnninternational-1-gb.samsung.wurl.com/manifest/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/XbSHxd5/cnn.png",CNN INT [downlink]
https://cnn-cnninternational-1-eu.rakuten.wurl.tv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/XbSHxd5/cnn.png",CNN INT [downlink]
https://rakuten-cnninternational-1-gb.lg.wurl.tv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/XbSHxd5/cnn.png" user-agent="Star Wars",CNN FAST [geo-blocked]
https://cdn-uw2-prod.tsv2.amagi.tv/linear/amg00405-rakutentv-cnnfastlg-rakuten-lggb/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/8MBM4M1/skyn.png",SKY NEWS [deadlink]
https://linear021-gb-hls1-prd-ak.cdn.skycdp.com/Content/HLS_001_hd/Live/channel(skynews)/index_hd.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/8MBM4M1/skyn.png",SKY NEWS [deadlink]
http://linear116-gb-hls1-prd-ak.cdn.skycdp.com/Content/HLS_001_sd/Live/channel(skynewsinternational)/index_sd.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/8MBM4M1/skyn.png",SKY NEWS [deadlink]
https://d301yv2uyy17su.cloudfront.net/sky-news-live.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/8MBM4M1/skyn.png",SKY NEWS [deadlink]
https://d301yv2uyy17su.cloudfront.net/sky-news-international-live.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/8MBM4M1/skyn.png",SKY NEWS [deadlink]
https://siloh.pluto.tv/lilo/production/SkyNews/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/8MBM4M1/skyn.png",SKY NEWS [diedlink]
https://d2vv1kwm3dofeu.cloudfront.net/v1/master/3fec3e5cac39a52b2132f9c66c83dae043dc17d4/prod_default_xumo-ams-aws/master.m3u8?ads.xumo_channelId=99951223
#EXTINF:-1 tvg-logo="https://i.ibb.co/XWNXpVg/talk.png",TALK NEWS [geo-blocked]
https://samsunguk-newsuk-talkradiotv-samsunguk-ppg60.amagi.tv/playlist/samsunguk-newsuk-talkradiotv-samsunguk/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/CKTjvj8/nbc.jpg",NBC NEWS [downlink]
https://nbcnews2.akamaized.net/hls/live/723426/NBCNewsPlaymaker24x7Linear99a3a827-ua/master.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/Nn5x9Hq/bloom.jpg",BLOOMBERG EU [downlink]
https://bloomberg-bloomberg-1-eu.rakuten.wurl.tv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/R4xVMYc/enews.png",EURONEWS EN [downlink]
https://d1mpprlbe8tn2j.cloudfront.net/v1/master/7b67fbda7ab859400a821e9aa0deda20ab7ca3d2/euronewsLive/87O7AhxRUdeeIVqf/ewnsabren_eng.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/hdBrzcc/fox.png",FOX NEWS [diedlink]
https://cdn-ue1-prod.tsv2.amagi.tv/linear/samsungus-fox-newsnow-samsung/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/hdBrzcc/fox.png",FOX NEWS [diedlink]
https://fox-foxnewsnow-samsungus-tsv2-hm6vl.amagi.tv/playlist/samsungus-fox-newsnow-samsung/playlist.m3u8


#EXTINF:-1 tvg-logo="https://i.ibb.co/mywSdSQ/att.png" group-title="28. |📡|👨‍💻👉GITHUB.COM/IPSTREET312",|ℹ️|MORE-INFO➡️: ☛RECEPTIONIPTV.BLOGSPOT.COM
https://github.com/ipstreet312/freeiptv/raw/master/ressources/infos/barkers/linkupdatedinfo.ts
#EXTINF:-1 group-title="28. |📡|👨‍💻👉GITHUB.COM/IPSTREET312",--- |🎁⭐ ⬇↓ DELUXE PACKAGE👍 ↓⬇🤩❤️| --- 🎵💯
http://
#EXTINF:-1 tvg-logo="https://i.ibb.co/6t2ztJT/dlxmsc.png",DELUXE MUSIC English
https://sdn-global-live-streaming-packager-cache.3qsdn.com/13456/13456_264_live.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/jZWbT2g/dlxfbk.png",DELUXE MUSIC Flash Back
https://sdn-global-live-streaming-packager-cache.3qsdn.com/65185/65185_264_live.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/2ks2Ys7/dlxdnc.png",DELUXE MUSIC Dance
https://sdn-global-live-streaming-packager-cache.3qsdn.com/64733/64733_264_live.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/WBKwntS/dlxrap.png",DELUXE MUSIC Rap
https://sdn-global-live-streaming-packager-cache.3qsdn.com/65183/65183_264_live.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/mDFLYx3/dlxrck.png",DELUXE MUSIC Rock
https://sdn-global-live-streaming-packager-cache.3qsdn.com/65181/65181_264_live.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/TmL52ct/dlxde.png",DELUXE MUSIC Deutsch Schlager
https://sdn-global-live-streaming-packager-cache.3qsdn.com/26658/26658_264_live.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/6RvHVvn/dlxdtschpp.png",DELUXE MUSIC Deutsch Pop
https://d46c0ebf9ef94053848fdd7b1f2f6b90.mediatailor.eu-central-1.amazonaws.com/v1/master/81bfcafb76f9c947b24574657a9ce7fe14ad75c0/live-prod/95d6544c-4164-11ec-9c7c-2cf753b8a203/0/master.m3u8?uid=%7BPSID%7D&optout=%7BTARGETOPT%7D&country=DE&vendor=samsung
#EXTINF:-1 tvg-logo="https://i.ibb.co/1KhQxpd/dlxwnt.png",DELUXE MUSIC Winter Time
https://d2l1hs6hxlg3df.cloudfront.net/v1/master/3722c60a815c199d9c0ef36c5b73da68a62b09d1/cc-pb0nloqsgtwc2/index.m3u8
#EXTINF:-1 tvg-logo="https://i.ibb.co/RpfpWkr/dlxlng.png",DELUXE MUSIC Lounge
https://stream.ads.ottera.tv/playlist.m3u8?network_id=2664
#EXTINF:-1 tvg-logo="https://i.ibb.co/RpfpWkr/dlxlng.png",DELUXE MUSIC Lounge
https://stream.ads.ottera.tv/playlist.m3u8?network_id=2489
#EXTINF:-1 tvg-logo="https://i.ibb.co/pKt53kX/dl1.png",DELUXE MUSIC Lounge Extra
https://d46c0ebf9ef94053848fdd7b1f2f6b90.mediatailor.eu-central-1.amazonaws.com/v1/master/81bfcafb76f9c947b24574657a9ce7fe14ad75c0/live-prod/8ef13d2a-80c1-11eb-908d-533d39655269/0/master.m3u8?uid=%7BPSID%7D&optout=%7BTARGETOPT%7D&country=FR&vendor=samsung
#EXTINF:-1 tvg-logo="https://i.ibb.co/pKt53kX/dl1.png",DELUXE MUSIC Lounge Extra
https://d46c0ebf9ef94053848fdd7b1f2f6b90.mediatailor.eu-central-1.amazonaws.com/v1/master/81bfcafb76f9c947b24574657a9ce7fe14ad75c0/live-prod/ec8e5c43-6fae-11eb-908d-533d39655269/0/master.m3u8?uid=%7BPSID%7D&optout=%7BTARGETOPT%7D&country=DE&vendor=samsung
#EXTINF:-1,📻🎶📺🎥Video Player Checker
http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4


"""

# 正则匹配频道名称和播放链接
pattern = re.compile(r'#EXTINF:-1 .*?,(.+?)\n(.+?)')

# 创建新的 M3U 文件
new_m3u = ["#EXTM3U"]

# 解析新 m3u 内容并构建新的 M3U 文件
for match in re.finditer(pattern, new_m3u_content):
    channel_name = match.group(1).strip()
    stream_url = match.group(2).strip()

    # 从 STATIC_TV_NAMES 获取标准化的频道名称
    standardized_name = STATIC_TV_NAMES.get(channel_name, channel_name)

    # 尝试从字典获取 logo 和类别，如果没有匹配到，则保留原值
    logo = STATIC_LOGOS.get(channel_name, "")
    category = STATIC_CATEGORIES.get(channel_name, "Unknown Category")
    
    # 如果没有 logo 信息，使用原始的 logo 值（如果有的话）
    if logo == "":
        logo = match.group(0).split('tvg-logo="')[1].split('"')[0]

    # 添加到新的 M3U 内容中
    new_m3u.append(f'#EXTINF:-1 group-title="{category}" tvg-logo="{logo}", {standardized_name}')
    new_m3u.append(stream_url)

# 输出新的 M3U 文件内容
with open("new_playlist.m3u", "w", encoding="utf-8") as f:
    f.write("\n".join(new_m3u))

# 打印输出新的 M3U 文件内容
with open("new_playlist.m3u", "r", encoding="utf-8") as f:
    print(f.read())
