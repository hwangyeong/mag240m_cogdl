
feats = [
    ('x_rgat_1024', 1024, 128), # 0
    ('x_base', 768, 128), # 1
    ('x_pcbpcp_rw_lratio', 153, 32), # 2
    ('x_pcbpcp_rw_top10_lratio', 153, 32), # 3
    ('x_pcp_rw_lratio', 153, 32), # 4
    ('x_pcpcbp_rw_lratio', 153, 32), # 5
    ('x_pcpcbp_rw_top10_lratio', 153, 32), # 6
    ('x_pcpcp_rw_lratio', 153, 32), # 7
    ('x_pcpcp_rw_top10_lratio', 153, 32), # 8
    ('x_pwbawp_rw_lratio', 153, 32), # 9
    ('x_pwbawp_rw_top10_lratio', 153, 32), # 10
    ('x_pwbawp_ns_l_lratio', 153, 32), # 11
    ('x_pwbawp_ns_c2_lratio', 153, 32), # 12
    ('x_pwbawp_ns_c4_lratio', 153, 32), # 13

    ('x_jax_153', 153, 32), # 14
    ('x_m2v_64', 64, 128), # 15

    ('x_pcbpcbp_ns_fmean', 768, 32), # 16
    ('x_pcbpcp_ns_fmean', 768, 32), # 17
    ('x_pcbp_ns_fmean', 768, 32), # 18
    ('x_pcpcbp_ns_fmean', 768, 32), # 19
    ('x_pcpcp_ns_fmean', 768, 32), # 20
    ('x_pcp_ns_fmean', 768, 32), # 21
    ('x_pwbawp_ns_fmean', 768, 32), # 22
    ('x_pcbpwba_ns_fmean', 768, 32), # 23
    ('x_pcpwba_ns_fmean', 768, 32), # 24
    ('x_pwbaawi_ns_fmean', 768, 32), # 25
    ('x_pwba_ns_fmean', 768, 32), # 26

    ('3layer_x_rgat_1024', 1024, 128), # 27
    ('x_pca_129', 129, 64) # 28
]

model_feats = [
    {"rgat1024_label":[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]},
    {"rgat1024_label_m2v_feat_fhid_seed0": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]},
    {"rgat1024_label_m2v_feat_fhid_seed1": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]},
    {"rgat1024_label_m2v_feat_fhid_seed2": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]},
    {"rgat1024_label_m2v_feat_fhid_seed3": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]},
    {"rgat1024_label_m2v_feat_fhid_seed4": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]},
    {"rgat1024_label_m2v_feat_fhid_seed5": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]},

    {"rgat1024_label_m2v_feat_3rgat1024": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, (16, 128), (17, 128), (18, 128), (19, 128), (20, 128), (21, 128), (22, 128), (23, 128), (24, 128), (25, 128), (26, 128), 27]},
    {"rgat1024_label_m2v_feat_3rgat1024_fhid_seed0": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]},
    {"rgat1024_label_m2v_feat_3rgat1024_fhid_seed1": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]},
    {"rgat1024_label_m2v_feat_3rgat1024_fhid_seed2": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]},

    {"rgat1024_label_m2v_feat_fhid_hid1024": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]},
    {"label_m2v_3rgat1024": [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 27]},
    {"rgat1024_label_m2v_feat_3rgat1024_jax_fhid": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]},
]
