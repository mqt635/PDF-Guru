import argparse

def getParser():
    parser = argparse.ArgumentParser()
    sub_parsers = parser.add_subparsers()
    # 合并子命令
    merge_parser = sub_parsers.add_parser("merge", help="合并", description="合并pdf文件")
    merge_parser.set_defaults(which='merge')
    merge_parser.add_argument("input_path_list", type=str, nargs="+", help="pdf文件路径")
    merge_parser.add_argument("-o", "--output", type=str, help="输出文件路径")
    merge_parser.add_argument("--sort_method", type=str, choices=['default', 'name', 'name_digit', 'ctime', 'mtime'], default="default", help="排序方式")
    merge_parser.add_argument("--sort_direction", type=str, choices=['asc', 'desc'], default="asc", help="排序方向")

    # 拆分子命令
    split_parser = sub_parsers.add_parser("split", help="拆分", description="拆分pdf文件")
    split_parser.set_defaults(which='split')
    split_parser.add_argument("input_path", type=str, help="pdf文件路径")
    split_parser.add_argument("--mode", type=str, choices=['chunk', 'page', 'toc'], default="chunk", help="拆分模式")
    split_parser.add_argument("--page_range", type=str, default="all", help="页码范围")
    split_parser.add_argument("--chunk_size", type=int, default=10, help="拆分块大小")
    split_parser.add_argument("-o", "--output", type=str, help="输出文件路径")
    split_parser.add_argument("--toc-level", type=int, default=1, help="目录层级")

    #  删除子命令
    delete_parser = sub_parsers.add_parser("delete", help="删除", description="删除pdf文件")
    delete_parser.set_defaults(which='delete')
    delete_parser.add_argument("input_path", type=str, help="pdf文件路径")
    delete_parser.add_argument("--page_range", type=str, default="all", help="页码范围")
    delete_parser.add_argument("-o", "--output", type=str, help="输出文件路径")

    # 插入子命令
    insert_parser = sub_parsers.add_parser("insert", help="插入", description="插入pdf文件")
    insert_parser.set_defaults(which='insert')
    insert_parser.add_argument("--method", type=str, choices=['blank', 'pdf'], default="pdf", help="插入方式")
    insert_parser.add_argument("input_path1", type=str, help="被插入的pdf文件路径")
    insert_parser.add_argument("input_path2", type=str, help="插入pdf文件路径")
    insert_parser.add_argument("--insert_pos", type=int, default=0, help="插入位置页码")
    insert_parser.add_argument("--pos-type", type=str, choices=['before_first', 'after_first', 'before_last', 'after_last', 'before_custom', 'after_custom'], default="before", help="插入位置类型")
    insert_parser.add_argument("--page_range", type=str, default="all", help="插入pdf的页码范围")
    insert_parser.add_argument("--orientation", type=str, choices=['portrait', 'landscape'], default="portrait", help="纸张方向")
    insert_parser.add_argument("--paper_size", type=str, default="A4", help="纸张大小")
    insert_parser.add_argument("--count", type=int, default=1, help="插入数量")
    insert_parser.add_argument("-o", "--output", type=str, help="输出文件路径")

    # 替换子命令
    replace_parser = sub_parsers.add_parser("replace", help="替换", description="替换pdf文件")
    replace_parser.set_defaults(which='replace')
    replace_parser.add_argument("input_path1", type=str, help="被替换的pdf文件路径")
    replace_parser.add_argument("input_path2", type=str, help="替换pdf文件路径")
    replace_parser.add_argument("--src_page_range", type=str, default="all", help="页码范围")
    replace_parser.add_argument("--dst_page_range", type=str, default="all", help="页码范围")
    replace_parser.add_argument("-o", "--output", type=str, help="输出文件路径")

    # 旋转子命令
    rotate_parser = sub_parsers.add_parser("rotate", help="旋转", description="旋转pdf文件")
    rotate_parser.set_defaults(which='rotate')
    rotate_parser.add_argument("input_path", type=str, help="pdf文件路径")
    rotate_parser.add_argument("--page_range", type=str, default="all", help="页码范围")
    rotate_parser.add_argument("--angle", type=int, default=90, help="旋转角度")
    rotate_parser.add_argument("-o", "--output", type=str, help="输出文件路径")

    # 重排子命令
    reorder_parser = sub_parsers.add_parser("reorder", help="重排", description="重排pdf文件")
    reorder_parser.set_defaults(which='reorder')
    reorder_parser.add_argument("input_path", type=str, help="pdf文件路径")
    reorder_parser.add_argument("--page_range", type=str, default="all", help="页码范围")
    reorder_parser.add_argument("-o", "--output", type=str, help="输出文件路径")

    # 加密子命令
    encrypt_parser = sub_parsers.add_parser("encrypt", help="加密", description="加密pdf文件")
    encrypt_parser.add_argument("input_path", type=str, help="pdf文件路径")
    encrypt_parser.add_argument("--user_password", type=str, help="用户密码")
    encrypt_parser.add_argument("--owner_password", type=str, help="所有者密码")
    encrypt_parser.add_argument("--perm", type=str, nargs="+", help="权限")
    encrypt_parser.add_argument("-o", "--output", type=str, help="输出文件路径")
    encrypt_parser.set_defaults(which='encrypt')
    
    # 解密子命令
    decrypt_parser = sub_parsers.add_parser("decrypt", help="解密", description="解密pdf文件")
    decrypt_parser.add_argument("input_path", type=str, help="pdf文件路径")
    decrypt_parser.add_argument("--password", type=str, help="密码")
    decrypt_parser.add_argument("-o", "--output", type=str, help="输出文件路径")
    decrypt_parser.set_defaults(which='decrypt')
    
    # 修改密码子命令
    change_password_parser = sub_parsers.add_parser("change_password", help="修改密码", description="修改pdf文件密码")
    change_password_parser.set_defaults(which="change_password")
    change_password_parser.add_argument("input_path", type=str, help="pdf文件路径")
    change_password_parser.add_argument("--old_user_password", type=str, help="旧用户密码")
    change_password_parser.add_argument("--user_password", type=str, help="新用户密码")
    change_password_parser.add_argument("--old_owner_password", type=str, help="旧所有者密码")
    change_password_parser.add_argument("--owner_password", type=str, help="新所有者密码")
    change_password_parser.add_argument("-o", "--output", type=str, help="输出文件路径")

    # 书签子命令
    bookmark_parser = sub_parsers.add_parser("bookmark", help="书签", description="添加、提取、转换书签")
    bookmark_sub_parsers = bookmark_parser.add_subparsers()
    bookmark_parser.set_defaults(which='bookmark')

    ## 添加书签
    bookmark_add_parser = bookmark_sub_parsers.add_parser("add", help="添加书签")
    ### 文件书签
    bookmark_add_parser.add_argument("input_path", type=str, help="pdf文件路径")
    bookmark_add_parser.add_argument("--method", type=str, choices=['file', 'gap'], default="file", help="添加方式")
    bookmark_add_parser.add_argument("--toc", type=str, help="目录文件路径")
    bookmark_add_parser.add_argument("--offset", type=int, default=0, help="偏移量, 计算方式: “pdf文件实际页码” - “目录文件标注页码”")
    bookmark_add_parser.add_argument("-o", "--output", type=str, help="输出文件路径")
    bookmark_add_parser.set_defaults(bookmark_which='add')

    ### 页码书签
    bookmark_add_parser.add_argument("--gap", type=int, default=1, help="页码间隔")
    bookmark_add_parser.add_argument("--format", type=str, default="第%p页", help="页码格式")
    bookmark_add_parser.add_argument("--page_range", type=str, default="all", help="页码范围")
    bookmark_add_parser.add_argument("--start-number", type=int, default=1, help="起始编号")

    ## 提取书签
    bookmark_extract_parser = bookmark_sub_parsers.add_parser("extract", help="提取书签")
    bookmark_extract_parser.add_argument("input_path", type=str, help="pdf文件路径")
    bookmark_extract_parser.add_argument("--format", type=str, default="txt", choices=['txt', 'json'], help="输出文件格式")
    bookmark_extract_parser.add_argument("-o", "--output", type=str, help="输出文件路径")
    bookmark_extract_parser.set_defaults(bookmark_which='extract')

    ## 书签转换
    bookmark_transform_parser = bookmark_sub_parsers.add_parser("transform", help="转换书签")
    bookmark_transform_parser.add_argument("--toc", type=str, help="目录文件路径")
    bookmark_transform_parser.add_argument("--add_offset", type=int, default=0, help="页码偏移量")
    bookmark_transform_parser.add_argument("--level-dict", type=str, action="append", help="目录层级字典")
    bookmark_transform_parser.add_argument("--delete-level-below", type=int, default=0, help="删除目录层级")
    bookmark_transform_parser.add_argument("--default-level", type=int, default=1, help="默认目录层级")
    bookmark_transform_parser.add_argument("--remove-blank-lines", action="store_true", help="删除空行")
    bookmark_transform_parser.add_argument("-o", "--output", type=str, help="输出文件路径")
    bookmark_transform_parser.set_defaults(bookmark_which='transform')

    ## 书签识别
    bookmark_detect_parser = bookmark_sub_parsers.add_parser("detect", help="识别书签")
    bookmark_detect_parser.set_defaults(bookmark_which="detect")
    bookmark_detect_parser.add_argument("--type", type=str, choices=['font', 'ocr'], default="font", help="识别方式")
    bookmark_detect_parser.add_argument("input_path", type=str, help="pdf文件路径")
    bookmark_detect_parser.add_argument("--page_range", type=str, default="all", help="页码范围")
    bookmark_detect_parser.add_argument("-o", "--output", type=str, help="输出文件路径")

    # 水印子命令
    watermark_parser = sub_parsers.add_parser("watermark", help="水印", description="添加文本水印")
    watermark_parser.set_defaults(which='watermark')

    watermark_subparsers = watermark_parser.add_subparsers()
    watermark_add_parser= watermark_subparsers.add_parser("add", help="添加水印")
    watermark_add_parser.set_defaults(watermark_which='add')
    watermark_add_parser.add_argument("input_path", type=str, help="pdf文件路径")
    watermark_add_parser.add_argument("--type", type=str, choices=['text', 'image', 'pdf'], default="text", help="水印类型")
    watermark_add_parser.add_argument("--mark-text", type=str, dest="mark_text", help="水印文本")
    watermark_add_parser.add_argument("--font-family", type=str, dest="font_family", help="水印字体路径")
    watermark_add_parser.add_argument("--font-size", type=int, default=50, dest="font_size", help="水印字体大小")
    watermark_add_parser.add_argument("--color", type=str, default="#000000", dest="color", help="水印文本颜色")
    watermark_add_parser.add_argument("--angle", type=int, default=30, dest="angle", help="水印旋转角度")
    watermark_add_parser.add_argument("--opacity", type=float, default=0.3, dest="opacity", help="水印不透明度")
    watermark_add_parser.add_argument("--line-spacing", type=float, default=1, dest="line_spacing", help="水印行间距")
    watermark_add_parser.add_argument("--word-spacing", type=float, default=1, dest="word_spacing", help="相邻水印间距")
    watermark_add_parser.add_argument("--x-offset", type=float, default=0, dest="x_offset", help="水印x轴偏移量")
    watermark_add_parser.add_argument("--y-offset", type=float, default=0, dest="y_offset", help="水印y轴偏移量")
    watermark_add_parser.add_argument("--multiple-mode", action="store_true", dest="multiple_mode", help="多行水印模式")
    watermark_add_parser.add_argument("--num-lines", type=int, default=1, dest="num_lines", help="多行水印行数")
    watermark_add_parser.add_argument("--wm-path", type=str, dest="wm_path", help="水印图片路径")
    watermark_add_parser.add_argument("--scale", type=float, default=1, dest="scale", help="水印图片缩放比例")
    watermark_add_parser.add_argument("--page_range", type=str, default="all", help="页码范围")
    watermark_add_parser.add_argument("--layer", type=str, default="bottom", help="水印图层")
    watermark_add_parser.add_argument("-o", "--output", type=str, help="输出文件路径")

    watermark_remove_parser = watermark_subparsers.add_parser("remove", help="删除水印")
    watermark_remove_parser.set_defaults(watermark_which='remove')
    watermark_remove_parser.add_argument("input_path", type=str, help="pdf文件路径")
    watermark_remove_parser.add_argument("--method", type=str, choices=['type', 'index', 'text'], default="type", help="删除方式")
    watermark_remove_parser.add_argument("--page_range", type=str, default="all", help="页码范围")
    watermark_remove_parser.add_argument("--wm_index", type=int, nargs="+", help="水印元素所有索引")
    watermark_remove_parser.add_argument("--wm_text", type=str, help="水印文本")
    watermark_remove_parser.add_argument("-o", "--output", type=str, help="输出文件路径")

    watermark_detect_parser = watermark_subparsers.add_parser("detect", help="检测水印")
    watermark_detect_parser.set_defaults(watermark_which='detect')
    watermark_detect_parser.add_argument("input_path", type=str, help="pdf文件路径")
    watermark_detect_parser.add_argument("--wm_index", type=int, default=0, help="水印所在页码")
    watermark_detect_parser.add_argument("-o", "--output", type=str, help="输出文件路径")


    # 压缩子命令
    compress_parser = sub_parsers.add_parser("compress", help="压缩", description="压缩pdf文件")
    compress_parser.add_argument("input_path", type=str, help="pdf文件路径")
    compress_parser.add_argument("-o", "--output", type=str, help="输出文件路径")
    compress_parser.set_defaults(which='compress')

    # 缩放子命令
    resize_parser = sub_parsers.add_parser("resize", help="缩放", description="缩放pdf文件")
    resize_parser.set_defaults(which='resize')
    resize_parser.add_argument("input_path", type=str, help="pdf文件路径")
    resize_parser.add_argument("--method", type=str, choices=['dim', 'scale', 'paper_size'], default="dim", help="缩放方式")
    resize_parser.add_argument("--width", type=float, help="宽度")
    resize_parser.add_argument("--height", type=float, help="高度")
    resize_parser.add_argument("--scale", type=float, help="缩放比例")
    resize_parser.add_argument("--paper_size", type=str, help="纸张大小")
    resize_parser.add_argument("--page_range", type=str, default="all", help="页码范围")
    resize_parser.add_argument("--unit", type=str, choices=['pt', 'mm', 'cm', 'in'], default="pt", help="单位")
    resize_parser.add_argument("-o", "--output", type=str, help="输出文件路径")

    # 提取子命令
    extract_parser = sub_parsers.add_parser("extract", help="提取", description="提取pdf文件")
    extract_parser.set_defaults(which='extract')
    extract_parser.add_argument("input_path", type=str, help="pdf文件路径")
    extract_parser.add_argument("--page_range", type=str, default="all", help="页码范围")
    extract_parser.add_argument("--type", type=str, choices=['text', 'image'], default="text", help="提取类型")
    extract_parser.add_argument("-o", "--output", type=str, help="输出文件路径")

    # 分割子命令
    cut_parser = sub_parsers.add_parser("cut", help="分割", description="分割pdf文件")
    cut_parser.set_defaults(which='cut')
    cut_parser.add_argument("input_path", type=str, help="pdf文件路径")
    cut_parser.add_argument("--method", type=str, choices=['grid', 'breakpoints'], default="grid", help="分割模式")
    cut_parser.add_argument("--page_range", type=str, default="all", help="页码范围")
    cut_parser.add_argument("--h_breakpoints", type=float, nargs="+", help="水平分割点")
    cut_parser.add_argument("--v_breakpoints", type=float, nargs="+", help="垂直分割点")
    cut_parser.add_argument("--nrow", type=int, default=1, help="行数")
    cut_parser.add_argument("--ncol", type=int, default=1, help="列数")
    cut_parser.add_argument("-o", "--output", type=str, help="输出文件路径")

    # 组合子命令
    combine_parser = sub_parsers.add_parser("combine", help="组合", description="组合pdf文件")
    combine_parser.set_defaults(which='combine')
    combine_parser.add_argument("input_path", type=str, help="pdf文件路径")
    combine_parser.add_argument("--page_range", type=str, default="all", help="页码范围")
    combine_parser.add_argument("--nrow", type=int, default=1, help="行数")
    combine_parser.add_argument("--ncol", type=int, default=1, help="列数")
    combine_parser.add_argument("--paper_size", type=str, default="A4", help="纸张大小")
    combine_parser.add_argument("--orientation", type=str, choices=['portrait', 'landscape'], default="portrait", help="纸张方向")
    combine_parser.add_argument("-o", "--output", type=str, help="输出文件路径")

    # 裁剪子命令
    crop_parser = sub_parsers.add_parser("crop", help="裁剪", description="裁剪pdf文件")
    crop_parser.set_defaults(which='crop')
    crop_parser.add_argument("--method", type=str, choices=['bbox', 'margin', "annot"], default="bbox", help="裁剪模式")
    crop_parser.add_argument("input_path", type=str, help="pdf文件路径")
    crop_parser.add_argument("--page_range", type=str, default="all", help="页码范围")
    crop_parser.add_argument("--bbox", type=float, nargs=4, help="裁剪框")
    crop_parser.add_argument("--margin", type=float, nargs=4, help="裁剪边距")
    crop_parser.add_argument("--keep_size", action="store_true", help="保持裁剪后的尺寸不变")
    crop_parser.add_argument("--unit", type=str, choices=['pt', 'mm', 'cm', 'in'], default="pt", help="单位")
    crop_parser.add_argument("-o", "--output", type=str, help="输出文件路径")

    # 转换子命令
    convert_parser = sub_parsers.add_parser("convert", help="转换", description="转换pdf文件")
    convert_parser.set_defaults(which='convert')
    convert_parser.add_argument("input_path", type=str, nargs="+", help="输入文件列表")
    convert_parser.add_argument("--page_range", type=str, default="all", help="页码范围")
    convert_parser.add_argument("--source-type", type=str, default="pdf", help="源类型")
    convert_parser.add_argument("--target-type", type=str, default="png", help="目标类型")
    convert_parser.add_argument("--dpi", type=int, default=300, help="分辨率")
    convert_parser.add_argument("--paper-size", type=str, default="A4", help="纸张大小")
    convert_parser.add_argument("--orientation", type=str, choices=['portrait', 'landscape'], default="portrait", help="纸张方向")
    convert_parser.add_argument("--is_merge", action="store_true", help="是否合并")
    convert_parser.add_argument("--sort-method", type=str, choices=['custom', 'name', 'name_digit', 'ctime', 'mtime'], default="default", help="排序方式")
    convert_parser.add_argument("--sort-direction", type=str, choices=['asc', 'desc'], default="asc", help="排序方向")
    convert_parser.add_argument("-o", "--output", type=str, help="输出文件路径")

    # 遮罩子命令
    mask_parser = sub_parsers.add_parser("mask", help="遮罩", description="遮罩pdf文件")
    mask_parser.set_defaults(which='mask')
    mask_parser.add_argument("input_path", type=str, help="pdf文件路径")
    mask_parser.add_argument("--page_range", type=str, default="all", help="页码范围")
    mask_parser.add_argument("--type", type=str, choices=['rect', 'annot'], default="rectangle", help="遮罩类型")
    mask_parser.add_argument("--bbox", type=float, nargs=4, action='append', help="遮罩框")
    mask_parser.add_argument("--color", type=str, default="#FFFFFF", help="遮罩颜色")
    mask_parser.add_argument("--opacity", type=float, default=0.5, help="遮罩不透明度")
    mask_parser.add_argument("--angle", type=float, default=0, help="遮罩旋转角度")
    mask_parser.add_argument("--unit", type=str, choices=['pt', 'mm', 'cm', 'in'], default="pt", help="单位")
    mask_parser.add_argument("--annot-page", type=int, default=0, help="批注所在页码")
    mask_parser.add_argument("-o", "--output", type=str, help="输出文件路径")

    # 背景子命令
    bg_parser = sub_parsers.add_parser("bg", help="背景", description="添加背景")
    bg_parser.set_defaults(which='bg')
    bg_parser.add_argument("input_path", type=str, help="pdf文件路径")
    bg_parser.add_argument("--page_range", type=str, default="all", help="页码范围")
    bg_parser.add_argument("--type", type=str, choices=['color', 'image'], default="color", help="背景类型")
    bg_parser.add_argument("--color", type=str, default="#FFFFFF", help="背景颜色")
    bg_parser.add_argument("--opacity", type=float, default=0.5, help="背景不透明度")
    bg_parser.add_argument("--angle", type=float, default=0, help="背景旋转角度")
    bg_parser.add_argument("--x-offset", type=float, default=0, help="背景x轴偏移量")
    bg_parser.add_argument("--y-offset", type=float, default=0, help="背景y轴偏移量")
    bg_parser.add_argument("--scale", type=float, default=1, help="背景缩放比例")
    bg_parser.add_argument("--img-path", type=str, help="背景图片路径")
    bg_parser.add_argument("-o", "--output", type=str, help="输出文件路径")

    # 页眉页脚子命令
    header_footer_parser = sub_parsers.add_parser("header_footer", help="页眉页脚", description="添加页眉页脚")
    header_footer_parser.set_defaults(which='header_footer')
    header_footer_parser.add_argument("--type", type=str, choices=['add', 'remove'], default="add", help="操作类型")
    header_footer_parser.add_argument("input_path", type=str, help="pdf文件路径")
    header_footer_parser.add_argument("--page-range", type=str, default="all", help="页码范围")
    header_footer_parser.add_argument("--header-left", type=str, help="页眉左侧内容")
    header_footer_parser.add_argument("--header-center", type=str, help="页眉中间内容")
    header_footer_parser.add_argument("--header-right", type=str, help="页眉右侧内容")
    header_footer_parser.add_argument("--footer-left", type=str, help="页脚左侧内容")
    header_footer_parser.add_argument("--footer-center", type=str, help="页脚中间内容")
    header_footer_parser.add_argument("--footer-right", type=str, help="页脚右侧内容")
    header_footer_parser.add_argument("--font-family", type=str, help="字体类型")
    header_footer_parser.add_argument("--font-size", type=int, default=10, help="字体大小")
    header_footer_parser.add_argument("--font-color", type=str, default="#000000", help="字体颜色")
    header_footer_parser.add_argument("--opacity", type=float, default=1, help="字体不透明度")
    header_footer_parser.add_argument("--margin-bbox", type=float, nargs=4, default=[1.27, 1.27, 2.54, 2.54], help="页眉页脚边框, [上,下,左,右]")
    header_footer_parser.add_argument("--unit", type=str, choices=['pt', 'mm', 'cm', 'in'], default="cm", help="单位")
    header_footer_parser.add_argument("--remove", type=str, nargs="+", default=['header', 'footer'], help="删除页眉页脚")
    header_footer_parser.add_argument("-o", "--output", type=str, help="输出文件路径")

    # 页码子命令
    page_number_parser = sub_parsers.add_parser("page_number", help="页码", description="添加页码")
    page_number_parser.set_defaults(which='page_number')
    page_number_parser.add_argument("input_path", type=str, help="pdf文件路径")
    page_number_parser.add_argument("--type", type=str, choices=['add', 'remove'], default="add", help="操作类型")
    page_number_parser.add_argument("--page-range", type=str, default="all", help="页码范围")
    page_number_parser.add_argument("--start", type=int, default=1, help="起始页码")
    page_number_parser.add_argument("--format", type=str, default="第%p页", help="页码格式")
    page_number_parser.add_argument("--pos", type=str, choices=['header', 'footer'], default="footer", help="页码位置")
    page_number_parser.add_argument("--align", type=str, choices=['left', 'center', 'right'], default="right", help="页码对齐方式")
    page_number_parser.add_argument("--font-family", type=str, help="字体类型")
    page_number_parser.add_argument("--font-size", type=int, default=10, help="字体大小")
    page_number_parser.add_argument("--font-color", type=str, default="#000000", help="字体颜色")
    page_number_parser.add_argument("--opacity", type=float, default=1, help="字体不透明度")
    page_number_parser.add_argument("--margin-bbox", type=float, nargs=4, help="页眉页脚边框, [上,下,左,右]")
    page_number_parser.add_argument("--unit", type=str, choices=['pt', 'mm', 'cm', 'in'], default="pt", help="单位")
    page_number_parser.add_argument("-o", "--output", type=str, help="输出文件路径")

    # 双层PDF子命令
    dual_parser = sub_parsers.add_parser("dual", help="双层PDF", description="生成双层PDF")
    dual_parser.set_defaults(which='dual')
    dual_parser.add_argument("input_path", type=str, help="pdf文件路径")
    dual_parser.add_argument("--dpi", type=int, default=300, help="分辨率")
    dual_parser.add_argument("--page-range", type=str, default="all", help="页码范围")
    dual_parser.add_argument("--lang", type=str, default="ch", help="识别语言") # ['chi_sim', 'eng']
    dual_parser.add_argument("-o", "--output", type=str, help="输出文件路径")


    # 签名子命令
    sign_parser = sub_parsers.add_parser("sign", help="签名", description="生成电子签名")
    sign_parser.set_defaults(which="sign")
    sign_parser.add_argument("input_path", type=str, help="输入图片路径")
    sign_parser.add_argument("-o", "--output", type=str, help="输出文件路径")


    # Anki子命令
    anki_parser = sub_parsers.add_parser("anki", help="Anki", description="生成Anki卡片")
    anki_parser.set_defaults(which="anki")
    anki_parser.add_argument("input_path", type=str, help="pdf文件路径")
    anki_parser.add_argument("--type", type=str, help="操作")
    anki_parser.add_argument("--address", type=str, default="http://localhost:8765")
    anki_parser.add_argument("--parent-deck", type=str, help="父卡组")
    anki_parser.add_argument("--model", type=str, help='模板名称')
    anki_parser.add_argument("--field-mapping", type=str, help="字段映射")
    anki_parser.add_argument("--mode", type=str, nargs="+", help="模式")
    anki_parser.add_argument("--create-sub-deck", action="store_true", help="创建子卡组")
    anki_parser.add_argument("--level", type=int, default=2, help="标题层级")
    anki_parser.add_argument("--tags", type=str, nargs="+", help="标签")
    anki_parser.add_argument("--q-mask-color", type=str, default="#FF5656", help="问题遮罩颜色")
    anki_parser.add_argument("--a-mask-color", type=str, default="#FFEBA2", help="答案遮罩颜色")
    anki_parser.add_argument("--dpi", type=int, default=300, help="分辨率")
    anki_parser.add_argument("--matches", type=str, nargs="+", help="匹配条件")
    anki_parser.add_argument("--mask-types", type=str, nargs="+", default=['highlight', 'strikeout', 'underline', 'squiggly'], help="遮罩类型")
    anki_parser.add_argument("--image-mode", action="store_true", help="开启图片模式")
    anki_parser.add_argument("--page_range", type=str, default="all", help="页码范围")
    anki_parser.add_argument("--output", type=str, help="输出文件路径")
    return parser