from django.core.management.base import BaseCommand
from core.models import SiteConfig, Program, Achievement, Extracurricular


class Command(BaseCommand):
    help = 'Seed database with initial placeholder data for SMKN 5 Kota Tangerang'

    def handle(self, *args, **options):
        self._seed_config()
        self._seed_programs()
        self._seed_achievements()
        self._seed_ekskul()
        self.stdout.write(self.style.SUCCESS('Data awal berhasil dibuat.'))

    def _seed_config(self):
        if SiteConfig.objects.exists():
            self.stdout.write('SiteConfig sudah ada, dilewati.')
            return
        SiteConfig.objects.create(
            school_name='SMKN 5 Kota Tangerang',
            tagline='Mendidik dengan Hati, Berkarya untuk Bangsa',
            description=(
                'SMK Negeri 5 Kota Tangerang adalah sekolah menengah kejuruan negeri '
                'yang berkomitmen mencetak lulusan terampil, berkarakter, dan siap kerja. '
                'Dengan fasilitas modern dan tenaga pendidik berpengalaman, kami mempersiapkan '
                'generasi penerus bangsa yang kompeten di bidangnya.'
            ),
            address='Jl. Moh. Toha No.255, Bugel, Karawaci, Kota Tangerang, Banten 15113',
            phone='(021) 5523456',
            email='smkn5tangerang@gmail.com',
            vision=(
                'Terwujudnya sekolah vokasi unggul yang menghasilkan lulusan berkarakter '
                'Pancasila, kompeten, dan berdaya saing di era global.'
            ),
            mission=(
                'Menyelenggarakan pendidikan vokasi berbasis kompetensi yang relevan dengan kebutuhan industri\n'
                'Membentuk peserta didik yang berakhlak mulia, disiplin, dan berjiwa Pancasila\n'
                'Mengembangkan kemitraan strategis dengan dunia usaha dan dunia industri (DUDI)\n'
                'Menciptakan lingkungan belajar yang kondusif, inovatif, dan berbasis teknologi\n'
                'Meningkatkan kompetensi dan profesionalisme tenaga pendidik secara berkelanjutan'
            ),
            total_students=1500,
            total_teachers=85,
            founded_year=2003,
            accreditation='A',
        )
        self.stdout.write('SiteConfig dibuat.')

    def _seed_programs(self):
        if Program.objects.exists():
            self.stdout.write('Program sudah ada, dilewati.')
            return
        programs = [
            ('Teknik Komputer dan Jaringan', 'TKJ',
             'Mempelajari instalasi, konfigurasi, dan pemeliharaan jaringan komputer serta sistem operasi. '
             'Lulusan siap bekerja sebagai teknisi jaringan, administrator sistem, atau wirausaha di bidang IT.', 1),
            ('Rekayasa Perangkat Lunak', 'RPL',
             'Mempelajari perancangan, pengembangan, dan pengujian perangkat lunak berbasis web maupun mobile. '
             'Lulusan siap menjadi programmer, web developer, atau software engineer profesional.', 2),
            ('Multimedia', 'MM',
             'Mempelajari desain grafis, videografi, animasi, dan produksi konten digital. '
             'Lulusan siap berkarir sebagai desainer kreatif, video editor, atau content creator.', 3),
            ('Teknik Kendaraan Ringan Otomotif', 'TKRO',
             'Mempelajari perawatan, perbaikan, dan diagnosa kendaraan ringan bermesin bensin maupun diesel. '
             'Lulusan siap bekerja di bengkel otomotif, dealer kendaraan, atau wirausaha sendiri.', 4),
            ('Akuntansi dan Keuangan Lembaga', 'AKL',
             'Mempelajari pencatatan akuntansi, perpajakan, dan pengelolaan keuangan perusahaan. '
             'Lulusan siap bekerja sebagai akuntan, staf keuangan, atau kasir profesional.', 5),
            ('Desain Komunikasi Visual', 'DKV',
             'Mempelajari prinsip desain, tipografi, dan komunikasi visual untuk media cetak maupun digital. '
             'Lulusan siap menjadi desainer grafis, illustrator, atau creative director.', 6),
        ]
        for name, short, desc, order in programs:
            Program.objects.create(name=name, short_name=short, description=desc, order=order)
        self.stdout.write(f'{len(programs)} program keahlian dibuat.')

    def _seed_achievements(self):
        if Achievement.objects.exists():
            self.stdout.write('Prestasi sudah ada, dilewati.')
            return
        achievements = [
            ('Juara 1 LKS Teknik Komputer dan Jaringan', 2024, 'provinsi',
             'Meraih juara pertama dalam Lomba Kompetensi Siswa tingkat Provinsi Banten.'),
            ('Juara 2 LKS Web Design', 2024, 'provinsi',
             'Meraih juara kedua dalam Lomba Kompetensi Siswa Web Design tingkat Provinsi Banten.'),
            ('Juara 1 Olimpiade Matematika', 2023, 'kota',
             'Meraih juara pertama dalam Olimpiade Matematika tingkat Kota Tangerang.'),
            ('Juara 1 LKS Akuntansi', 2023, 'nasional',
             'Meraih juara pertama dalam Lomba Kompetensi Siswa Akuntansi tingkat Nasional.'),
            ('Sekolah Adiwiyata Mandiri', 2023, 'nasional',
             'Meraih penghargaan Sekolah Adiwiyata Mandiri dari Kementerian Lingkungan Hidup.'),
            ('Juara 2 Film Pendek Pelajar', 2022, 'provinsi',
             'Meraih juara kedua dalam Festival Film Pendek Pelajar tingkat Provinsi Banten.'),
        ]
        for title, year, level, desc in achievements:
            Achievement.objects.create(title=title, year=year, level=level, description=desc)
        self.stdout.write(f'{len(achievements)} prestasi dibuat.')

    def _seed_ekskul(self):
        if Extracurricular.objects.exists():
            self.stdout.write('Ekstrakurikuler sudah ada, dilewati.')
            return
        ekskul = [
            ('Pramuka', 'Kegiatan kepramukaan yang membentuk karakter, disiplin, dan jiwa kepemimpinan siswa.', 1),
            ('PMR (Palang Merah Remaja)', 'Melatih siswa dalam pertolongan pertama dan kepedulian sosial.', 2),
            ('OSIS', 'Organisasi siswa intra sekolah sebagai wadah pengembangan kepemimpinan.', 3),
            ('Futsal', 'Kegiatan olahraga futsal untuk pengembangan bakat dan prestasi siswa.', 4),
            ('Basket', 'Kegiatan olahraga bola basket untuk pengembangan bakat dan sportivitas.', 5),
            ('English Club', 'Klub bahasa Inggris untuk meningkatkan kemampuan komunikasi internasional.', 6),
            ('Robotika', 'Kegiatan pengembangan minat di bidang teknologi robotika dan otomasi.', 7),
            ('Paduan Suara', 'Kegiatan seni vokal untuk mengembangkan bakat dan apresiasi musik.', 8),
        ]
        for name, desc, order in ekskul:
            Extracurricular.objects.create(name=name, description=desc, order=order)
        self.stdout.write(f'{len(ekskul)} ekstrakurikuler dibuat.')
