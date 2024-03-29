# A Python dictionary object that maps all cogenital heart defect terms to their respective entry terms. 
# For example, 'DiGeorge Syndrome' is also known as '22q11.2 Deletion Syndrome', 'Conotruncal Anomaly Face Syndrome', etc.
# This is the result of the last step from the file 'extracting_data'.

d = {'DiGeorge Syndrome': ['DiGeorge Syndrome',
  'Velocardiofacial Syndrome',
  '22q11.2 Deletion Syndrome',
  '22q11.2DS',
  'Autosomal Dominant Opitz G-Bbb Syndrome',
  'Catch22',
  'Conotruncal Anomaly Face Syndrome',
  'Conotruncal Anomaly Face Syndrome (CTAF)',
  'Deletion 22q11.2 Syndrome',
  'DiGeorge Anomaly',
  'DiGeorge Sequence',
  'Familial Third and Fourth Pharyngeal Pouch Syndrome',
  'Hypoplasia of Thymus and Parathyroids',
  'Pharyngeal Pouch Syndrome',
  'Sedlackova Syndrome',
  'Shprintzen Syndrome',
  'Shprintzen VCF Syndrome',
  'Third and Fourth Pharyngeal Pouch Syndrome',
  'Thymic Aplasia Syndrome',
  'VCF Syndrome',
  'Velo-Cardio-Facial Syndrome',
  'Autosomal Dominant Opitz G Bbb Syndrome',
  'Deletion Syndrome, 22q11.2',
  'Syndrome, DiGeorge',
  'Syndrome, Sedlackova',
  'Syndrome, Shprintzen',
  'Syndrome, VCF',
  'Syndrome, Velo-Cardio-Facial',
  'Syndrome, Velocardiofacial',
  'Velo Cardio Facial Syndrome',
  '22q11.2 Deletion'],
 'Aortic Coarctation': ['Aortic Coarctation',
  'Coarctation of Aorta',
  'Coarctation of Aorta Dominant',
  'Coarctation of the Aorta',
  'Aorta Coarctation',
  'Aorta Coarctations',
  'Aorta Dominant Coarctation',
  'Aorta Dominant Coarctations',
  'Aortic Coarctations',
  'Coarctation, Aortic',
  'Coarctations, Aortic'],
 'Arrhythmogenic Right Ventricular Dysplasia': ['Arrhythmogenic Right Ventricular Dysplasia',
  'Arrhythmogenic Right Ventricular Cardiomyopathy',
  'Right Ventricular Dysplasia, Arrhythmogenic',
  'Ventricular Dysplasia, Right, Arrhythmogenic',
  'ARVD-C',
  'Arrhythmogenic Right Ventricular Cardiomyopathy-Dysplasia',
  'Arrhythmogenic Right Ventricular Dysplasia-Cardiomyopathy',
  'Arrhythmogenic Right Ventricular Cardiomyopathy Dysplasia'],
 'Barth Syndrome': ['Barth Syndrome',
  '3-Methylglutaconic Aciduria, Type II',
  '3-Methylglutaconicaciduria Type 2',
  '3-Methylglutaconicaciduria Type II',
  'Cardioskeletal Myopathy with Neutropenia and Abnormal Mitochondria',
  'MGA Type 2',
  'MGA Type II',
  '3 Methylglutaconic Aciduria, Type II',
  '3 Methylglutaconicaciduria Type 2',
  '3-Methylglutaconicaciduria Type 2s',
  '3-Methylglutaconicaciduria Type IIs',
  'MGA Type 2s',
  'MGA Type IIs',
  'Syndrome, Barth',
  'Type 2, 3-Methylglutaconicaciduria',
  'Type 2, MGA',
  'Type 2s, MGA',
  'Type II, MGA',
  'Type IIs, MGA'],
 'Cor Triatriatum': ['Cor Triatriatum',
  'Triatrial Heart',
  'Cor Triatriatum Sinistrum',
  'Subdivided Left Atrium',
  'Atrium, Subdivided Left',
  'Atriums, Subdivided Left',
  'Heart, Triatrial',
  'Hearts, Triatrial',
  'Left Atrium, Subdivided',
  'Left Atriums, Subdivided',
  'Subdivided Left Atriums',
  'Triatrial Hearts'],
 'Anomalous Left Coronary Artery': ['Anomalous Left Coronary Artery'],
 'Bland White Garland Syndrome': ['Bland White Garland Syndrome',
  'ALCAPA',
  'ALCAPA Syndrome',
  'Bland-White-Garland Syndrome',
  'ALCAPA Syndromes',
  'Syndrome, ALCAPA',
  'Syndrome, Bland-White-Garland'],
 'Crisscross Heart': ['Crisscross Heart',
  'Criss-cross Heart',
  'Criss cross Heart',
  'Criss-cross Hearts',
  'Crisscross Hearts',
  'Heart, Criss-cross',
  'Heart, Crisscross',
  'Hearts, Criss-cross',
  'Hearts, Crisscross'],
 'Myocardial Bridging': ['Myocardial Bridging',
  'Bridging, Myocardial',
  'Bridgings, Myocardial',
  'Myocardial Bridgings'],
 'Kartagener Syndrome': ['Kartagener Syndrome',
  'Kartagener Triad',
  'Ciliary Dyskinesia, Primary, 1',
  'Ciliary Dyskinesia, Primary, 1, With Or Without Situs Inversus',
  'Dextrocardia, Bronchiectasis, and Sinusitis',
  "Kartagener's Syndrome",
  "Kartagener's Triad",
  'Polynesian Bronchiectasis',
  'Siewert Syndrome',
  'Bronchiectasis, Polynesian',
  'Kartageners Syndrome',
  'Kartageners Triad',
  'Polynesian Bronchiectases',
  'Syndrome, Kartagener',
  "Syndrome, Kartagener's",
  'Syndrome, Siewert'],
 'Ductus Arteriosus, Patent': ['Ductus Arteriosus, Patent',
  'Patent Ductus Arteriosus Familial',
  'Patency of the Ductus Arteriosus',
  'Patent Ductus Arteriosus'],
 'Eisenmenger Complex': ['Eisenmenger Complex',
  'Eisenmenger Syndrome',
  "Eisenmenger's Complex",
  "Eisenmenger's Syndrome",
  'Complex, Eisenmenger',
  "Complex, Eisenmenger's",
  'Eisenmengers Complex',
  'Eisenmengers Syndrome',
  'Syndrome, Eisenmenger',
  "Syndrome, Eisenmenger's"],
 'Truncus Arteriosus, Persistent': ['Truncus Arteriosus, Persistent',
  'Persistent Truncus Arteriosus'],
 'Endocardial Cushion Defects': ['Endocardial Cushion Defects',
  'Persistent Common Atrioventricular Canal',
  'Endocardial Cushion Defect',
  'Cushion Defect, Endocardial',
  'Cushion Defects, Endocardial',
  'Defect, Endocardial Cushion',
  'Defects, Endocardial Cushion'],
 'Foramen Ovale, Patent': ['Foramen Ovale, Patent',
  'Patent Foramen Ovale',
  'Patent Oval Foramen',
  'Oval Foramen, Patent'],
 'Lutembacher Syndrome': ['Lutembacher Syndrome',
  "Lutembacher's Syndrome",
  'Lutembachers Syndrome',
  'Syndrome, Lutembacher',
  "Syndrome, Lutembacher's"],
 'Heart Septal Defects, Ventricular': ['Heart Septal Defects, Ventricular',
  'Ventricular Septal Defects',
  'Intraventricular Septal Defects',
  'Ventricular Septal Defect',
  'Defect, Intraventricular Septal',
  'Defect, Ventricular Septal',
  'Defects, Intraventricular Septal',
  'Intraventricular Septal Defect',
  'Septal Defect, Intraventricular',
  'Septal Defect, Ventricular',
  'Septal Defects, Intraventricular',
  'Septal Defects, Ventricular'],
 'Heterotaxy Syndrome': ['Heterotaxy Syndrome',
  'Asplenia Syndrome',
  'Asplenia with Cardiovascular Anomalies',
  'Ivemark Syndrome',
  'Left Atrial Isomerism',
  'Left Atrial Isomerism with Polysplenia',
  'Polysplenia Syndrome',
  'Right Atrial Isomerism',
  'Right Atrial Isomerism with Asplenia',
  'Situs Ambiguus',
  'Situs Ambiguus Viscerum',
  'Situs Ambiguus with Asplenia',
  'Situs Ambiguus with Polysplenia',
  'Visceral Heterotaxy',
  'Ambiguus Viscerum, Situs',
  'Ambiguus Viscerums, Situs',
  'Ambiguus, Situs',
  'Asplenia Syndromes',
  'Atrial Isomerism, Left',
  'Atrial Isomerism, Right',
  'Atrial Isomerisms, Left',
  'Atrial Isomerisms, Right',
  'Heterotaxies, Visceral',
  'Heterotaxy Syndromes',
  'Heterotaxy, Visceral',
  'Isomerism, Left Atrial',
  'Isomerism, Right Atrial',
  'Isomerisms, Left Atrial',
  'Isomerisms, Right Atrial',
  'Left Atrial Isomerisms',
  'Polysplenia Syndromes',
  'Right Atrial Isomerisms',
  'Situs Ambiguus Viscerums',
  'Syndrome, Asplenia',
  'Syndrome, Heterotaxy',
  'Syndrome, Ivemark',
  'Syndrome, Polysplenia',
  'Syndromes, Asplenia',
  'Syndromes, Heterotaxy',
  'Syndromes, Polysplenia',
  'Visceral Heterotaxies',
  'Viscerum, Situs Ambiguus',
  'Viscerums, Situs Ambiguus'],
 'Hypoplastic Left Heart Syndrome': ['Hypoplastic Left Heart Syndrome',
  'Left Heart Syndrome, Hypoplastic',
  'Left Heart Hypoplasia Syndrome'],
 'Isolated Noncompaction of the Ventricular Myocardium': ['Isolated Noncompaction of the Ventricular Myocardium',
  'Isolated Non-compaction of the Ventricular Myocardium',
  'Isolated Noncompaction of the Left Ventricular Myocardium, X-Linked',
  'Noncompaction of the Left Ventricular Myocardium, Autosomal Dominant'],
 'LEOPARD Syndrome': ['LEOPARD Syndrome',
  'Cardio-Cutaneous Syndrome',
  'Cardiomyopathic Lentiginosis',
  'LEOPARD Syndrome, 1',
  'Lentiginosis Cardiomyopathic',
  'Leopard Syndrome 1',
  'Multiple Lentigines Syndrome',
  'Noonan Syndrome with Multiple Lentigines',
  'Progressive Cardiomyopathic Lentiginosis',
  'Cardio Cutaneous Syndrome',
  'Cardio-Cutaneous Syndromes',
  'Cardiomyopathic Lentiginoses',
  'Cardiomyopathic Lentiginoses, Progressive',
  'Cardiomyopathic Lentiginosis, Progressive',
  'Cardiomyopathic, Lentiginosis',
  'Cardiomyopathics, Lentiginosis',
  'LEOPARD Syndromes',
  'Lentigines Syndrome, Multiple',
  'Lentigines Syndromes, Multiple',
  'Lentiginoses, Cardiomyopathic',
  'Lentiginoses, Progressive Cardiomyopathic',
  'Lentiginosis Cardiomyopathics',
  'Lentiginosis, Cardiomyopathic',
  'Lentiginosis, Progressive Cardiomyopathic',
  'Multiple Lentigines Syndromes',
  'Progressive Cardiomyopathic Lentiginoses',
  'Syndrome, Cardio-Cutaneous',
  'Syndrome, LEOPARD',
  'Syndrome, Multiple Lentigines',
  'Syndromes, Cardio-Cutaneous',
  'Syndromes, LEOPARD',
  'Syndromes, Multiple Lentigines'],
 'Levocardia': ['Levocardia',
  'Isolated Levocardia',
  'Situs Inversus with Levocardia',
  'Levocardia, Isolated'],
 'Marfan Syndrome': ['Marfan Syndrome',
  'Marfan Syndrome, Type I',
  "Marfan's Syndrome",
  'Marfans Syndrome'],
 'Noonan Syndrome': ['Noonan Syndrome',
  'Male Turner Syndrome',
  'Turner Syndrome, Male',
  'Familial Turner Syndrome',
  'Female Pseudo-Turner Syndrome',
  'Noonan Syndrome 1',
  'Noonan-Ehmke Syndrome',
  'Pseudo-Ullrich-Turner Syndrome',
  'Turner Phenotype with Normal Karyotype',
  "Turner's Phenotype, Karyotype Normal",
  "Turner's Syndrome, Male",
  'Turner-Like Syndrome',
  'Ullrich-Noonan Syndrome',
  'Female Pseudo Turner Syndrome',
  "Male Turner's Syndrome",
  'Noonan Ehmke Syndrome',
  'Pseudo Ullrich Turner Syndrome',
  'Pseudo-Turner Syndrome, Female',
  'Turner Like Syndrome',
  'Turner Syndrome, Familial',
  'Ullrich Noonan Syndrome'],
 'Tetralogy of Fallot': ['Tetralogy of Fallot',
  "Fallot's Tetralogy",
  "Tetralogy, Fallot's",
  'Fallot Tetralogy',
  'Fallots Tetralogy',
  'Tetralogy, Fallot',
  'Tetralogy, Fallots'],
 'Congenitally Corrected Transposition of the Great Arteries': ['Congenitally Corrected Transposition of the Great Arteries',
  'Congenitally Corrected Transposition',
  'Congenitally Corrected Transposition of the Great Vessels',
  'Congenitally Corrected Transpositions',
  'Corrected Transposition, Congenitally',
  'Transposition, Congenitally Corrected'],
 'Double Outlet Right Ventricle': ['Double Outlet Right Ventricle',
  'Taussig-Bing Anomaly',
  'Double Outlet Right Ventricle, Noncommitted VSD',
  'Double Outlet Right Ventricle, Subaortic VSD',
  'Double Outlet Right Ventricle, Subpulmonary VSD',
  'Double-Outlet Right Ventricle',
  'Anomaly, Taussig-Bing',
  'Taussig Bing Anomaly'],
 'Tricuspid Atresia': ['Tricuspid Atresia',
  'Atresia, Tricuspid',
  'Tricuspid Valve Atresia',
  'Absent Right Atrioventricular Connection',
  'Atresia, Tricuspid Valve',
  'Atresias, Tricuspid',
  'Atresias, Tricuspid Valve',
  'Tricuspid Atresias',
  'Tricuspid Valve Atresias',
  'Valve Atresia, Tricuspid',
  'Valve Atresias, Tricuspid'],
 'Trilogy of Fallot': ['Trilogy of Fallot',
  "Fallot's Trilogy",
  'Fallot Trilogy',
  'Fallots Trilogy',
  "Trilogy, Fallot's"],
 'Trisomy 13 Syndrome': ['Trisomy 13 Syndrome',
  'Bartholin-Patau Syndrome',
  'Chromosome 13 Duplication',
  'Chromosome 13 Trisomy Syndrome',
  'Complete Trisomy 13 Syndrome',
  'Mosaic Trisomy 13 Syndrome',
  'Patau Syndrome',
  "Patau's Syndrome",
  'Trisomy 13',
  'Trisomy 13 Syndromes',
  'Bartholin Patau Syndrome',
  'Chromosome 13 Duplications',
  'Duplication, Chromosome 13',
  'Pataus Syndrome'],
 'Trisomy 18 Syndrome': ['Trisomy 18 Syndrome',
  'Complete Trisomy 18 Syndrome',
  'Edwards Syndrome',
  'Mosaic Trisomy 18 Syndrome',
  'Trisomy 18',
  'Trisomy E Syndrome',
  'Trisomy 18 Syndromes'],
 'Turner Syndrome': ['Turner Syndrome',
  'Bonnevie-Ullrich Syndrome',
  'Gonadal Dysgenesis, 45,X',
  'Gonadal Dysgenesis, XO',
  'Monosomy X',
  'Status Bonnevie-Ullrich',
  "Turner's Syndrome",
  'Ullrich-Turner Syndrome',
  'Bonnevie Ullrich Syndrome',
  'Status Bonnevie Ullrich',
  'Syndrome, Ullrich-Turner',
  'Turners Syndrome',
  'Ullrich Turner Syndrome',
  'XO Gonadal Dysgenesis'],
 'Univentricular Heart': ['Univentricular Heart',
  'Complex Single Ventricle',
  'Complex Single Ventricles',
  'Univentricular Hearts',
  'Ventricle, Complex Single'],
 'Alagille Syndrome': ['Alagille Syndrome',
  'Arteriohepatic Dysplasia',
  'Dysplasia, Arteriohepatic',
  'Alagille Syndrome 1',
  'Alagille Syndrome 2',
  'Alagille Watson Syndrome',
  "Alagille's Syndrome",
  'Alagille-Watson Syndrome',
  'Arteriohepatic Dysplasia (AHD)',
  'Cardiovertebral Syndrome',
  'Cholestasis with Peripheral Pulmonary Stenosis',
  'Hepatic Ductular Hypoplasia',
  'Hepatic Ductular Hypoplasia, Syndromatic',
  'Hepatofacioneurocardiovertebral Syndrome',
  'Paucity of Interlobular Bile Ducts',
  'Watson Alagille Syndrome',
  'Watson Miller Syndrome',
  'Watson-Miller syndrome',
  'Alagilles Syndrome',
  'Ductular Hypoplasia, Hepatic',
  'Dysplasia, Arteriohepatic (AHD)',
  'Hypoplasia, Hepatic Ductular',
  'Syndrome, Alagille',
  'Syndrome, Alagille Watson',
  "Syndrome, Alagille's",
  'Syndrome, Alagille-Watson',
  'Syndrome, Cardiovertebral',
  'Syndrome, Hepatofacioneurocardiovertebral',
  'Syndrome, Watson Alagille',
  'Syndrome, Watson Miller',
  'syndrome, Watson-Miller'],
 'Wolff-Parkinson-White Syndrome': ['Wolff-Parkinson-White Syndrome',
  'WPW Syndrome',
  'Anomalous Ventricular Excitation Syndrome',
  'Auriculoventricular Accessory Pathway Syndrome',
  'False Bundle-Branch Block Syndrome',
  'Ventricular Pre-Excitation with Arrhythmia',
  'Wolf-Parkinson-White Syndrome',
  'Syndrome, WPW',
  'Syndrome, Wolf-Parkinson-White',
  'Syndrome, Wolff-Parkinson-White',
  'Wolf Parkinson White Syndrome',
  'Wolff Parkinson White Syndrome'],
 'Ectopia Cordis': ['Ectopia Cordis', 'Cordis, Ectopia'],
 'Andersen Syndrome': ['Andersen Syndrome',
  'Andersen Cardiodysrhythmic Periodic Paralysis',
  'Andersen Cardiodysrythmic Periodic Paralysis',
  'Andersen Tawil Syndrome',
  'Andersen-Tawil Syndrome',
  'Long QT Syndrome 7',
  'Periodic Paralysis, Potassium-Sensitive Cardiodysrhythmic Type',
  'Potassium-Sensitive Periodic Paralysis, Ventricular Ectopy, and Dysmorphic Features',
  'Periodic Paralysis, Potassium Sensitive Cardiodysrhythmic Type',
  'Syndrome, Andersen',
  'Syndrome, Andersen Tawil'],
 'Jervell-Lange Nielsen Syndrome': ['Jervell-Lange Nielsen Syndrome',
  'Cardio-Auditory-Syncope Syndrome',
  'Cardioauditory Syndrome of Jervell and Lange-Nielsen',
  'Deafness, Congenital, and Functional Heart Disease',
  'Jervell And Lange-Nielsen Syndrome 1',
  'Jervell and Lange-Nielsen Syndrome',
  'Prolonged QT Interval in EKG and Sudden Death',
  'Surdo-Cardiac Syndrome',
  'Cardio Auditory Syncope Syndrome',
  'Cardio-Auditory-Syncope Syndromes',
  'Cardioauditory Syndrome of Jervell and Lange Nielsen',
  'Jervell And Lange Nielsen Syndrome 1',
  'Jervell Lange Nielsen Syndrome',
  'Jervell and Lange Nielsen Syndrome',
  'Surdo Cardiac Syndrome',
  'Surdo-Cardiac Syndromes',
  'Syndrome, Cardio-Auditory-Syncope',
  'Syndrome, Jervell-Lange Nielsen',
  'Syndrome, Surdo-Cardiac',
  'Syndromes, Cardio-Auditory-Syncope'],
 'Romano-Ward Syndrome': ['Romano-Ward Syndrome',
  'Long QT Syndrome 1',
  'Ward-Romano Syndrome',
  'Long QT Syndrome Type 1',
  'Ventricular Fibrillation with Prolonged QT Interval',
  'Romano Ward Syndrome',
  'Syndrome, Romano-Ward',
  'Syndrome, Ward-Romano',
  'Ward Romano Syndrome']}
