# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Perpustakaan (models.Model):
    _name = 'perpus'
    _description = 'Perpustakaan'

    name                    = fields.Char(string='Kode Peminjaman', readonly=True)
    peminjam                = fields.Many2one('res.partner', string='Peminjam', required=True)
    email_peminjam          = fields.Char(string='Email Peminjam', related='peminjam.email', readonly=True)
    phone_peminjam          = fields.Char(string='Telepon Peminjam', related='peminjam.phone', readonly=True)
    # alamat_peminjam         = fields.Text(string='Alamat Peminjam', related='peminjam.street', readonly=True)
    # jenis_kelamin_peminjam  = fields.Selection(string='Jenis Kelamin', related='peminjam.gender', readonly=True)
    # tanggal_lahir_peminjam  = fields.Date(string='Tanggal Lahir', related='peminjam.birthday', readonly=True)
    
    buku_id = fields.Many2one(
        'buku',
        string='Buku',
        domain=[('status', '=', 'tersedia')],
    )

    # Fields related dari buku_id
    judul_buku = fields.Char(string='Judul Buku', related='buku_id.name', readonly=True)
    kode_buku = fields.Char(string='Kode Buku', related='buku_id.kode_buku', readonly=True)
    penulis = fields.Char(string='Penulis', related='buku_id.penulis', readonly=True)
    penerbit = fields.Char(string='Penerbit', related='buku_id.penerbit', readonly=True)
    tahun_terbit = fields.Integer(string='Tahun Terbit', related='buku_id.tahun_terbit', readonly=True)
    isbn = fields.Char(string='ISBN', related='buku_id.isbn', readonly=True)
    bahasa = fields.Selection(
        string='Bahasa',
        related='buku_id.bahasa',
        readonly=True
    )
    jumlah_halaman = fields.Integer(string='Jumlah Halaman', related='buku_id.jumlah_halaman', readonly=True)
    deskripsi = fields.Text(string='Deskripsi Buku', related='buku_id.deskripsi', readonly=True)
    jumlah_tersedia = fields.Integer(string='Jumlah Tersedia', related='buku_id.jumlah_tersedia', readonly=True)
    
    @api.model
    def create(self, vals):
        # Generate kode peminjaman
        if not vals.get('name'):
            last_loan = self.search([], order='id desc', limit=1)
            last_number = int(last_loan.name.split('/')[-1]) if last_loan and last_loan.name else 0
            vals['name'] = f"PINJ/{str(last_number + 1).zfill(4)}"
        return super(Perpustakaan, self).create(vals)

