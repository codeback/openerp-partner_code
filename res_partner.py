from osv import osv, fields

class res_partner(osv.osv):
    _inherit = 'res.partner'

    def create(self, cr, uid, vals, context={}):
        if (not 'ref' in vals) or (vals['ref'] == False):
            vals['ref'] = self.pool.get('ir.sequence').get(cr, uid, 'res.partner')
        return super(res_partner, self).create(cr, uid, vals, context)

    _defaults = {
        'ref': lambda obj, cr, uid, context: obj.pool.get('ir.sequence').get(cr, uid, 'res_partner'),
    }
res_partner()