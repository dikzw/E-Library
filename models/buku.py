from odoo import models, fields, api

class Buku(models.Model):
    _name = 'buku'
    _description = 'Model untuk Manajemen Buku'
    _order = 'name asc'

    # Field Utama
    name = fields.Char(string='Judul Buku', required=True)
    kode_buku = fields.Char(string='Kode Buku', required=True)
    penulis = fields.Char(string='Penulis', required=True)
    penerbit = fields.Char(string='Penerbit')
    tahun_terbit = fields.Integer(string='Tahun Terbit')
    isbn = fields.Char(string='ISBN', help='Nomor ISBN buku')
    bahasa = fields.Selection([
        ('indonesia', 'Indonesia'),
        ('inggris', 'Inggris'),
        ('lainnya', 'Lainnya'),
    ], string='Bahasa', default='indonesia')
    jumlah_halaman = fields.Integer(string='Jumlah Halaman')
    deskripsi = fields.Text(string='Deskripsi Buku')
    
    # Tambahan field jumlah buku
    jumlah_tersedia = fields.Integer(string='Jumlah Buku Tersedia', default=0)

    # Field Status
    status = fields.Selection([
        ('tersedia', 'Tersedia'),
        ('tidak', 'Tidak Tersedia')
    ], string='Status Buku', compute='_compute_status', store=True)
    
    perpus_ids = fields.One2many(
        'perpus',
        'buku_id',
        string='Kode Peminjaman'
    )

    # Compute method untuk status
    @api.depends('jumlah_tersedia')
    def _compute_status(self):
        for record in self:
            record.status = 'tersedia' if record.jumlah_tersedia > 0 else 'tidak'