-- Insérer des données dans la table sirh_annonce
INSERT INTO sirh_annonce (recruitment_id, description_id, approche, contenu, descriptif_societe, profil_recherche, modalite_reponse, obligations, create_uid, create_date, write_uid, write_date)
VALUES 
(1, 1, 'Approche 1', 'Contenu 1', 'Descriptif société 1', 'Profil recherche 1', 'Modalité réponse 1', 'Obligations 1', 1, NOW(), 1, NOW()),
(2, 2, 'Approche 2', 'Contenu 2', 'Descriptif société 2', 'Profil recherche 2', 'Modalité réponse 2', 'Obligations 2', 1, NOW(), 1, NOW()),
(3, 3, 'Approche 3', 'Contenu 3', 'Descriptif société 3', 'Profil recherche 3', 'Modalité réponse 3', 'Obligations 3', 1, NOW(), 1, NOW());

-- Insérer des données dans la table sirh_desc
INSERT INTO sirh_desc (recruitment_id, intitule, descr, niveau, diplome, formation, formation_experience, savoir_faire, savoir_etre, type, horaires, remuneration, create_uid, create_date, write_uid, write_date)
VALUES 
(1, 1, 'Description 1', 'Niveau 1', 'Diplôme 1', 'Formation 1', 'Expérience de formation 1', 'Savoir-faire 1', 'Savoir-être 1', 'Type 1', 40, 3000.00, 1, NOW(), 1, NOW()),
(2, 2, 'Description 2', 'Niveau 2', 'Diplôme 2', 'Formation 2', 'Expérience de formation 2', 'Savoir-faire 2', 'Savoir-être 2', 'Type 2', 35, 3500.00, 1, NOW(), 1, NOW()),
(3, 3, 'Description 3', 'Niveau 3', 'Diplôme 3', 'Formation 3', 'Expérience de formation 3', 'Savoir-faire 3', 'Savoir-être 3', 'Type 3', 30, 4000.00, 1, NOW(), 1, NOW());

-- Insérer des données dans la table sirh_form
INSERT INTO sirh_form (description_id, motif, pourex, intitule, budget, echeanceContrat, xp, lieu, Deplacement, autre, annonce_id, dateEntree, create_uid, create_date, write_uid, write_date)
VALUES 
(1, 'Motif 1', 1, 1, 5000.00, '2024-04-01', 2, 'Lieu 1', 'Deplacement 1', 'Autre 1', 1, '2024-04-15', 1, NOW(), 1, NOW()),
(2, 'Motif 2', 2, 2, 6000.00, '2024-04-02', 3, 'Lieu 2', 'Deplacement 2', 'Autre 2', 2, '2024-04-16', 1, NOW(), 1, NOW()),
(3, 'Motif 3', 3, 3, 7000.00, '2024-04-03', 4, 'Lieu 3', 'Deplacement 3', 'Autre 3', 3, '2024-04-17', 1, NOW(), 1, NOW());

