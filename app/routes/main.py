from flask import render_template, request, redirect, url_for, flash, session
from app.routes import main_bp
from app.routes.auth import login_required
from app.models.transaction import Transaction
from app.models.category import Category
from app.models.budget import Budget

@main_bp.route('/')
@login_required
def index():
    """
    GET: 顯示當月總結餘、近幾筆紀錄與預算消耗進度
    """
    pass

@main_bp.route('/transactions')
@login_required
def transactions():
    """
    GET: 顯示歷史紀錄列表，支援參數篩選 (如 ?month=2024-05)
    """
    pass

@main_bp.route('/transactions/new', methods=('GET', 'POST'))
@login_required
def create_transaction():
    """
    GET: 顯示新增記帳表單
    POST: 接收表單資料並建立 Transaction，然後導向首頁
    """
    pass

@main_bp.route('/transactions/<int:id>/edit', methods=('GET', 'POST'))
@login_required
def edit_transaction(id):
    """
    GET: 顯示編輯表單（需帶入原資料）
    POST: 實際上不使用此路徑處理更新，由下方 update 處理
    但為了相容可在此處理或分開
    """
    pass

@main_bp.route('/transactions/<int:id>/update', methods=('POST',))
@login_required
def update_transaction(id):
    """
    POST: 接收表單並更新對應的 Transaction，然後導向歷史紀錄
    """
    pass

@main_bp.route('/transactions/<int:id>/delete', methods=('POST',))
@login_required
def delete_transaction(id):
    """
    POST: 刪除對應的 Transaction，然後導向歷史紀錄
    """
    pass

@main_bp.route('/categories', methods=('GET', 'POST'))
@login_required
def categories():
    """
    GET: 顯示所有分類
    POST: 新增自訂分類
    """
    pass

@main_bp.route('/categories/<int:id>/delete', methods=('POST',))
@login_required
def delete_category(id):
    """
    POST: 刪除自訂分類（需檢查是否被使用中）
    """
    pass

@main_bp.route('/budgets', methods=('GET', 'POST'))
@login_required
def budgets():
    """
    GET: 顯示當月預算設定表單與進度
    POST: 更新或建立當月預算
    """
    pass

@main_bp.route('/statistics')
@login_required
def statistics():
    """
    GET: 查詢當月所有支出與收入，以 JSON 格式提供前端繪製圖表，
         或是直接傳遞彙整資料給模板渲染。
    """
    pass
