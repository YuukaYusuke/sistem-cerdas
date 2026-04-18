import streamlit as st


st.set_page_config(
    page_title="Workforce Recommendation System",
    layout="wide",
    initial_sidebar_state="collapsed",
)


def inject_styles():
    st.markdown(
        """
        <style>
        :root {
            --ink: #1d2935;
            --muted: #667085;
            --line: #dfe6ee;
            --surface: #ffffff;
            --page: #f5f7fa;
            --accent: #087f8c;
            --accent-deep: #066771;
            --accent-soft: #e6f4f5;
            --success: #2e8b57;
            --warning: #c58b1b;
            --risk: #c2574b;
            --shadow: 0 14px 30px rgba(29, 41, 53, 0.07);
        }

        .stApp {
            background: var(--page);
            color: var(--ink);
        }

        .block-container {
            max-width: 1120px;
            padding-top: 2rem;
            padding-bottom: 3rem;
        }

        [data-testid="stHeader"] {
            background: transparent;
        }

        .page-header {
            margin-bottom: 1.4rem;
            padding-bottom: 1rem;
            border-bottom: 1px solid var(--line);
        }

        .eyebrow {
            color: var(--accent-deep);
            font-size: 0.78rem;
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: 0;
            margin-bottom: 0.45rem;
        }

        .page-header h1 {
            margin: 0 0 0.4rem 0;
            color: var(--ink);
            font-size: 2.15rem;
            line-height: 1.15;
            letter-spacing: 0;
        }

        .page-header p {
            max-width: 790px;
            margin: 0;
            color: var(--muted);
            line-height: 1.6;
            font-size: 1rem;
        }

        .section-title {
            margin: 0.25rem 0 0.75rem 0;
            font-size: 1rem;
            font-weight: 800;
            color: var(--ink);
        }

        .result-card,
        .readiness,
        .decision-summary,
        .step-card,
        div[data-testid="stMetric"] {
            background: var(--surface);
            border: 1px solid var(--line);
            border-radius: 8px;
            box-shadow: var(--shadow);
        }

        .result-card {
            border-left: 6px solid var(--accent);
            padding: 1.35rem;
            margin-bottom: 1rem;
        }

        .badge {
            display: inline-block;
            padding: 0.32rem 0.58rem;
            border-radius: 8px;
            background: var(--accent-soft);
            color: var(--accent-deep);
            font-size: 0.78rem;
            font-weight: 800;
            text-transform: uppercase;
        }

        .result-card h2 {
            margin: 0.75rem 0 0.5rem 0;
            font-size: 1.85rem;
            line-height: 1.2;
            letter-spacing: 0;
            color: var(--ink);
        }

        .result-card p {
            color: var(--muted);
            line-height: 1.65;
            margin: 0.35rem 0;
        }

        .decision-summary {
            padding: 1rem;
            margin-bottom: 1rem;
        }

        .decision-summary b {
            display: block;
            color: var(--ink);
            margin-bottom: 0.35rem;
        }

        .decision-summary p {
            color: var(--muted);
            line-height: 1.55;
            margin: 0;
        }

        .criteria-list {
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
            margin-top: 0.85rem;
        }

        .criteria-chip {
            border: 1px solid #cfe3e6;
            border-radius: 8px;
            background: #f8fbfb;
            color: #31565c;
            padding: 0.42rem 0.58rem;
            font-size: 0.88rem;
        }

        .readiness {
            padding: 1rem;
            margin-bottom: 1rem;
        }

        .readiness-top {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 1rem;
            margin-bottom: 0.65rem;
        }

        .readiness-top b {
            color: var(--ink);
        }

        .readiness-top span {
            color: var(--accent);
            font-weight: 900;
        }

        .readiness-track {
            height: 12px;
            overflow: hidden;
            border-radius: 8px;
            background: #e8eef2;
        }

        .readiness-fill {
            height: 100%;
            border-radius: 8px;
            background: linear-gradient(90deg, var(--risk), var(--warning), var(--success), var(--accent));
            width: var(--score);
        }

        .step-card {
            padding: 1rem;
            min-height: 126px;
        }

        .step-card b {
            color: var(--ink);
        }

        .step-card p {
            color: var(--muted);
            margin: 0.35rem 0 0 0;
            line-height: 1.5;
        }

        div[data-testid="stMetric"] {
            padding: 0.75rem 0.85rem;
        }

        div[data-testid="stMetricValue"] {
            color: var(--ink);
            font-size: 1.24rem;
        }

        .stButton > button {
            border-radius: 8px;
            border: 1px solid var(--accent);
            background: var(--accent);
            color: white;
            font-weight: 800;
        }

        .stButton > button:hover {
            border-color: var(--accent-deep);
            background: var(--accent-deep);
            color: white;
        }

        @media (max-width: 760px) {
            .page-header h1 {
                font-size: 1.8rem;
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def get_work_recommendation(condition, energy, focus_minutes, environment, priority):
    if condition == "Terbebani":
        if energy == "Rendah":
            return {
                "title": "Recovery block terstruktur",
                "action": "Alokasikan 10-15 menit untuk jeda singkat, lalu lanjutkan dengan satu pekerjaan administratif yang ringan.",
                "reason": "Kondisi terbebani dan energi rendah berisiko menurunkan kualitas output. Sistem memprioritaskan pemulihan singkat sebelum eksekusi kerja.",
                "tag": "Risk control",
                "level": "Prioritas sedang",
                "criteria": ["Kondisi: Terbebani", "Energi: Rendah", "Fokus: Pemulihan kerja"],
                "steps": [
                    ("Stabilisasi", "Ambil jeda singkat dan kurangi distraksi langsung."),
                    ("Pilih tugas ringan", "Mulai dari pekerjaan administratif dengan risiko rendah."),
                    ("Evaluasi ulang", "Cek energi setelah 15 menit sebelum mengambil tugas besar."),
                ],
            }
        if focus_minutes <= 15:
            return {
                "title": "Check-in singkat",
                "action": "Gunakan waktu tersedia untuk menyusun prioritas, mengklarifikasi hambatan, dan menutup satu pekerjaan kecil.",
                "reason": "Waktu fokus terbatas tidak ideal untuk pekerjaan kompleks. Sistem mengarahkan pada klarifikasi dan penyelesaian kecil.",
                "tag": "Stabilization",
                "level": "Prioritas sedang",
                "criteria": ["Kondisi: Terbebani", "Waktu fokus: Terbatas", "Fokus: Klarifikasi"],
                "steps": [
                    ("Catat hambatan", "Tulis kendala utama yang sedang menghambat progress."),
                    ("Tentukan pemilik", "Putuskan apakah tugas bisa diselesaikan sendiri atau perlu eskalasi."),
                    ("Tutup satu item", "Selesaikan satu pekerjaan kecil agar ada progress nyata."),
                ],
            }
        return {
            "title": "Focused execution block",
            "action": "Kerjakan satu deliverable prioritas selama 25 menit dengan scope yang jelas dan tanpa multitasking.",
            "reason": "Kondisi terbebani masih dapat diarahkan ke output jika energi dan waktu fokus mencukupi.",
            "tag": "Execution",
            "level": "Prioritas tinggi",
            "criteria": ["Kondisi: Terbebani", "Waktu fokus: Cukup", "Fokus: Deliverable tunggal"],
            "steps": [
                ("Definisikan output", "Tulis hasil akhir yang harus selesai dalam satu kalimat."),
                ("Batasi scope", "Kerjakan satu deliverable tanpa berpindah konteks."),
                ("Dokumentasikan progress", "Catat status akhir untuk memudahkan handover atau follow-up."),
            ],
        }

    if condition == "Kurang fokus":
        if priority == "Pengembangan skill":
            return {
                "title": "Guided learning session",
                "action": "Pilih satu materi singkat, pelajari selama 25-30 menit, lalu tulis ringkasan hasil belajar.",
                "reason": "Saat fokus menurun, pembelajaran terarah lebih efektif daripada tugas strategis yang membutuhkan konsentrasi panjang.",
                "tag": "Development",
                "level": "Prioritas sedang",
                "criteria": ["Kondisi: Kurang fokus", "Prioritas: Pengembangan skill", "Fokus: Pembelajaran terarah"],
                "steps": [
                    ("Pilih topik", "Ambil satu topik yang relevan dengan pekerjaan saat ini."),
                    ("Belajar terarah", "Gunakan durasi pendek dan hindari membuka banyak sumber."),
                    ("Ringkas output", "Tulis 3-5 poin yang bisa dipakai kembali."),
                ],
            }
        if environment == "Kondusif" and focus_minutes >= 30:
            return {
                "title": "Context reset",
                "action": "Gunakan 30 menit untuk menata ulang prioritas, membersihkan backlog kecil, atau menyelesaikan task menengah.",
                "reason": "Lingkungan kondusif dan waktu cukup membantu mengembalikan ritme kerja meski fokus sedang turun.",
                "tag": "Focus reset",
                "level": "Prioritas sedang",
                "criteria": ["Kondisi: Kurang fokus", "Lingkungan: Kondusif", "Waktu fokus: Cukup"],
                "steps": [
                    ("Rapikan daftar kerja", "Pisahkan tugas penting, mendesak, dan bisa ditunda."),
                    ("Ambil task menengah", "Pilih pekerjaan yang jelas selesai dalam satu sesi."),
                    ("Review hasil", "Bandingkan progress dengan target awal sesi."),
                ],
            }
        return {
            "title": "Structured micro-task",
            "action": "Pecah pekerjaan menjadi target 10-20 menit dan mulai dari item dengan dependensi paling rendah.",
            "reason": "Fokus rendah lebih aman dikelola dengan pekerjaan kecil yang jelas batas selesainya.",
            "tag": "Micro execution",
            "level": "Prioritas rendah",
            "criteria": ["Kondisi: Kurang fokus", "Fokus: Tugas kecil", "Risiko: Rendah"],
            "steps": [
                ("Pecah pekerjaan", "Ubah pekerjaan besar menjadi beberapa item kecil."),
                ("Mulai dari dependensi rendah", "Kerjakan item yang tidak menunggu approval orang lain."),
                ("Update status", "Tandai hasil agar progress tetap terlihat."),
            ],
        }

    if condition == "Termotivasi":
        if energy == "Tinggi":
            if priority == "Kesejahteraan":
                return {
                    "title": "Wellbeing activity block",
                    "action": "Gunakan sesi 30-45 menit untuk aktivitas pemulihan fisik atau mental yang mendukung performa kerja.",
                    "reason": "Motivasi dan energi tinggi dapat diarahkan ke kesejahteraan agar performa tetap berkelanjutan.",
                    "tag": "Wellbeing",
                    "level": "Prioritas sedang",
                    "criteria": ["Kondisi: Termotivasi", "Energi: Tinggi", "Prioritas: Kesejahteraan"],
                    "steps": [
                        ("Pilih aktivitas", "Gunakan aktivitas ringan, mobility, atau mindful break."),
                        ("Tetapkan durasi", "Batasi sesi agar tidak mengganggu agenda kerja."),
                        ("Kembali bertahap", "Masuk lagi ke pekerjaan dengan satu target jelas."),
                    ],
                }
            return {
                "title": "Strategic work block",
                "action": "Prioritaskan pekerjaan bernilai tinggi selama 45-60 menit, terutama yang berdampak pada deliverable tim.",
                "reason": "Kondisi dan energi optimal sebaiknya dialokasikan ke pekerjaan strategis dengan dampak tinggi.",
                "tag": "High impact",
                "level": "Prioritas tinggi",
                "criteria": ["Kondisi: Termotivasi", "Energi: Tinggi", "Fokus: High impact work"],
                "steps": [
                    ("Pilih deliverable utama", "Ambil pekerjaan yang paling berdampak pada target tim."),
                    ("Blokir distraksi", "Tutup channel yang tidak terkait selama sesi berlangsung."),
                    ("Kirim progress", "Update hasil kepada stakeholder terkait."),
                ],
            }
        return {
            "title": "Steady progress block",
            "action": "Kerjakan pekerjaan prioritas menengah selama 25 menit, lalu evaluasi kapasitas sebelum lanjut.",
            "reason": "Motivasi tinggi dengan energi sedang perlu diarahkan ke progress stabil, bukan sprint panjang.",
            "tag": "Sustainable pace",
            "level": "Prioritas sedang",
            "criteria": ["Kondisi: Termotivasi", "Energi: Tidak tinggi", "Fokus: Ritme stabil"],
            "steps": [
                ("Pilih task menengah", "Ambil pekerjaan yang tidak terlalu kompleks."),
                ("Kerjakan satu sesi", "Gunakan batas 25 menit untuk menjaga ritme."),
                ("Evaluasi kapasitas", "Lanjutkan hanya jika energi masih memadai."),
            ],
        }

    if condition == "Stabil":
        if focus_minutes < 15:
            return {
                "title": "Quick operational win",
                "action": "Gunakan waktu pendek untuk menyelesaikan satu pekerjaan kecil seperti update status, review agenda, atau follow-up singkat.",
                "reason": "Durasi fokus yang pendek lebih efektif untuk pekerjaan operasional dengan output langsung.",
                "tag": "Operational",
                "level": "Prioritas rendah",
                "criteria": ["Kondisi: Stabil", "Waktu fokus: Pendek", "Fokus: Output cepat"],
                "steps": [
                    ("Pilih item cepat", "Ambil tugas yang selesai kurang dari 15 menit."),
                    ("Eksekusi langsung", "Jangan membuka backlog besar terlebih dahulu."),
                    ("Tandai selesai", "Update status agar progress tercatat."),
                ],
            }
        if priority == "Pengembangan skill":
            return {
                "title": "Focused development block",
                "action": "Pelajari satu topik kerja selama 30 menit dan dokumentasikan insight yang bisa diterapkan.",
                "reason": "Kondisi stabil cocok untuk pembelajaran terstruktur dan peningkatan kompetensi.",
                "tag": "Development",
                "level": "Prioritas sedang",
                "criteria": ["Kondisi: Stabil", "Prioritas: Pengembangan skill", "Fokus: Kompetensi"],
                "steps": [
                    ("Tentukan topik", "Pilih materi yang relevan dengan role atau project."),
                    ("Praktik singkat", "Gunakan contoh atau studi kasus kecil."),
                    ("Dokumentasikan insight", "Simpan catatan agar bisa dibagikan atau dipakai ulang."),
                ],
            }
        return {
            "title": "Priority planning block",
            "action": "Tentukan tiga prioritas kerja, pilih satu yang paling berdampak, lalu mulai dari langkah pertama.",
            "reason": "Kondisi stabil cocok untuk pengambilan keputusan rasional dan perencanaan kerja bertahap.",
            "tag": "Planning",
            "level": "Prioritas sedang",
            "criteria": ["Kondisi: Stabil", "Fokus: Prioritization", "Output: Rencana kerja"],
            "steps": [
                ("Tulis tiga prioritas", "Batasi daftar agar keputusan tetap jelas."),
                ("Pilih dampak terbesar", "Utamakan pekerjaan yang membantu target tim."),
                ("Mulai langkah pertama", "Buat progress awal yang mudah diukur."),
            ],
        }

    return {
        "title": "Low-risk starter task",
        "action": "Mulai dengan pekerjaan ringan selama 10 menit, lalu evaluasi kembali kondisi sebelum mengambil tugas lanjutan.",
        "reason": "Jika kondisi belum jelas, sistem memilih pendekatan aman dengan risiko rendah.",
        "tag": "Safe start",
        "level": "Prioritas rendah",
        "criteria": ["Kondisi: Belum jelas", "Fokus: Risiko rendah"],
        "steps": [
            ("Mulai ringan", "Ambil pekerjaan yang mudah dihentikan atau dilanjutkan."),
            ("Cek kapasitas", "Evaluasi energi setelah 10 menit."),
            ("Sesuaikan prioritas", "Naikkan atau turunkan intensitas sesuai kondisi."),
        ],
    }


def get_readiness_score(condition, energy, focus_minutes, priority):
    score = 42

    if energy == "Tinggi":
        score += 25
    elif energy == "Sedang":
        score += 13
    else:
        score -= 5

    if condition == "Termotivasi":
        score += 20
    elif condition == "Stabil":
        score += 8
    elif condition == "Kurang fokus":
        score += 2
    else:
        score -= 8

    if focus_minutes >= 60:
        score += 12
    elif focus_minutes >= 30:
        score += 7
    else:
        score -= 4

    if priority in ["Operasional", "Pengembangan skill"]:
        score += 5

    return max(12, min(score, 100))


inject_styles()

st.markdown(
    """
    <div class="page-header">
        <div class="eyebrow">Internal decision support</div>
        <h1>Workforce Recommendation System</h1>
        <p>
            Dashboard internal untuk membantu menentukan aktivitas kerja berikutnya
            berdasarkan kondisi karyawan, kapasitas fokus, lingkungan kerja, dan prioritas operasional.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

left, right = st.columns([0.86, 1.14], gap="large")

with left:
    st.markdown('<div class="section-title">Assessment input</div>', unsafe_allow_html=True)
    with st.container(border=True):
        condition = st.selectbox(
            "Kondisi kerja",
            ["Stabil", "Termotivasi", "Terbebani", "Kurang fokus"],
        )
        energy = st.radio(
            "Tingkat energi",
            ["Rendah", "Sedang", "Tinggi"],
            index=1,
            horizontal=True,
        )
        focus_minutes = st.slider("Waktu fokus tersedia", 5, 120, 30, step=5)
        environment = st.selectbox(
            "Lingkungan kerja",
            ["Kondusif", "Netral", "Banyak distraksi"],
        )
        priority = st.selectbox(
            "Prioritas utama",
            ["Operasional", "Pengembangan skill", "Kesejahteraan", "Administratif"],
        )

        analyze = st.button("Generate recommendation", use_container_width=True)

    st.markdown('<div class="section-title">Input summary</div>', unsafe_allow_html=True)
    metric_1, metric_2 = st.columns(2)
    with metric_1:
        st.metric("Kondisi", condition)
        st.metric("Fokus", f"{focus_minutes} menit")
    with metric_2:
        st.metric("Energi", energy)
        st.metric("Prioritas", priority)

with right:
    result = get_work_recommendation(
        condition=condition,
        energy=energy,
        focus_minutes=focus_minutes,
        environment=environment,
        priority=priority,
    )
    readiness_score = get_readiness_score(condition, energy, focus_minutes, priority)

    st.markdown('<div class="section-title">Recommendation output</div>', unsafe_allow_html=True)
    st.markdown(
        f"""
        <div class="result-card">
            <span class="badge">{result["tag"]} - {result["level"]}</span>
            <h2>{result["title"]}</h2>
            <p>{result["action"]}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
        <div class="readiness">
            <div class="readiness-top">
                <b>Readiness score</b>
                <span>{readiness_score}%</span>
            </div>
            <div class="readiness-track">
                <div class="readiness-fill" style="--score: {readiness_score}%;"></div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
        <div class="decision-summary">
            <b>Decision rationale</b>
            <p>{result["reason"]}</p>
            <div class="criteria-list">
                {"".join(f'<span class="criteria-chip">{item}</span>' for item in result["criteria"])}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<div class="section-title">Action plan</div>', unsafe_allow_html=True)
    step_cols = st.columns(3)
    for index, (step_title, step_body) in enumerate(result["steps"]):
        with step_cols[index]:
            st.markdown(
                f"""
                <div class="step-card">
                    <b>{index + 1}. {step_title}</b>
                    <p>{step_body}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

if analyze:
    st.toast("Recommendation generated successfully.")
