SECTORS = [
    {"id":"immobilier-btp","name":"Immobilier & BTP","description":"Suivi du marché immobilier, construction, infrastructures urbaines et logement.","priority":1,"trend":"stable","growth_rate":2.4,"investment_score":74,"risk_score":48,"data_freshness_hours":8},
    {"id":"energie-renouvelables","name":"Énergie & Énergies Renouvelables","description":"Analyse de la transition énergétique, production et investissements verts.","priority":2,"trend":"positive","growth_rate":5.8,"investment_score":86,"risk_score":36,"data_freshness_hours":6},
    {"id":"finance-marches","name":"Finance & Marchés de Capitaux","description":"Veille sur les marchés, taux, liquidité, banques et instruments financiers.","priority":3,"trend":"stable","growth_rate":3.1,"investment_score":79,"risk_score":42,"data_freshness_hours":4},
    {"id":"agroalimentaire","name":"Agroalimentaire & Agriculture","description":"Production agricole, sécurité alimentaire, export et transformation.","priority":4,"trend":"negative","growth_rate":1.2,"investment_score":67,"risk_score":61,"data_freshness_hours":12},
    {"id":"tourisme-hotellerie","name":"Tourisme & Hôtellerie","description":"Arrivées touristiques, nuitées, capacité hôtelière et investissements.","priority":5,"trend":"positive","growth_rate":6.3,"investment_score":82,"risk_score":39,"data_freshness_hours":10},
    {"id":"telecom-digital","name":"Télécommunications & Digital","description":"Connectivité, cloud, digitalisation, cybersécurité et services numériques.","priority":6,"trend":"positive","growth_rate":7.1,"investment_score":88,"risk_score":33,"data_freshness_hours":5},
    {"id":"infrastructure-logistique","name":"Infrastructure & Logistique","description":"Ports, zones logistiques, transport, supply chain et corridors commerciaux.","priority":7,"trend":"stable","growth_rate":3.7,"investment_score":77,"risk_score":45,"data_freshness_hours":9},
    {"id":"industrie-manufacturiere","name":"Industrie Manufacturière","description":"Automobile, aéronautique, textile, chimie et montée en gamme industrielle.","priority":8,"trend":"positive","growth_rate":4.4,"investment_score":81,"risk_score":41,"data_freshness_hours":7},
]

DOCUMENTS = [
    {"id":"doc-001","sector_id":"energie-renouvelables","title":"Note transition énergétique Maroc","source":"Ministère / Open data","year":2026,"tags":["énergie","renouvelable","investissement"],"summary":"Capacité renouvelable en croissance, pression positive sur les investissements verts."},
    {"id":"doc-002","sector_id":"finance-marches","title":"Synthèse marchés de capitaux","source":"AMMC / BVC","year":2026,"tags":["marchés","liquidité","taux"],"summary":"Marché prudent, attention aux conditions de liquidité et aux anticipations de taux."},
    {"id":"doc-003","sector_id":"tourisme-hotellerie","title":"Baromètre tourisme","source":"Ministère du Tourisme","year":2026,"tags":["tourisme","hôtellerie","arrivées"],"summary":"Reprise soutenue des flux touristiques et hausse des nuitées dans les pôles majeurs."},
]

BENCHMARKS = {
    "energie-renouvelables": [
        {"label":"Croissance annuelle","morocco":5.8,"international_avg":4.2,"best_in_class":8.5,"unit":"%"},
        {"label":"Score attractivité","morocco":86,"international_avg":72,"best_in_class":94,"unit":"/100"},
        {"label":"Risque sectoriel","morocco":36,"international_avg":44,"best_in_class":29,"unit":"/100"},
    ],
    "finance-marches": [
        {"label":"Croissance annuelle","morocco":3.1,"international_avg":2.7,"best_in_class":5.2,"unit":"%"},
        {"label":"Score attractivité","morocco":79,"international_avg":75,"best_in_class":91,"unit":"/100"},
        {"label":"Risque sectoriel","morocco":42,"international_avg":46,"best_in_class":31,"unit":"/100"},
    ],
    "default": [
        {"label":"Croissance annuelle","morocco":4.0,"international_avg":3.3,"best_in_class":7.0,"unit":"%"},
        {"label":"Score attractivité","morocco":76,"international_avg":70,"best_in_class":90,"unit":"/100"},
        {"label":"Risque sectoriel","morocco":45,"international_avg":50,"best_in_class":32,"unit":"/100"},
    ]
}
