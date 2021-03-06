{
    'name': 'Library Management',
    'version': '14.0.1.0.0',
    'summary': """Module help library management.""",
    'description': """
    Author: Nhóm 3 - 44K21.2
    Members:
    - Nguyễn Thùy Dung
    - Đỗ Anh Thư
    - Phan Thị Thùy Trang
    """,
    'category': 'Library',
    'author': '44K21.2',
    'company': '',
    'maintainer': '44K21.2',
    'website': '',
    'depends': [
        'hr', 'product'
    ],
    'data': [
        # SECURITY
        'security/ir.model.access.csv',
        #DATA
        # VIEWS
        'views/assets.xml',
        'views/book_views.xml',
        'views/book_category_views.xml',
        'views/reader_views.xml',
        'views/call_card_views.xml',
        # Menus
        'menu/menu_views.xml',
    ],
    'demo': [],
    'images': [],
    'installable': True,
    'auto_install': False,
    'application': False,
}
